#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Downloads and flattens datas from GPT
# Copyright (C) 2021 Mindbaz
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os;
import sys;
import pickle;

from googleapiclient.discovery import build;
from googleapiclient.errors import HttpError;
from multiprocessing import Pool;
from multiprocessing.managers import BaseManager;

sys.path.insert ( 0, os.path.dirname ( os.path.dirname ( os.path.abspath ( __file__ ) ) ) );
from googlepostmasterapi.datas import FlatDatas;
from googlepostmasterapi.stats import Stats;
from googlepostmasterapi.utils import write_std;

class GPostmaster ( object ):
    """Download datas from Google postmaster tools
    
    Attributes:
        _uri_tpl (string): Template to create an uri to get domain infos
        _domains (string[]): All domains download from server
        _service (googleapiclient.discovery.build): Connector to GPT
        _parser (FlatDatas): Connector to datas cleaner
        _stats (Stats): Connector to statistiques datas
        _pool_size (int): Pool size to calls
    """
    def __init__ ( self, token, pool_size = 2, verbose = False ):
        """Default constructor
        
        Arguments:
            token (string): Absolute file path to GPT token
            verbose (bool): Verbose mode. Default to False
        """
        """Verbose mode"""
        self.verbose = bool ( verbose );
        
        """Template to create an uri to get domain infos"""
        self._uri_tpl = 'domains/{domain}/trafficStats/{date}';
        
        """All domains download from server"""
        self._domains = [];
        
        """Pool size to calls"""
        self._pool_size = int ( pool_size );
        
        self._init_resources (
            token = token
        );
    
    
    def _init_resources ( self, token ):
        """Init resources used by system : init service / parser / stats
        
        Arguments:
            token (string): Absolute file path to GPT token
        """
        ## Init service
        self._init_service (
            token = token
        );
        
        ## Init parser
        self._init_parser_con ();
        
        ## Init stats
        self._init_stats_con ();
    
    
    def _init_stats_con ( self ):
        """Init stats con. Should be manager by multiprocessing to work with pool
        """
        BaseManager.register ( 'Stats', Stats );
        manager = BaseManager ();
        manager.start ();
        
        self._stats = manager.Stats ();
    
    
    def _load_token ( self, token ):
        """Load GPT token
        
        Arguments:
            token (string): Absolute file path to GPT token
        """
        with open ( token, 'rb' ) as token:
            return pickle.load ( token );
    
    
    def _init_service ( self, token ):
        """Init service connector
        
        Arguments:
            token (string): Absolute file path to GPT token
        """
        """Connector to Google Postmaster Tools"""
        self._service = build (
            'gmailpostmastertools',
            'v1beta1',
            credentials = self._load_token (
                token = token
            )
        );
    
    
    def _gpt_get_domains ( self ):
        """Call GPT to get all domains
        
        Returns:
            list: List of dict with all domains, format : [ { 'name': ..., 'createTime': ..., 'permission': ... } ]
        """
        return self._service.domains ().list ().execute ();
    
    
    def get_domains ( self ):
        """Get all domains with permissions : owner/reader
        """
        """All domains infos from GPT"""
        domains = self._gpt_get_domains ();
        
        for domain_datas in domains [ 'domains' ]:
            if ( domain_datas [ 'permission' ].lower () == 'none' ):
                continue;
            self._domains.append ( domain_datas [ 'name' ].split ( '/' ).pop () );
        
        write_std ( [
            'Download {} domain(s) from GPT'.format ( len ( self._domains ) )
        ] );
    
    
    def _create_domain_uri ( self, domain, input_date ):
        """Create URI to a domain to query
        
        Arguments:
            domain (string): Domain to query
            input_date (string): Date to query, format : YYYYMMDD
        """
        return self._uri_tpl.format (
            domain = domain,
            date = input_date
        );
    
    
    def _gpt_get_domain_info ( self, domain, input_date ):
        """Call GPT to get all infos to a domain
        
        Arguments:
            domain (string): Domain to query
            input_date (string): Date to query, format : YYYYMMDD
        
        Returns:
            dict: Process state & result
        """
        """Process state & result"""
        ret = {
            'state': True,
            'result': None
        };
        
        """Current domain uri to call"""
        uri = self._create_domain_uri (
            domain = domain,
            input_date = input_date
        );
        
        try:
            if ( self.verbose == True ):
                write_std ( [ 'Get domain info : {}'.format ( domain ) ] );
            ret [ 'result' ] = self._service.domains ().trafficStats ().get ( name = uri ).execute ();
            self._stats.add_ok ();
        except HttpError as e:
            ret [ 'state' ] = False;
            """Http code"""
            code = e.resp.status;
            """Error message"""
            err = e._get_reason ().strip ();
            self._stats.add_err_http (
                code = code,
                err = err,
                domain = domain
            );
        
        return ret;
    
    
    def _init_parser_con ( self ):
        """Init datas parser/cleaner con
        """
        self._parser = FlatDatas ();
    
    
    def _clean_domain_infos ( self, key, datas ):
        """Clean domain infos
        
        Arguments:
            key (string): Key to identify datas on cleaner
            datas (dict): Domain infos to clean
        
        Returns:
            dict: Cleaned datas
        """
        return self._parser.parse (
            key = key,
            datas = datas
        );
    
    
    def get_domain_infos ( self, domain, input_date, print_stats = True ):
        """Get infos to a domain
        
        Arguments:
            domain (string): Domain to query
            input_date (string): Date to query, format : YYYYMMDD
            print_stats (bool): True to display stats of the call. Defaut : True
        
        Returns:
            dict: Process state & domain infos
        """
        """Get domain infos"""
        ret = self._gpt_get_domain_info (
            domain = domain,
            input_date = input_date
        );
        
        ret [ 'domain' ] = domain;
        ret [ 'date' ] = input_date;
        
        if ( print_stats == True ):
            self._print_stats ();
        
        if ( ret [ 'state' ] == False ):
            return ret;
        
        ## Clean domain infos
        ret [ 'result' ] = self._clean_domain_infos (
            key = '{domain}-{date}'.format (
                domain = domain,
                date = input_date
            ),
            datas = ret [ 'result' ]
        );
        
        ret [ 'result' ] [ 'domain' ] = domain;
        ret [ 'result' ] [ 'date' ] = input_date;
        
        return ret;
    
    
    def _print_stats ( self ):
        """Display calls statistics
        """
        self._stats.print_stats ();
    
    
    def _create_pool_datas ( self, input_date ):
        """Create datas to map call on pool with all domains
        
        Arguments:
            input_date (string): Date to query
        
        Returns:
            dict[]: List of dict with domain&input_date
        """
        return [ { 'domain': x, 'input_date': input_date } for x in self._domains ];
    
    
    def _get_domain_infos_pool ( self, datas ):
        """Abstract call to get_domain_infos from pool with datas as dict
        
        Arguments:
            datas (dict): Values domain/input_date to send to get_domain_infos
        
        Returns:
            dict: Result from get_domain_infos calls
        """
        return self.get_domain_infos (
            domain = datas [ 'domain' ],
            input_date = datas [ 'input_date' ],
            print_stats = False
        );
    
    
    def _clean_pool_returns ( self, datas ):
        """Clean result from pool map returns : remove all state==false
        
        Arguments:
            datas (dict[]): List of dict from pool map
        
        Returns:
            dict[]: List of dict from pool map with only state==true
        """
        return [ x for x in datas if x [ 'state' ] == True ];
    
    
    def get_all_domains_infos ( self, input_date ):
        """Call GPT on all available domains
        
        Arguments:
            input_date (string): Date to query, format : YYYYMMDD
        
        Returns:
            list: All domain infos
        """
        """All domains infos"""
        ret = [];
        
        ## Get all domains
        self.get_domains ();
        
        """Datas as dict to method args"""
        datas = self._create_pool_datas (
            input_date = input_date
        );
        
        if ( len ( datas ) == 0 ):
            write_std ( [ 'Nothing to download' ] );
            return [];
        
        with Pool ( processes = self._pool_size ) as pool:
            ret = pool.map (
                self._get_domain_infos_pool,
                datas
            );
        
        ## Clean result
        ret = self._clean_pool_returns (
            datas = ret
        );
        
        self._print_stats ();
        
        return ret;

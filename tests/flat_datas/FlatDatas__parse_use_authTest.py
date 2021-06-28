#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas__parse_use_authTest ( unittest.TestCase ):
    def test_calls ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_use_auth (
            key = 'random-key',
            dkim = '0.1234',
            spf = '0.4567',
            dmarc = '0.789'
        );
            
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dkim_percent' ], 12.3 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_spf_percent' ], 45.7 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dmarc_percent' ], 78.9 );

        
    def test_no_dkim ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_use_auth (
            key = 'random-key',
            spf = '0.4567',
            dmarc = '0.789'
        );
            
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dkim_percent' ], None );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_spf_percent' ], 45.7 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dmarc_percent' ], 78.9 );

        
    def test_no_spf ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_use_auth (
            key = 'random-key',
            dkim = '0.1234',
            dmarc = '0.789'
        );
            
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dkim_percent' ], 12.3 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_spf_percent' ], None );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dmarc_percent' ], 78.9 );

        
    def test_no_dmarc ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_use_auth (
            key = 'random-key',
            dkim = '0.1234',
            spf = '0.4567'
        );
            
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dkim_percent' ], 12.3 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_spf_percent' ], 45.7 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dmarc_percent' ], None );

        
    def test_no_one ( self ):
        p = FlatDatas ();
        
        ret = p._parse_use_auth (
            key = 'random-key',);
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
            
        self.assertFalse ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dkim_percent' ], None );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_spf_percent' ], None );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dmarc_percent' ], None );

        
    def test_values_none ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_use_auth (
            key = 'random-key',
            dkim = None,
            spf = None,
            dmarc = None
        );
        
        self.assertFalse ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dkim_percent' ], None );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_spf_percent' ], None );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'auth_use_dmarc_percent' ], None );




        
        
if __name__ == '__main__':
    unittest.main ();

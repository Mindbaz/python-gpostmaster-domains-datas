#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas__parse_domain_reputationsTest ( unittest.TestCase ):
    def test_calls ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();

        p.dict_reputation = {
            'random-value-1': 'random-assoc-1',
            'random-value-2': 'random-assoc-2',
            'random-value-3': 'random-assoc-3'
        };
        
        ret = p._parse_domain_reputations (
            key = 'random-key',
            value = 'RANDOM-VALUE-1'
        );
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'domain_reputation' ], 'random-assoc-1' );

        
    def test_no_value ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();

        p.dict_reputation = {
            'random-value-1': 'random-assoc-1',
            'random-value-2': 'random-assoc-2',
            'random-value-3': 'random-assoc-3'
        };
        
        ret = p._parse_domain_reputations (
            key = 'random-key',
            value = None
        );
        self.assertFalse ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'domain_reputation' ], None );

        
    def test_unknow_value ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();

        p.dict_reputation = {
            'random-value-1': 'random-assoc-1',
            'random-value-2': 'random-assoc-2',
            'random-value-3': 'random-assoc-3'
        };
        
        ret = p._parse_domain_reputations (
            key = 'random-key',
            value = 'RANDOM-VALUE-4'
        );
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'domain_reputation' ], 0 );



        
        
if __name__ == '__main__':
    unittest.main ();

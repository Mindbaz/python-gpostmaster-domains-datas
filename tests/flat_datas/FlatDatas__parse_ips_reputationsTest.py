#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas__parse_ips_reputationsTest ( unittest.TestCase ):
    def test_calls ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_ips_reputations (
            key = 'random-key',
            value = [
                { 'reputation': 'HIGH', 'ipCount': 5, 'sampleIps': [ 'random-ip-high-1', 'random-ip-high-2' ] },
                { 'reputation': 'MEDIUM', 'sampleIps': [ 'random-ip-medium-1' ] },
                { 'reputation': 'LOW', 'ipCount': 37, 'sampleIps': [ 'random-ip-low-1' ] },
                { 'reputation': 'BAD', 'ipCount': 12, 'sampleIps': [ 'random-ip-bad-1', 'random-ip-bad-2', 'random-ip-bad-3' ] }
            ]
        );
        self.assertTrue ( ret );
        
        self.assertEqual ( p.datas [ 'random-key' ] [ 'ips_reputations' ], [
            { 'level': 4, 'value': 9.3, 'ips': 'random-ip-high-1;random-ip-high-2' },
            { 'level': 2, 'value': 68.5, 'ips': 'random-ip-low-1' },
            { 'level': 1, 'value': 22.2, 'ips': 'random-ip-bad-1;random-ip-bad-2;random-ip-bad-3' }
        ] );

        
    def test_no_datas ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_ips_reputations (
            key = 'random-key',
            value = None
        );
        self.assertFalse ( ret );
        self.assertEqual ( p.datas [ 'random-key' ] [ 'ips_reputations' ], [] );
        

        
        
        
if __name__ == '__main__':
    unittest.main ();

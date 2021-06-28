#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas__parse_crypted_inboundTest ( unittest.TestCase ):
    def test_calls ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_crypted_inbound (
            key = 'random-key',
            value = '0.4567'
        );
        
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'tls_inbound_percent' ], 45.7 );

        
    def test_no_value ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_crypted_inbound (
            key = 'random-key',
            value = None
        );
        
        self.assertFalse ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'tls_inbound_percent' ], None );




        
        
if __name__ == '__main__':
    unittest.main ();

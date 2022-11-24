#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas__parse_user_report_spamTest ( unittest.TestCase ):
    def test_calls ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_user_report_spam ( key = 'random-key', value = '0.1234' );
        self.assertTrue ( ret );
        self.assertEqual ( p.datas [ 'random-key' ] [ 'user_report_spam_percent' ], 12.3 );

        
    def test_no_value ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_user_report_spam ( key = 'random-key', value = None );
        self.assertFalse ( ret );
        self.assertEqual ( p.datas [ 'random-key' ] [ 'user_report_spam_percent' ], None );


        
        
if __name__ == '__main__':
    unittest.main ();

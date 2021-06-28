#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas__parse_feed_back_loopTest ( unittest.TestCase ):
    def test_calls ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_feed_back_loop (
            key = 'random-key',
            value = [
                { 'id': '123', 'spamRatio': 0.1234 },
                { 'id': '456', 'spamRatio': 0.4567 },
            ]
        );
            
        self.assertTrue ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'feedback_loop' ] [ 'nb_row' ], 2 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'feedback_loop' ] [ 'percent_per_uid' ], [
            { 'uid': 123, 'spam_percent': 12.3 },
            { 'uid': 456, 'spam_percent': 45.7 }
        ] );

        
    def test_no_value ( self ):
        p = FlatDatas ();
        p.datas [ 'random-key' ] = p._datas_tpl.copy ();
        
        ret = p._parse_feed_back_loop (
            key = 'random-key',
            value = None
        );
        
        self.assertFalse ( ret );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'feedback_loop' ] [ 'nb_row' ], 0 );
        self.assertEquals ( p.datas [ 'random-key' ] [ 'feedback_loop' ] [ 'percent_per_uid' ], [] );



        
        
if __name__ == '__main__':
    unittest.main ();

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.stats import Stats;


class Stats_add_err_httpTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.stats.Stats.add_err' ) as add_err:
            s = Stats ();
            s.datas = { 'err_http': {} };
            
            s.add_err_http (
                code = 'random-code',
                err = 'random-err',
                domain = 'random-domain'
            );
            
            self.assertEquals ( add_err.call_count, 1 );
            self.assertTrue ( 'random-code' in s.datas [ 'err_http' ] );
            self.assertTrue ( s.datas [ 'err_http' ] [ 'random-code' ] [ 'count' ], 1 );
            self.assertTrue ( s.datas [ 'err_http' ] [ 'random-code' ] [ 'domains' ], [ 'random-domain' ] );
            self.assertTrue ( s.datas [ 'err_http' ] [ 'random-code' ] [ 'message' ], 'random-err' );

            
    def test_new_err ( self ):
        with patch ( 'googlepostmasterapi.stats.Stats.add_err' ) as add_err:
            s = Stats ();
            s.datas = { 'err_http': {
                'another-code': { 'count': 12, 'domains': [ 'another-domain-1', 'another-domain-2' ], 'message': 'another-message' }
            } };
            
            s.add_err_http (
                code = 'random-code',
                err = 'random-err',
                domain = 'random-domain'
            );
            
            self.assertEquals ( add_err.call_count, 1 );
            self.assertEquals ( s.datas [ 'err_http' ], {
                'another-code': { 'count': 12, 'domains': [ 'another-domain-1', 'another-domain-2' ], 'message': 'another-message' },
                'random-code': { 'count': 1, 'domains': [ 'random-domain' ], 'message': 'random-err' }
            } );

            
    def test_add_domain ( self ):
        with patch ( 'googlepostmasterapi.stats.Stats.add_err' ) as add_err:
            s = Stats ();
            s.datas = { 'err_http': {
                'random-code': { 'count': 12, 'domains': [ 'random-domain-1', 'random-domain-2' ], 'message': 'random-message' }
            } };
            
            s.add_err_http (
                code = 'random-code',
                err = 'another-message',
                domain = 'random-domain-3'
            );
            
            self.assertEquals ( add_err.call_count, 1 );
            self.assertEquals ( s.datas [ 'err_http' ] [ 'random-code' ] [ 'count' ], 13 );
            self.assertEquals ( s.datas [ 'err_http' ] [ 'random-code' ] [ 'domains' ], [ 'random-domain-1', 'random-domain-2', 'random-domain-3' ] );
            self.assertEquals ( s.datas [ 'err_http' ] [ 'random-code' ] [ 'message' ], 'random-message' );
            
            
            
if __name__ == '__main__':
    unittest.main ();

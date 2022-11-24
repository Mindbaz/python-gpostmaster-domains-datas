#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;


class GPostmaster_get_domain_infosTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.GPostmaster._gpt_get_domain_info', return_value = { 'state': True, 'result': 'random-domain-info' } ) as get_info:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._clean_domain_infos', return_value = { 'random-key': 'random-datas-cleaned' } ) as clean_info:
                    with patch ( 'googlepostmasterapi.gpt.GPostmaster._print_stats' ) as print_stats:
                        w = GPostmaster (
                            token = 'random-token'
                        );
                        
                        ret = w.get_domain_infos (
                            domain = 'random-domain',
                            input_date = 'random-input-date'
                        );

                        self.assertTrue ( ret [ 'state' ] );
                        self.assertEqual ( ret [ 'result' ], { 'random-key': 'random-datas-cleaned', 'domain': 'random-domain', 'date': 'random-input-date' } );
                        self.assertEqual ( ret [ 'domain' ], 'random-domain' );
                        self.assertEqual ( ret [ 'date' ], 'random-input-date' );
                        get_info.assert_called_with (
                            domain = 'random-domain',
                            input_date = 'random-input-date'
                        );
                        clean_info.assert_called_with (
                            key = 'random-domain-random-input-date',
                            datas = 'random-domain-info'
                        );
                        self.assertEqual ( print_stats.call_count, 1 );

                        
    def test_get_info_return_false ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.GPostmaster._gpt_get_domain_info', return_value = { 'state': False } ) as get_info:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._clean_domain_infos', return_value = 'random-datas-cleaned' ) as clean_info:
                    with patch ( 'googlepostmasterapi.gpt.GPostmaster._print_stats' ) as print_stats:
                        w = GPostmaster (
                            token = 'random-token'
                        );
                        
                        ret = w.get_domain_infos (
                            domain = 'random-domain',
                            input_date = 'random-input-date'
                        );

                        self.assertFalse ( ret [ 'state' ] );
                        self.assertEqual ( ret [ 'domain' ], 'random-domain' );
                        self.assertEqual ( ret [ 'date' ], 'random-input-date' );
                        
                        get_info.assert_called_with (
                            domain = 'random-domain',
                            input_date = 'random-input-date'
                        );
                        clean_info.assert_not_called ();
                        self.assertEqual ( print_stats.call_count, 1 );

                        
    def test_do_not_print_sats ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.GPostmaster._gpt_get_domain_info', return_value = { 'state': True, 'result': 'random-domain-info' } ) as get_info:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._clean_domain_infos', return_value = { 'random-key': 'random-datas-cleaned' } ) as clean_info:
                    with patch ( 'googlepostmasterapi.gpt.GPostmaster._print_stats' ) as print_stats:
                        w = GPostmaster (
                            token = 'random-token'
                        );
                        
                        ret = w.get_domain_infos (
                            domain = 'random-domain',
                            input_date = 'random-input-date',
                            print_stats = False
                        );
                        
                        self.assertTrue ( ret [ 'state' ] );
                        self.assertEqual ( ret [ 'result' ], { 'random-key': 'random-datas-cleaned', 'domain': 'random-domain', 'date': 'random-input-date' } );
                        self.assertEqual ( ret [ 'domain' ], 'random-domain' );
                        self.assertEqual ( ret [ 'date' ], 'random-input-date' );
                        get_info.assert_called_with (
                            domain = 'random-domain',
                            input_date = 'random-input-date'
                        );
                        clean_info.assert_called_with (
                            key = 'random-domain-random-input-date',
                            datas = 'random-domain-info'
                        );
                        print_stats.assert_not_called ();
                    

                        
            
            
if __name__ == '__main__':
    unittest.main ();

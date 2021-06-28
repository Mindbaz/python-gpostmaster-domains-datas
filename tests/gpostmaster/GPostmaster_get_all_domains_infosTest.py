#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;


class PoolMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( '>> PoolMock : __init__' );
        pass;
    
    def __enter__ ( self, *args, **kargs ):
        print ( '>> PoolMock : __enter__' );
        return RMock ();
    
    def __exit__ ( self, *args, **kargs ):
        print ( '>> PoolMock : __exit__' );
        pass;

    
class RMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( '>> RMock : __init__' );
        pass;
    
    def map ( self, *args, **kargs ):
        print ( '>> RMock : map' );
        pass;

        
class GPostmaster_get_all_domains_infosTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.write_std' ) as write_std:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster.get_domains' ) as get_domains:
                    with patch ( 'googlepostmasterapi.gpt.GPostmaster._create_pool_datas', return_value = [ 'random-pool-datas' ] ) as create_pool_datas:
                        with patch ( 'googlepostmasterapi.gpt.Pool', side_effect = PoolMock ) as init_pool:
                            with patch ( 'tests.gpostmaster.GPostmaster_get_all_domains_infosTest.RMock.map', return_value = 'random-map-returns' ) as map_call:
                                with patch ( 'googlepostmasterapi.gpt.GPostmaster._clean_pool_returns', return_value = 'random-cleaned-datas' ) as clean_pool_returns:
                                    with patch ( 'googlepostmasterapi.gpt.GPostmaster._print_stats' ) as print_stats:
                                        w = GPostmaster (
                                            token = 'random-token'
                                        );
                                        w._pool_size = 52;
                                        
                                        ret = w.get_all_domains_infos (
                                            input_date = 'random-input-date'
                                        );
                                        
                                        self.assertEquals ( ret, 'random-cleaned-datas' );
                                        self.assertEquals ( get_domains.call_count, 1 );
                                        create_pool_datas.assert_called_with (
                                            input_date = 'random-input-date'
                                        );
                                        init_pool.assert_called_with (
                                            processes = 52
                                        );
                                        self.assertEquals ( map_call.call_count, 1 );
                                        for call in map_call.call_args_list:
                                            args, kwargs = call;
                                            self.assertEquals ( args [ 0 ], w._get_domain_infos_pool );
                                            self.assertEquals ( args [ 1 ], [ 'random-pool-datas' ] );
                                        clean_pool_returns.assert_called_with (
                                            datas = 'random-map-returns'
                                        );
                                        self.assertEquals ( print_stats.call_count, 1 );
                                        write_std.assert_not_called ();

                                        
    def test_nothing_to_fecth ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.write_std' ) as write_std:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster.get_domains' ) as get_domains:
                    with patch ( 'googlepostmasterapi.gpt.GPostmaster._create_pool_datas', return_value = [] ) as create_pool_datas:
                        with patch ( 'googlepostmasterapi.gpt.Pool', side_effect = PoolMock ) as init_pool:
                            with patch ( 'tests.gpostmaster.GPostmaster_get_all_domains_infosTest.RMock.map', return_value = 'random-map-returns' ) as map_call:
                                with patch ( 'googlepostmasterapi.gpt.GPostmaster._clean_pool_returns', return_value = 'random-cleaned-datas' ) as clean_pool_returns:
                                    with patch ( 'googlepostmasterapi.gpt.GPostmaster._print_stats' ) as print_stats:
                                        w = GPostmaster (
                                            token = 'random-token'
                                        );
                                        w._pool_size = 52;
                                        
                                        ret = w.get_all_domains_infos (
                                            input_date = 'random-input-date'
                                        );
                                        
                                        self.assertEquals ( ret, [] );
                                        self.assertEquals ( get_domains.call_count, 1 );
                                        create_pool_datas.assert_called_with (
                                            input_date = 'random-input-date'
                                        );
                                        init_pool.assert_not_called ();
                                        map_call.assert_not_called ();
                                        clean_pool_returns.assert_not_called ();
                                        print_stats.assert_not_called ();
                                        write_std.assert_called_with ( [ 'Nothing to download' ] );
            
            
if __name__ == '__main__':
    unittest.main ();

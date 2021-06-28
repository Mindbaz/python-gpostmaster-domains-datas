#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googleapiclient.errors import HttpError;
from googlepostmasterapi.gpt import GPostmaster;


class RMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'RMock : __init__' );
        pass;
    
    def domains ( self, *args, **kargs ):
        print ( 'RMock : domains' );
        pass;
    
    def trafficStats ( self, *args, **kargs ):
        print ( 'RMock : trafficStats' );
        pass;
    
    def get ( self, *args, **kargs ):
        print ( 'RMock : get' );
        pass;
    
    def execute ( self, *args, **kargs ):
        print ( 'RMock : execute' );
        pass;

    
class HttpErrorMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'HttpErrorMock : __init__' );
        self.status = 123;
        self.reason = 'random-reason';
        pass;


class StatsMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'StatsMock : __init__' );
        pass;
    
    def add_ok ( self, *args, **kargs ):
        print ( 'StatsMock : add_ok' );
        pass;
    
    def add_err_http ( self, *args, **kargs ):
        print ( 'StatsMock : add_err_http' );
        pass;
    

class GPostmaster__gpt_get_domain_infoTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.write_std' ) as write_std:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._create_domain_uri' ) as create_uri:
                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.domains', return_value = RMock () ) as domains_call:
                        with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.trafficStats', return_value = RMock () ) as stats_call:
                            with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.get', return_value = RMock () ) as get_call:
                                with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.execute', return_value = 'random-returns' ) as execute_call:
                                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.StatsMock.add_ok' ) as stats_add_ok:            
                                        with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.StatsMock.add_err_http' ) as stats_add_err_http:
                                            w = GPostmaster (
                                                token = 'random-token'
                                            );
                                            w._service = RMock ();
                                            w._stats = StatsMock ();
                                            
                                            ret = w._gpt_get_domain_info (
                                                domain = 'random-domain',
                                                input_date = 'random-input-date'
                                            );
                                            
                                            self.assertTrue ( ret [ 'state' ] );
                                            self.assertEquals ( ret [ 'result' ], 'random-returns' );
                                            
                                            create_uri.assert_called_with (
                                                domain = 'random-domain',
                                                input_date = 'random-input-date'
                                            );
                                            write_std.assert_not_called ();
                                            self.assertEquals ( stats_add_ok.call_count, 1 );
                                            stats_add_err_http.assert_not_called ();

                                    
    def test_call_raise_exception ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.write_std' ) as write_std:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._create_domain_uri' ) as create_uri:
                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.domains', side_effect = HttpError ( HttpErrorMock (), b'random-exception' ) ) as domains_call:
                        with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.StatsMock.add_ok' ) as stats_add_ok:            
                            with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.StatsMock.add_err_http' ) as stats_add_err_http:
                                w = GPostmaster (
                                    token = 'random-token'
                                );
                                w._service = RMock ();
                                w._stats = StatsMock ();
                                
                                ret = w._gpt_get_domain_info (
                                    domain = 'random-domain',
                                    input_date = 'random-input-date'
                                );
                                
                                self.assertFalse ( ret [ 'state' ] );
                                self.assertEquals ( ret [ 'result' ], None );
                                
                                create_uri.assert_called_with (
                                    domain = 'random-domain',
                                    input_date = 'random-input-date'
                                );
                                write_std.assert_not_called ();
                                stats_add_ok.assert_not_called ();
                                stats_add_err_http.assert_called_with (
                                    code = 123,
                                    err = 'random-reason',
                                    domain = 'random-domain'
                                );

                                
    def test_verbose_mode ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.write_std' ) as write_std:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._create_domain_uri' ) as create_uri:
                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.domains', return_value = RMock () ) as domains_call:
                        with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.trafficStats', return_value = RMock () ) as stats_call:
                            with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.get', return_value = RMock () ) as get_call:
                                with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.RMock.execute', return_value = 'random-returns' ) as execute_call:
                                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.StatsMock.add_ok' ) as stats_add_ok:            
                                        with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domain_infoTest.StatsMock.add_err_http' ) as stats_add_err_http:
                                            w = GPostmaster (
                                                token = 'random-token',
                                                verbose = True
                                            );
                                            w._service = RMock ();
                                            w._stats = StatsMock ();
                                            
                                            ret = w._gpt_get_domain_info (
                                                domain = 'random-domain',
                                                input_date = 'random-input-date'
                                            );
                                            
                                            self.assertTrue ( ret [ 'state' ] );
                                            self.assertEquals ( ret [ 'result' ], 'random-returns' );
                                            
                                            create_uri.assert_called_with (
                                                domain = 'random-domain',
                                                input_date = 'random-input-date'
                                            );
                                            write_std.assert_called_with ( [ 'Get domain info : random-domain' ] );
                                            self.assertEquals ( stats_add_ok.call_count, 1 );
                                            stats_add_err_http.assert_not_called ();
                                

                    
                        
            
            
if __name__ == '__main__':
    unittest.main ();

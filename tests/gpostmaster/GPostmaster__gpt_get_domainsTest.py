#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;


class RMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'RMock : __init__' );
        pass;
    
    def domains ( self, *args, **kargs ):
        print ( 'RMock : domains' );
        pass;
    
    def list ( self, *args, **kargs ):
        print ( 'RMock : list' );
        pass;
    
    def execute ( self, *args, **kargs ):
        print ( 'RMock : execute' );
        pass;


class GPostmaster__gpt_get_domainsTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.domains', return_value = RMock () ) as domains_call:
                with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.list', return_value = RMock () ) as list_call:
                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.execute', return_value = 'random-returns' ) as execute_call:
                        with patch ( 'googlepostmasterapi.gpt.recursive_call' ) as r_call:
                            w = GPostmaster (
                                token = 'random-token'
                            );
                            w._service = RMock ();
                            
                            ret = w._gpt_get_domains ();
                            
                            self.assertEqual ( ret, 'random-returns' );
                            domains_call.assert_called_once_with ();
                            list_call.assert_called_once_with (
                                pageToken = None
                            );
                            execute_call.assert_called_once_with ();
                            r_call.assert_not_called ();

                            
    def test_arg_next_page ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.domains', return_value = RMock () ) as domains_call:
                with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.list', return_value = RMock () ) as list_call:
                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.execute', return_value = 'random-returns' ) as execute_call:
                        with patch ( 'googlepostmasterapi.gpt.recursive_call' ) as r_call:
                            w = GPostmaster (
                                token = 'random-token'
                            );
                            w._service = RMock ();
                            
                            ret = w._gpt_get_domains (
                                next_page = 'random-next-page'
                            );
                            
                            self.assertEqual ( ret, 'random-returns' );
                            domains_call.assert_called_once_with ();
                            list_call.assert_called_once_with (
                                pageToken = 'random-next-page'
                            );
                            execute_call.assert_called_once_with ();
                            r_call.assert_not_called ();

                            
    def test_recursive_on_pagination ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.domains', return_value = RMock () ) as domains_call:
                with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.list', return_value = RMock () ) as list_call:
                    with patch ( 'tests.gpostmaster.GPostmaster__gpt_get_domainsTest.RMock.execute' ) as execute_call:
                        with patch ( 'googlepostmasterapi.gpt.recursive_call' ) as r_call:
                            execute_call.return_value = {
                                'nextPageToken': 'random-next-page-token',
                                'domains': [ 'random-domain-1', 'random-domain-2' ]
                            };
                            r_call.return_value = {
                                'domains': [ 'random-domain-3' ]
                            };
                            
                            w = GPostmaster (
                                token = 'random-token'
                            );
                            w._service = RMock ();
                            
                            ret = w._gpt_get_domains ();
                            
                            self.assertEqual ( ret, {
                                'nextPageToken': 'random-next-page-token',
                                'domains': [
                                    'random-domain-1',
                                    'random-domain-2',
                                    'random-domain-3'
                                ]
                            } );
                            domains_call.assert_called_once_with ();
                            list_call.assert_called_once_with (
                                pageToken = None
                            );
                            execute_call.assert_called_once_with ();
                            r_call.assert_called_once_with (
                                w._gpt_get_domains,
                                next_page = 'random-next-page-token'
                            );

                        
            
            
if __name__ == '__main__':
    unittest.main ();

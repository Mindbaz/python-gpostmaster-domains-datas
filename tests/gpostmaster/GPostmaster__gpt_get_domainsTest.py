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
                        w = GPostmaster (
                            token = 'random-token'
                        );
                        w._service = RMock ();

                        ret = w._gpt_get_domains ();

                        self.assertEquals ( ret, 'random-returns' );
                        self.assertEquals ( domains_call.call_count, 1 );
                        self.assertEquals ( list_call.call_count, 1 );
                        self.assertEquals ( execute_call.call_count, 1 );

                        
            
            
if __name__ == '__main__':
    unittest.main ();

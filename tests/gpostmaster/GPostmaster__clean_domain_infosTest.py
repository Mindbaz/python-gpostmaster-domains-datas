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
    
    def parse ( self, *args, **kargs ):
        print ( 'RMock : parse' );
        pass;


class GPostmaster__clean_domain_infosTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'tests.gpostmaster.GPostmaster__clean_domain_infosTest.RMock.parse', return_value = 'random-returns' ) as parse_call:
                w = GPostmaster (
                    token = 'random-token'
                );
                w._parser = RMock ();
                
                ret = w._clean_domain_infos (
                    key = 'random-key',
                    datas = 'random-datas'
                );
                
                self.assertEquals ( ret, 'random-returns' );
                parse_call.assert_called_with (
                    key = 'random-key',
                    datas = 'random-datas'
                );

                    

                        
            
            
if __name__ == '__main__':
    unittest.main ();

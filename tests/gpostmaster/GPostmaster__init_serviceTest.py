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

    
class GPostmaster__init_serviceTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.GPostmaster._load_token', return_value = 'random-datas' ) as load_credentials:
                with patch ( 'googlepostmasterapi.gpt.build', side_effect = RMock ) as build_call:
                    w = GPostmaster (
                        token = 'random-token'
                    );
                    
                    w._init_service (
                        token = 'another-credentials'
                    );
                    
                    self.assertTrue ( isinstance ( w._service, RMock ) );
                    load_credentials.assert_called_with (
                        token = 'another-credentials'
                    );
                    build_call.assert_called_with (
                        'gmailpostmastertools',
                        'v1beta1',
                        credentials = 'random-datas'
                    );

                        
            
            
if __name__ == '__main__':
    unittest.main ();

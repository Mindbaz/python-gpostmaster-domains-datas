#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;


class HandleMock ( object ):    
    def read ( self, *args, **kargs ):
        print ( 'HandleMock : read' );
        pass;


class OpenMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'OpenMock : __init__' );
        pass;
    
    def __open__ ( self, *args, **kargs ):
        print ( 'OpenMock : __open__' );
        pass;
    
    def __enter__ ( self, *args, **kargs ):
        print ( 'OpenMock : __enter__' );
        return HandleMock;
    
    def __exit__ ( self, *args, **kargs ):
        print ( 'OpenMock : __exit__' );
        pass;

    
class PickleMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'OpenMock : __init__' );
        pass;
    
    def load ( self, *args, **kargs ):
        print ( 'OpenMock : load' );
        pass;

@patch ( 'googlepostmasterapi.gpt.pickle', PickleMock )
class GPostmaster__load_tokenTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.open', side_effect = OpenMock ) as open_call:
                with patch ( 'googlepostmasterapi.gpt.pickle.load', return_value = 'random-returns' ) as p_load:
                    w = GPostmaster (
                        token = 'random-token'
                    );

                    ret = w._load_token (
                        token = 'another-credentials'
                    );

                    self.assertEquals ( ret, 'random-returns' );
                    open_call.asser_called_with (
                        'another-credentials',
                        'rb'
                    );
                    self.assertEquals ( p_load.call_count, 1 );
                    for call in p_load.call_args_list:
                        args, kwargs = call;
                        self.assertEquals ( args [ 0 ], HandleMock );
                        
            
            
if __name__ == '__main__':
    unittest.main ();

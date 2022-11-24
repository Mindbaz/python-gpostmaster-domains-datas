#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;

class GPostmaster_constructorTest ( unittest.TestCase ):
    def test_constructor ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            w = GPostmaster (
                token = 'random-token'
            );
            
            init_ressources.assert_called_with (
                token = 'random-token'
            );
            
            self.assertFalse ( w.verbose );
            self.assertTrue ( type ( w._uri_tpl ) is str );
            self.assertTrue ( len ( w._uri_tpl ) > 0 );
            self.assertEqual ( w._domains, [] );
            self.assertEqual ( w._pool_size, 2 );

                
    def test_pool_size ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            w = GPostmaster (
                token = 'random-token',
                pool_size = '951'
            );
            self.assertEqual ( w._pool_size, 951 );
              
                
    def test_verbose ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            w = GPostmaster (
                token = 'random-token',
                verbose = True
            );
            self.assertTrue ( w.verbose );

        
        
        
if __name__ == '__main__':
    unittest.main ();

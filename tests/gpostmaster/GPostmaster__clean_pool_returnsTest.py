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


class GPostmaster__clean_pool_returnsTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            w = GPostmaster (
                token = 'random-token'
            );
            
            
            ret = w._clean_pool_returns (
                datas = [
                    { 'state': False, 'key': 'random-datas-1' },
                    { 'state': True, 'key': 'random-datas-2' },
                    { 'state': False, 'key': 'random-datas-3' },
                    { 'state': True, 'key': 'random-datas-4' }
                ] );
            self.assertEqual ( ret, [
                { 'state': True, 'key': 'random-datas-2' },
                { 'state': True, 'key': 'random-datas-4' }
            ] );
                
        
            
            
if __name__ == '__main__':
    unittest.main ();

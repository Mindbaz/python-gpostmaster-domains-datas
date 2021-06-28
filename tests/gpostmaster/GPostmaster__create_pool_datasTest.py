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


class GPostmaster__create_pool_datasTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            w = GPostmaster (
                token = 'random-token'
            );
            w._domains = [ 'random-domain-1', 'random-domain-2', 'random-domain-3' ];
            
            ret = w._create_pool_datas (
                input_date = 'random-input-date'
            );
            self.assertEquals ( ret, [
                { 'domain': 'random-domain-1', 'input_date': 'random-input-date' },
                { 'domain': 'random-domain-2', 'input_date': 'random-input-date' },
                { 'domain': 'random-domain-3', 'input_date': 'random-input-date' }
            ] );
        
            
            
if __name__ == '__main__':
    unittest.main ();

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


class GPostmaster__get_domain_infos_poolTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.GPostmaster.get_domain_infos', return_value = 'random-returns' ) as get_domain_infos:
                w = GPostmaster (
                    token = 'random-token'
                );


                ret = w._get_domain_infos_pool (
                    datas = {
                        'domain': 'random-domain',
                        'input_date': 'random-input-date'
                    } );
                self.assertEquals ( ret, 'random-returns' );
                get_domain_infos.assert_called_with (
                    domain = 'random-domain',
                    input_date = 'random-input-date',
                    print_stats = False
                );
        
            
            
if __name__ == '__main__':
    unittest.main ();

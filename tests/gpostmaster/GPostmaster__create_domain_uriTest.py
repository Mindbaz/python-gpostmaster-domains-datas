#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;


class GPostmaster__create_domain_uriTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            w = GPostmaster (
                token = 'random-token'
            );
            w._uri_tpl = 'random uri with : {domain} / {date}';
            
            ret = w._create_domain_uri (
                domain = 'random-domain',
                input_date = 'random-input-date'
            );

            self.assertEquals ( ret, 'random uri with : random-domain / random-input-date' );

                    

                        
            
            
if __name__ == '__main__':
    unittest.main ();

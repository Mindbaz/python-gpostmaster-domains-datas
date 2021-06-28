#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;

class GPostmaster__init_resourcesTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_service' ) as init_service:
            with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_parser_con' ) as init_parser:
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_stats_con' ) as init_stats:
                    w = GPostmaster (
                        token = 'random-token'
                    );
                    
                    init_service.assert_called_with (
                        token = 'random-token'
                    );
                    self.assertEquals ( init_parser.call_count, 1 );
                    self.assertEquals ( init_stats.call_count, 1 );
            
            
if __name__ == '__main__':
    unittest.main ();

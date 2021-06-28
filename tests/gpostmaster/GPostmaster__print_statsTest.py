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


class StatsMock ( object ):
    def __init__ ( self, *args, **kargs ):
        print ( 'StatsMock : __init__' );
        pass;
    
    def print_stats ( self, *args, **kargs ):
        print ( 'StatsMock : print_stats' );
        pass;
    

class GPostmaster__print_statsTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'tests.gpostmaster.GPostmaster__print_statsTest.StatsMock.print_stats' ) as print_stats:
                w = GPostmaster (
                    token = 'random-token'
                );
                w._stats = StatsMock ();

                w._print_stats ();
                self.assertEquals ( print_stats.call_count, 1 );
                
            
            
if __name__ == '__main__':
    unittest.main ();

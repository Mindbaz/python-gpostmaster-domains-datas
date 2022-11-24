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
    
    def register ( self, *args, **kargs ):
        print ( 'RMock : register' );
        pass;
    
    def start ( self, *args, **kargs ):
        print ( 'RMock : start' );
        pass;
    
    def Stats ( self, *args, **kargs ):
        print ( 'RMock : Stats' );
        pass;
    

class GPostmaster__init_stats_conTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_resssources:
            with patch ( 'googlepostmasterapi.gpt.BaseManager', side_effect = RMock ) as base_manager:
                with patch ( 'googlepostmasterapi.gpt.BaseManager.register' ) as register:
                    with patch ( 'tests.gpostmaster.GPostmaster__init_stats_conTest.RMock.start' ) as start:
                        with patch ( 'tests.gpostmaster.GPostmaster__init_stats_conTest.RMock.Stats', return_value = 'random-stats-instance' ) as stats:
                            w = GPostmaster (
                                token = 'random-token'
                            );
                            
                            w._init_stats_con ();
                            
                            self.assertEqual ( w._stats, 'random-stats-instance' );
                            self.assertEqual ( register.call_count, 1 );
                            for call in register.call_args_list:
                                args, kwargs = call;
                                self.assertEqual ( args [ 0 ], 'Stats' );
                                self.assertEqual ( args [ 1 ].__name__, 'Stats' );
                            self.assertEqual ( base_manager.call_count, 1 );
                            self.assertEqual ( start.call_count, 1 );
                            self.assertEqual ( stats.call_count, 1 );
                                
                                
            
if __name__ == '__main__':
    unittest.main ();

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.stats import Stats;


class Stats_constructorTest ( unittest.TestCase ):
    def test_constructor ( self ):
        s = Stats ();
        
        self.assertTrue ( type ( s.datas ) is dict );
        self.assertEqual ( s.datas [ 'total' ], 0 );
        self.assertEqual ( s.datas [ 'ok' ], 0 );
        self.assertEqual ( s.datas [ 'err' ], 0 );
        self.assertEqual ( s.datas [ 'err_http' ], {} );

                        
            
if __name__ == '__main__':
    unittest.main ();

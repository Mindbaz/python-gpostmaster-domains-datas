#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.stats import Stats;


class Stats_add_totalTest ( unittest.TestCase ):
    def test_calls ( self ):
        s = Stats ();
        s.datas = { 'total': 123 };
        s.add_total ();
        
        self.assertEquals ( s.datas [ 'total' ], 124 );


                    

                        
            
            
if __name__ == '__main__':
    unittest.main ();

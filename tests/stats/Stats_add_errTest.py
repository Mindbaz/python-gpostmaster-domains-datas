#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.stats import Stats;


class Stats_add_errTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.stats.Stats.add_total' ) as add_total:
            s = Stats ();
            s.datas = { 'err': 789 };
            s.add_err ();
            self.assertEqual ( s.datas [ 'err' ], 790 );
            self.assertEqual ( add_total.call_count, 1 );
            
            
            
if __name__ == '__main__':
    unittest.main ();

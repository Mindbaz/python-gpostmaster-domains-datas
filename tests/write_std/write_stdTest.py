#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.utils import write_std;

class write_stdTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.utils.sys.stdout.write' ) as w_stdout:
            write_std ( [
                'random-line-1',
                'random-line-2',
                'random-line-3'
            ] );

            self.assertEquals ( w_stdout.call_count, 3 );
            w_stdout.assert_any_call ( "random-line-1\n" );
            w_stdout.assert_any_call ( "random-line-2\n" );
            w_stdout.assert_any_call ( "random-line-3\n" );

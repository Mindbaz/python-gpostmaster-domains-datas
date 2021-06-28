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


class GPostmaster__init_parser_conTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.FlatDatas', side_effect= RMock ) as parser_call:
                w = GPostmaster (
                    token = 'random-token'
                );

                w._init_parser_con ();
                self.assertTrue ( isinstance ( w._parser, RMock ) );
            
            
if __name__ == '__main__':
    unittest.main ();

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas_constructorTest ( unittest.TestCase ):
    def test_constructor ( self ):
        p = FlatDatas ();

        self.assertEqual ( p.datas, {} );
        self.assertTrue ( type ( p._datas_tpl ) is dict );
        self.assertEqual ( len ( p._datas_tpl.keys () ), 9 );
        self.assertTrue ( type ( p.dict_reputation ) is dict );
        self.assertEqual ( len ( p.dict_reputation.keys () ), 5 );

        
    def test_datas_tpl_values ( self ):
        p = FlatDatas ();

        ## None
        for k in [ 'user_report_spam_percent', 'domain_reputation', 'auth_use_dkim_percent', 'auth_use_spf_percent', 'auth_use_dmarc_percent', 'tls_inbound_percent' ]:
            self.assertEqual ( p._datas_tpl [ k ], None );

        ## FBL
        for k in [ 'feedback_loop' ]:
            self.assertEqual ( p._datas_tpl [ k ] [ 'nb_row' ], 0 );
            self.assertEqual ( p._datas_tpl [ k ] [ 'percent_per_uid' ], [] );

        ## []
        for k in [ 'delivery_errors', 'ips_reputations' ]:
            self.assertEqual ( p._datas_tpl [ k ], [] );

        
    def test_dict_reputation_values ( self ):
        p = FlatDatas ();

        ## None
        for k in [ 'high', 'medium', 'low', 'bad', 'unknow' ]:
            self.assertTrue ( k in p.dict_reputation );
        
        
if __name__ == '__main__':
    unittest.main ();

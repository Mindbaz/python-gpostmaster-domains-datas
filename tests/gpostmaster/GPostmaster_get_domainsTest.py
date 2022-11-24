#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.gpt import GPostmaster;


class GPostmaster_get_domainsTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.write_std' ) as write_std:
                DS = { 'domains': [
                    { 'name': '/random-domain-1', 'permission': 'random-perm-1' },
                    { 'name': '/random-domain-2', 'permission': 'None' },
                    { 'name': '/random-domain-3', 'permission': 'random-perm-3' }
                ] };
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._gpt_get_domains', return_value = DS ) as gpt_get_domains:
                    w = GPostmaster (
                        token = 'random-token'
                    );

                    w.get_domains ();
                    
                    self.assertEqual ( w._domains, [ 'random-domain-1', 'random-domain-3' ] );
                    self.assertEqual ( gpt_get_domains.call_count, 1 );
                    write_std.asser_called_with ( [
                        'Download 2 domain(s) from GPT'
                    ] );

                    
    def test_no_domains ( self ):
        with patch ( 'googlepostmasterapi.gpt.GPostmaster._init_resources' ) as init_ressources:
            with patch ( 'googlepostmasterapi.gpt.write_std' ) as write_std:
                DS = { 'domains': [] };
                with patch ( 'googlepostmasterapi.gpt.GPostmaster._gpt_get_domains', return_value = DS ) as gpt_get_domains:
                    w = GPostmaster (
                        token = 'random-token'
                    );

                    w.get_domains ();
                    
                    self.assertEqual ( w._domains, [] );
                    self.assertEqual ( gpt_get_domains.call_count, 1 );
                    write_std.asser_called_with ( [
                        'Download 0 domain(s) from GPT'
                    ] );
                    

                        
            
            
if __name__ == '__main__':
    unittest.main ();

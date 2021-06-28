#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
from shutil import copyfile;
from unittest.mock import patch, Mock;
from datetime import datetime;

from pprint import pprint ;

from googlepostmasterapi.datas import FlatDatas;

class FlatDatas_parseTest ( unittest.TestCase ):
    def test_calls ( self ):
        with patch ( 'googlepostmasterapi.datas.copy.deepcopy', return_value = 'random-dict' ) as deep_copy:
            with patch ( 'googlepostmasterapi.datas.FlatDatas._parse_user_report_spam' ) as parse_user_report_spam:
                with patch ( 'googlepostmasterapi.datas.FlatDatas._parse_ips_reputations' ) as parse_ips_reputations:
                    with patch ( 'googlepostmasterapi.datas.FlatDatas._parse_domain_reputations' ) as parse_domain_reputations:
                        with patch ( 'googlepostmasterapi.datas.FlatDatas._parse_feed_back_loop' ) as parse_feed_back_loop:
                            with patch ( 'googlepostmasterapi.datas.FlatDatas._parse_use_auth' ) as parse_use_auth:
                                with patch ( 'googlepostmasterapi.datas.FlatDatas._parse_crypted_inbound' ) as parse_crypted_inbound:
                                    with patch ( 'googlepostmasterapi.datas.FlatDatas._parse_delivery_err' ) as parse_delivery_err:        
                                        p = FlatDatas ();
                                        p._datas_tpl = { 'random-key': 'random-value' };
                                        
                                        ret = p.parse (
                                            key = 'random-key',
                                            datas = {
                                                'userReportedSpamRatio': 'random-user-reported-spam-ratio',
                                                'ipReputations': 'random-ip-reputations',
                                                'domainReputation': 'random-domain-reputation',
                                                'spammyFeedbackLoops': 'random-spammy-feedback-loops',
                                                'dkimSuccessRatio': 'random-dkim-success-ratio',
                                                'spfSuccessRatio': 'random-spf-success-ratio',
                                                'dmarcSuccessRatio': 'random-dmarc-success-ratio',
                                                'inboundEncryptionRatio': 'random-inbound-encryption-ratio',
                                                'deliveryErrors': 'random-delivery-errors',
                                            }
                                        );
                                        self.assertEquals ( ret, 'random-dict' );
                                        
                                        self.assertTrue ( 'random-key' not in p.datas );
                                        
                                        self.assertEquals ( deep_copy.call_count, 2 );
                                        deep_copy.assert_any_call ( { 'random-key': 'random-value' } );
                                        deep_copy.assert_any_call ( 'random-dict' );
                                        parse_user_report_spam.assert_called_with (
                                            key = 'random-key',
                                            value = 'random-user-reported-spam-ratio'
                                        );
                                        parse_ips_reputations.assert_called_with (
                                            key = 'random-key',
                                            value = 'random-ip-reputations'
                                        );
                                        parse_domain_reputations.assert_called_with (
                                            key = 'random-key',
                                            value = 'random-domain-reputation'
                                        );
                                        parse_feed_back_loop.assert_called_with (
                                            key = 'random-key',
                                            value = 'random-spammy-feedback-loops'
                                        );
                                        parse_use_auth.assert_called_with (
                                            key = 'random-key',
                                            dkim = 'random-dkim-success-ratio',
                                            spf = 'random-spf-success-ratio',
                                            dmarc = 'random-dmarc-success-ratio'
                                        );
                                        parse_crypted_inbound.assert_called_with (
                                            key = 'random-key',
                                            value = 'random-inbound-encryption-ratio'
                                        );
                                        parse_delivery_err.assert_called_with (
                                            key = 'random-key',
                                            value = 'random-delivery-errors'
                                        );
        
        
if __name__ == '__main__':
    unittest.main ();

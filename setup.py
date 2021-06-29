#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Mindbaz
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os;
from setuptools import setup;

with open ( os.path.join ( os.path.dirname ( os.path.abspath ( __file__ ) ), 'README.md' ) , 'r', encoding='utf-8' ) as fh:
    long_description = fh.read ();
    
from googlepostmasterapi import __version__;

setup (
    name = 'gpostmaster-domains-datas',
    version = __version__,
    description = 'Downloads and flattends datas from Google Postmaster Tools (GPT)',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Mindbaz/python-gpostmaster-domains-datas',
    author = 'Valentin Henon',
    author_email = 'vhenon@mindbaz.com',
    python_requires = '>=3.6',
    keywords = 'google postmaster tools',
    license = 'GPLv3',
    packages = [
        'googlepostmasterapi',
        'entry_points_googlepostmasterapi'
    ],
    install_requires = [
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
    ],
    tests_require = [
        'nose',
        'coverage'
    ],
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'gpt_dl_all_datas = entry_points_googlepostmasterapi.gpt_dl_all_datas:run',
            'gpt_dl_domain_datas = entry_points_googlepostmasterapi.gpt_dl_domain_datas:run'
        ]
    },
    zip_safe = False,
    classifiers = [
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
);

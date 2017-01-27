#!/bin/env/python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from glob import glob
from setuptools import find_packages
import sys

VER = sys.version_info.major, sys.version_info.minor

if VER < (3, 4):
    REQS = ['importlib', 'mako', 'pyserial', 'pyyaml', 'enum']	# 'enum' backport needed.
else:
    REQS = ['importlib', 'mako', 'pyserial', 'pyyaml']

setup(
    name = 'genicontrol',
    version = '0.1',
    description= "GENIBus library",
    author = 'Christoph Schueler',
    author_email = 'cpu12.gems@googlemail.com',
    url = 'https://github.com/christoph2/GENIBus-Arduino',
    packages = ['genicontrol', 'genicontrol/model', 'genicontrol/view', 'genicontrol/controller', 'genilib', 'genilib/utils'],
    entry_points = {
        'console_scripts': [
                'GeniControl = genicontrol.GeniControl:main',
        ],
    },
    install_requires = REQS,
    data_files = [
            ('genicontrol/config', glob('genicontrol/config/*.*')),
    ],
    test_suite="tests"
)

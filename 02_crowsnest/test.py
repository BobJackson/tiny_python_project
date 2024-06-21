#! /usr/bin/env python
"""
test for crownest.py
"""
import os
from subprocess import getstatusoutput

prg = './crowsnest.py'


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

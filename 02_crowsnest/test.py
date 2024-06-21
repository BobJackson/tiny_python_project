#! /usr/bin/env python
"""
test for crownest.py
"""
import os

prg = './crowsnest.py'


def test_exists():
    """exists"""

    assert os.path.isfile(prg)

#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
FileName:environent.py
DESC:
"""
import os
def run(**args):
    print "[*] In environment module."
    return str(os.environ)

#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: sa.py

import re
from collections import OrderedDict
from romanizer import Romanizer

data = OrderedDict()

r = Romanizer(data)

def preprocess(string):
    """
    Preprocess string to transform all diacritics and remove other special characters
    :param string:
    :return:
    """
    return string

def convert(string, sanitize=False):
    """
    Swap characters from script to roman and vice versa. Optionally sanitize string by using preprocess function.

    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))
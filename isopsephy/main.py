#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: main.py

import re
import pandas as pd
import search
from romanize import el

data = el.data

"""
Data mapping between roman and greek letters and isopsephy values
"""

# letters from α to θ (1 to 9)
data[1] = data['alpha']
data[2] = data['beta']
data[3] = data['gamma']
data[4] = data['delta']
data[5] = data['epsilon']
data[6] = data['digamma']
data[7] = data['zeta']
data[8] = data['eta']
data[9] = data['theta']

# letters from ι to ϙ (10 to 90)
data[10] = data['iota']
data[20] = data['kappa']
data[30] = data['lambda']
data[40] = data['mu']
data[50] = data['nu']
data[60] = data['xi']
data[70] = data['omicron']
data[80] = data['pi']
data[90] = data['qoppa']

# letters from ρ to ϡ (100 to 900)
data[100] = data['rho']
data[200] = data['sigma']
data[300] = data['tau']
data[400] = data['upsilon']
data[500] = data['phi']
data[600] = data['chi']
data[700] = data['psi']
data[800] = data['omega']
data[900] = data['sampi']

greek_roman_values = {}

for num, d in data.items():
  for l in d['letter']:
    # greek small letter value
    greek_roman_values[l] = num
    # greek capital letter value
    greek_roman_values[l.upper()] = num
    # roman small letter value
    greek_roman_values[d['roman']] = num
    # roman capital letter value
    greek_roman_values[d['roman'].upper()] = num

regex_greek_roman_values = re.compile('|'.join(greek_roman_values.keys()))
regex_has_numbers = re.compile('\d')
isopsephy_error_msg = "String '%s' contains unsupported characters for isopsephy calculation"

class IsopsephyException(Exception):
    pass

def isopsephy(string):
    """
    String is a greek letter, word or sentence OR roman letter representation (transliteration) 
    of the greek letter, word or sentence that will be converted to the numerical value letter by letter
    Main function will convert input to unicode format for easier frontend, but on module logic
    more straightforward function unicode_isopsephy is used.
    """
    return unicode_isopsephy(unicode(string, encoding="utf-8"))

def unicode_isopsephy(string):
    """
    String argument must be in unicode format.
    """
    result = 0
    # don't accept strings that contain numbers
    if regex_has_numbers.search(string):
        raise IsopsephyException(isopsephy_error_msg % string)
    else:
        num_str = regex_greek_roman_values.sub(lambda x: '%s ' % greek_roman_values[x.group()],
                                               string)
        # don't accept strings, that contains letters which haven't been be converted to numbers
        try:
            result = sum([int(i) for i in num_str.split()])
        except Exception as e:
            raise IsopsephyException(isopsephy_error_msg % string)
    return result

def to_roman(word):
    return el.convert(word)

def to_greek(word):
    return el.convert(word)

def preprocess_roman(string):
    return el.preprocess(string)

def preprocess_greek(string):
    return el.preprocess(string)

def find(text, num, cumulative = False):
    words = text.split()
    numbers = list(map(isopsephy, words))
    if cumulative:
        result = []
        for incides in search.find_cumulative_indices(numbers, num):
            result.append(' '.join([words[idx] for idx in incides]))
        return result
    else:
        return [words[idx] for idx in map(numbers.index, numbers) if numbers[idx] == num]

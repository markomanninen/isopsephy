#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: romanizer.py

import re

class Romanizer(object):

    def __init__(self, data, add_uppercase = True):
        self.substitutes = {}
        for key, d in data.items():
            # add roman letter substituting greek letters
            for x in d['letter']:
                self.substitutes[x] = d['roman']
                if add_uppercase:
                    self.substitutes[x.upper()] = d['roman'].upper()
            # add the primary greek letter substituting roman letter
            self.substitutes[d['roman']] = d['letter'][0]
            if add_uppercase:
                self.substitutes[d['roman'].upper()] = d['letter'][0].upper()

        if len(self.substitutes):
            self.regex = re.compile('|'.join(self.substitutes.keys()))

    def preprocess(self):
        pass

    def convert(self, string, preprocess = None):
        """
        Swap characters from script to roman and vice versa. Optionally sanitize string by using preprocess function.

        :param preprocess:
        :param string:
        :return:
        """
        string = unicode(preprocess(string) if preprocess else string, encoding="utf-8")
        if self.regex:
            return self.regex.sub(lambda x: self.substitutes[x.group()], string).encode('utf-8')
        else:
            return string
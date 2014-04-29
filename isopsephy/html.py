#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: html.py

from tagpy import helper as h, table
from math import digital_root, digital_sum
from main import to_roman, to_greek, isopsephy

def char_table(text, modulo = 9, capitalize = None):
    # handle capitalization
    if capitalize == True:
        text = to_roman(text).upper()
    elif capitalize == False:
        text = to_roman(text).lower()
    else:
        text = to_roman(text)
    # initialize html table
    tbl = table(Class="char-table")
    # add caption / table title
    tbl.addCaption(to_greek(text))
    # add data rows
    tr1 = h.tr() # greek letters
    tr2 = h.tr() # roman letters
    tr3 = h.tr() # isopsephy number
    tr4 = h.tr() # summary
    i = 0
    for word in text.split():
        if i > 0:
            # add empty cells for word separation
            tr1 << h.th("&nbsp;")+h.th("&nbsp;")
            tr2 << h.td()+h.td(Class="empty-cell")
            tr3 << h.td()+h.td(Class="empty-cell")
            tr4 << h.td()+h.td()
        num = isopsephy(word)
        tr4 << h.td("%s %s" % (num, h.sub(digital_root(num))), colspan=len(word))
        i = i+1
        # add each letter on own cell
        for letter in word:
            tr1 << h.th(letter)
            tr2 << h.td(to_greek(letter))
            tr3 << h.td(isopsephy(letter))
    # add rows to table
    tbl.addHeadRow(tr1)
    tbl.addBodyRow(tr2)
    tbl.addBodyRow(tr3)
    tbl.addFootRow(tr4)
    # add summary footer for table
    num = isopsephy(text)
    tbl.addFootRow(h.tr(h.td("%s %s" % (num, h.sub(digital_sum(num), " / ", digital_root(num, modulo))), 
                             colspan=len(text)+len(text.split()), 
                             style="border-top: solid 1px #ddd")))
    return tbl
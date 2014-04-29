#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: math.py

def digital_root(num, modulo = 9):
    """ similar to modulo, but 0 and 9 are taken as 9 """
    val = num % modulo
    return val if val > 0 else modulo

def digital_sum(num):
    return sum(prepare_digital_operation(num))

def digital_product(num):
    return reduce(lambda x, y: x * y, prepare_digital_operation(num), 1)

def prepare_digital_operation(num):
    """ strip off 0|,|. and return a list of single digit integers from original number """
    return map(int, str(num).replace('0', '').replace('.', '').replace(',', ''))

def digital_root_summary(df):
    df2 = df.groupby('word').sum()
    df2['digital_root'] = df2['digital_sum'].apply(digital_root)
    df2['digital_product'] = df2['isopsephy'].apply(digital_product)
    df2['digital_product_root'] = df2['digital_product'].apply(digital_root)
    return df2
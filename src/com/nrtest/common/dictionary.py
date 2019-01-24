# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: dictionary.py
@time: 2018/9/12 0012 8:56
@desc:
"""


class Dict(dict):
    def __missing__(self, key):
        print('该KEY值“{}”不存在！！'.format(key))
        return ''


if __name__ == '__main__':
    a = {'a': 1, 'b': 2}
    b = Dict(a)
    print(a['a'])
    print(b['c'])

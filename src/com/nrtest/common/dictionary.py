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
        print('该KEY值“{}”不存在，原因：元素没配置或元素名错误！！'.format(key))
        # raise RuntimeError('该KEY值“{}”不存在！！'.format(key))
        # 找不到KEY值是未配置元素，或元素名错误，与Page.ignore_op函数配套用
        return 'IGNORE_VAL'

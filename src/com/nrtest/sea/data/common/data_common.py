# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: data_common.py
@time: 2018/7/17 0017 16:27
@desc:
"""


class DataCommon(object):
    sql_commom = 'select t.value_one,t.value_two,t.value_three,t.value_four from TEST_CASE t where t.case_name =:pa'

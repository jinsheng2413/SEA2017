# -*- coding:utf-8 -*-

'''
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: data_loadrankanalyse.py
@time: 2018/8/21 15:08
@desc:
'''
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.common.data_common import DataCommon
class pg:
    #加载
    pa = {'pa': 'test_rank_num_two'}
    p = Oracle()
    lis = p.queryAll(DataCommon.sql_commom, pa)
    print(lis)
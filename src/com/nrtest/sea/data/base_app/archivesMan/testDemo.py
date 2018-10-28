# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: testDemo.py
@time: 2018/9/10 0010 14:25
@desc:
"""
from com.nrtest.common.data_access import DataAccess


class TestDemoData:
    op = DataAccess()
    #
    ps = op.getCaseData('guochunbiao', '99922120')

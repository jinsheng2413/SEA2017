# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_whiteListQuery.py
@time: 2018/10/19 14:47
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.whiteListQuery_page import WhiteListQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→白名单查询
@ddt
class TestWhiteListQuery(unittest.TestCase, WhiteListQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.WhiteListQuery_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.refreshPage(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 开始日期
        self.inputStr_start_date(para['START_DATE'])
        # 结束日期
        self.inputStr_end_date(para['END_DATE'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.WhiteListQuery_para))
    def test_der(self, para):
        self.query(para)

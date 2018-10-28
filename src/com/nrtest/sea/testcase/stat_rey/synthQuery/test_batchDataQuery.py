# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_batchDataQuery.py
@time: 2018/9/30 10:21
@desc:
'''

import unittest

import ddt

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.batchDataQuery_page import BatchDataQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→批量数据查询
@ddt.ddt
class TestBatchDataQuery(unittest.TestCase, BatchDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.BatchDataQuery_para)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 日期
        self.inputDt_date(para['DATA'])
        # 终端资产号
        self.inputStr_tmnl_asset_no(para['TMNL_ASSET_NO'])
        # 用户类型
        self.inputCSel_cons_type(para['CONS_TYPE'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 查询按钮
        self.btn_search()

    @ddt.data(*DataAccess.getCaseData(SynthQuery_data.BatchDataQuery_para))
    def test_der(self, para):
        self.query(para)

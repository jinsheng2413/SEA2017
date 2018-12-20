# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_userCollectStatistics.py
@time: 2018/10/24 14:19
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.collConstructStatus.collConstructStatus_data import CollConstructStatus_data
from com.nrtest.sea.pages.stat_rey.collConstructStatus.userCollectStatistics_page import UserCollectStatisticsPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计
@ddt
class TestUserCollectStatistics(unittest.TestCase, UserCollectStatisticsPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(CollConstructStatus_data.UserCollectStatistics_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

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
        # # 回收左边树
        # self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 用户类型（下拉选择）
        self.inputCSel_cons_type(para['CONS_TYPE'])
        # 统计月份
        self.inputDt_date(para['DATE'])
        # 统计口径
        self.inputSel_statistics_caliber(para['STATISTICS_CALIBER'])
        # 查询按钮
        self.btn_search()
        # #校验
        # result = self.assert_context(*UserCollectStatisticsLocators.CHECK_FIRST)
        # self.assertTrue(result)


    @data(*(DataAccess.getCaseData(CollConstructStatus_data.UserCollectStatistics_para)))
    def test_der(self, para):
        """
        下拉复选框选择
        :param para:
        :return:
        """
        print(para)
        self.query(para)

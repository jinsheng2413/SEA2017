# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_idCheckInfQuery.py
@time: 2018/11/15 11:39
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.securityMan.securityMan_data import SecutityMan_date
from com.nrtest.sea.pages.sys_mam.securityMan.idCheckInfQuery_page import *
from com.nrtest.sea.task.commonMath import *


# 系统管理→权限密码管理→账号审核信息查询
@ddt
class TestIdCheckInfQuery(unittest.TestCase, IdCheckInfQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            SecutityMan_date.IdCheckInfQuery_para, True)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新菜单页面
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
        # 回收左边树
        # self.recoverLeftTree()

    def query(self, para):
        sleep(2)
        # 审核开始日期
        self.inputDt_start_date(para['START_DATE'])
        # 审核结束日期
        self.inputDt_end_date(para['END_DATE'])
        # 审核结果
        self.inputSel_result(para['RESULT'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*IdCheckInfQueryLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(SecutityMan_date.IdCheckInfQuery_para))
    def test_der(self, para):
        self.query(para)

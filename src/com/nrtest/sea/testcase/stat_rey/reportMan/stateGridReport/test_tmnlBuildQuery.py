# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: test_tmnlBuildQuery.py
@time: 2018/11/8 9:21
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.reportMan.stateGridReport.tmnlBuildQuery_data import TmnlBuildQuery_data
from com.nrtest.sea.pages.stat_rey.reportMan.stateGridReport.tmnlBuildQuery_page import TmnlBuildQueryPage, \
    TmnlBuildQueryLocators
from com.nrtest.sea.task.commonMath import *


# 统计查询--》报表管理--》国网报表--》智能电能表及终端设备建设情况
@ddt
class TestTmnlBuildQuery(unittest.TestCase, TmnlBuildQueryPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        cls.driver = openMenu(TmnlBuildQuery_data.TmnlBuildQuery_para, True)
        sleep(2)
        cls.exec_script(cls, TmnlBuildQueryLocators.START_DATE_JS)
        cls.exec_script(cls, TmnlBuildQueryLocators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 关闭菜单页面
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
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        sleep(2)
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])

        # 查询日期
        self.inputStr_dateS(para['DATE_S'])
        self.inputStr_dateE(para['DATE_E'])
        # 终端类型
        self.inputSel_tmnlType(para['TMNL_TYPE'])
        # 终端厂商
        self.inputSel_tmnlFac(para['TMNL_FAC'])
        # 统计口径
        self.inputSel_statWay(para['STAT_WAY'])

        self.btn_qry()
        self.sleep_time(2)

        # 校验
        # result = self.assert_context(*TmnlBuildQueryLocators.TAB_ONE)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TmnlBuildQuery_data.TmnlBuildQuery_para))
    def test_query(self, para):
        self.query(para)

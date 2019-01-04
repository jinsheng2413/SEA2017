# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_customMsgSend.py
@time: 2018/11/21 16:36
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.msgPush.msgPush_data import MsgPushData
from com.nrtest.sea.pages.sys_mam.msgPush.customMsgSend_page import CustomMsgSendPage
from com.nrtest.sea.task.commonMath import *


# 系统管理→信息定制→推送信息定制→手机订阅→自定义短信发送
@ddt
class TestCustomMsgSend(unittest.TestCase, CustomMsgSendPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）f
        menuPage = MenuPage.openMenu(MsgPushData.CustomMsgSend_para)
        super(unittest.TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(SysConfigManData.SysAbnormalParaSet_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        # self.recoverLeftTree()

    def query(self, para):
        # 单位名称
        self.inputStr_org_name(para['ORG_NAME'])
        # 联系人
        self.inputStr_linkman(para['LINKMAN'])
        # 手机号码
        self.inputStr_phone_no(para['PHONE_NO'])
        # 查询按钮
        self.btn_search()

    # @BeautifulReport.add_test_img()
    # @data(
    #     *DataAccess.getCaseData(MsgPushData.CustomMsgSend_para))
    # def test_der(self, para):
    #     self.query(para)
    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(self.check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MsgPushData.CustomMsgSend_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MsgPushData.CustomMsgSend_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)

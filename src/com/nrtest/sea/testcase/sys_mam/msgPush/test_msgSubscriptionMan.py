# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_msgSubscriptionMan.py
@time: 2018/11/21 16:05
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.msgPush.msgPush_data import MsgPushData
from com.nrtest.sea.pages.sys_mam.msgPush.msgSubscriptionMan_page import MsgSubscriptionManPage, \
    MsgSubscriptionManLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→信息定制→推送信息定制→手机订阅→短信订阅管理
@ddt
class TestMsgSubscriptionMan(unittest.TestCase, MsgSubscriptionManPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            MsgPushData.MsgSubscriptionMan_para, True)

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
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 订阅类型
        self.inputSel_sub_type(para['SUB_TYPE'])
        # 发送范围
        self.inputSel_send_scope(para['SEND_SCOPE'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*MsgSubscriptionManLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(MsgPushData.MsgSubscriptionMan_para))
    def test_der(self, para):
        self.query(para)

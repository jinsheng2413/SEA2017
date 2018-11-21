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
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            MsgPushData.CustomMsgSend_para, True)

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
        # 单位名称
        self.inputStr_org_name(para['ORG_NAME'])
        # 联系人
        self.inputStr_linkman(para['LINKMAN'])
        # 手机号码
        self.inputStr_phone_no(para['PHONE_NO'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(MsgPushData.CustomMsgSend_para))
    def test_der(self, para):
        self.query(para)

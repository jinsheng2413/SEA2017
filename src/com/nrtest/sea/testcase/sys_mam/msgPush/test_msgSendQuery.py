# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_msgSendQuery.py
@time: 2018/11/22 14:06
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.msgPush.msgPush_data import MsgPushData
from com.nrtest.sea.pages.sys_mam.msgPush.msgSendQuery_page import MsgSendQueryPage
from com.nrtest.sea.task.commonMath import *


# 系统管理→信息定制→推送信息定制→手机订阅→短信发送查询
@ddt
class TestMsgSendQuery(unittest.TestCase, MsgSendQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(MsgPushData.MsgSendQuery_para)

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
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 开始时间
        self.inputDt_start_date(para['START_END'])
        # 结束时间
        self.inputDt_end_date(para['END_DATE'])
        # 发送状态
        self.inputSel_send_stat(para['SEND_STAT'])
        # 发送方式
        self.inputSel_send_way(para['SEND_WAY'])
        # 发送人
        self.inputStr_send_man(para['SEND_MAN'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(MsgPushData.MsgSendQuery_para))
    def test_der(self, para):
        self.query(para)

# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.TerminalPassword_page import TerminalPasswordPage, \
    TerminalPasswordLocators
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端管理→终端在线监视

@ddt
class TesterminalPassword(unittest.TestCase, TerminalPasswordPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(DataGatherMan_data.terminalPassword_para)
        sleep(2)
        cls.exec_script(cls, TerminalPasswordLocators.JS)

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
        # self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 输入日期
        self.inputStr_date(para['DATE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @data(*DataAccess.getCaseData(DataGatherMan_data.terminalPassword_para))
    def test_query(self, para):
        self.query(para)

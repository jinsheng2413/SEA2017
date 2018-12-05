# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
'''
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.terminalOnlineSpied_page import TerminalOnlineSpiedLocators, \
    TerminalOnlineSpiedPage
from com.nrtest.sea.task.commonMath import *


@ddt
class TestTerminalOnlineSpied(unittest.TestCase, TerminalOnlineSpiedPage):

    @classmethod
    def setUpClass(cls):

        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(DataGatherMan_data.terminalOnlineSpied_para)
        sleep(2)
        cls.exec_script(cls, TerminalOnlineSpiedLocators.TMNL_MANUFACTURER_JS)
        cls.exec_script(cls, TerminalOnlineSpiedLocators.TMNL_PROTOCOL_JS)
        cls.exec_script(cls, TerminalOnlineSpiedLocators.TMNL_STATE_JS)
        cls.exec_script(cls, TerminalOnlineSpiedLocators.TMNL_TYPE_JS)

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
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        sleep(2)
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 终端厂商
        self.inputStr_TmnlManufactory(para['TMNL_MANUFACTORY'])
        print(para['TMNL_ADDR'])
        # 终端地址
        self.inputSel_TmnlAddr(para['TMNL_ADDR'])
        # 终端状态
        self.inputStr_TmnlState(para['TMNL_STATE'])
        # 终端规约
        self.inputStr_TmnlProtocol(para["TMNL_PROTOCOL"])
        # 终端类型
        self.inputStr_TmnlType(para['TMNL_TYPE'])

        self.btn_qry()

        self.sleep_time(2)
        # 校验

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(DataGatherMan_data.terminalOnlineSpied_para))
    def test_query(self, para):
        self.query(para)
        self.assert_query_result(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.terminalOnlineSpied_para, valCheck=True))
    def _test_checkValue(self, para):
        self.query(para)
        self.assert_query_criteria(para)

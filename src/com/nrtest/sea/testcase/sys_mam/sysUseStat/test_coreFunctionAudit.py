# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_coreFunctionAudit.py
@time: 2018/11/21 0021 9:56
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysUseStat.sysUseStat_data import SysUseStat_date
from com.nrtest.sea.pages.sys_mam.sysUseStat.coreFunctionAudit_page import CoreFunctionAuditPage, \
    CoreFunctionAuditLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→系统使用情况统计→系统使用情况统计
@ddt
class TestCoreFunctionAudit(unittest.TestCase, CoreFunctionAuditPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SysUseStat_date.coreFunctionAudit_para)
        sleep(2)
        cls.exec_script(cls, CoreFunctionAuditLocators.START_DATE_JS)
        cls.exec_script(cls, CoreFunctionAuditLocators.END_DATE_JS)

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
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        self.DisplayTreeMenu()
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 操作员
        self.inputStr_performer(para['PERFORMER'])
        # 拜访时间
        self.inputStr_visitTime(para['VISIT_TIME'])
        # 到
        self.inputStr_TO(para['TO'])

        self.btn_qry()
        sleep(1)
        self.clickCancel()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CoreFunctionAuditLocators.BTN_QRY)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SysUseStat_date.coreFunctionAudit_para))
    def test_query(self, para):
        self.query(para)

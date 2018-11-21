# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_AccountsAudit.py
@time: 2018/11/21 0021 10:35
@desc:
"""
from com.nrtest.sea.data.sys_mam.sysUseStat.sysUseStat_data import SysUseStat_date
from com.nrtest.sea.pages.sys_mam.sysUseStat.accountsAudit_page import AccountsAuditPage,AccountsAuditLocators
from com.nrtest.sea.task.commonMath import *
from com.nrtest.common.data_access import DataAccess
from ddt import ddt, data
from time import sleep
from com.nrtest.common.BeautifulReport import BeautifulReport
import unittest


# 系统管理→系统使用情况统计→账号审计
@ddt
class TestAccountsAudit(unittest.TestCase,AccountsAuditPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SysUseStat_date.accountsAudit_para)


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
        self.clickCheckBox(para['TAB_NAME'])
        if para['TAB_NAME'] =='日':
         sleep(2)
         self.exec_script(AccountsAuditLocators.START_DATE_JS)
        else:
          sleep(2)
          self.exec_script(AccountsAuditLocators.START_DATE_I_JS)
        #时间
        self.inputStr_date(para['DATE'])
        #账号状态
        self.inputStr_accountStatus(para['ACCOUNT_STATUS'])


        self.btn_qry()
        self.sleep_time(2)
        self.clickCancel()
        # 校验
        # result = self.assert_context(*AccountsAuditLocators.)
        # self.assertTrue(result)

    #@BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SysUseStat_date.accountsAudit_para))
    def test_query(self, para):
        self.query(para)




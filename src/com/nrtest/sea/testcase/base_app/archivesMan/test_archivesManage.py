# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesManage.py
@time: 2018/8/29 0029 14:26
@desc:
'''
import unittest

from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.base_app.archivesMan.archivesManage_para import ArchivesManage_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.pages.base_app.archivesMan.archivesManage_pages import ArchivesManage_pages
from com.nrtest.sea.task.archivesManage import *


class test_archivesManage(unittest.TestCase, ArchivesManage_pages):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = archivesMange()
        cls.orl = Oracle()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.driver.quit()

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

        # self.sleep_time(2000)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.clear_values(ArchivesManage_pages)

    # 用户类型
    def test_am_user_cata(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesManage_para.para_test_am_user_cata)
        self.inputSel_user_cata(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesManage_locators.TAB_ONE)
        self.assertTrue(result)

    # 户号
    def test_am_family_no(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesManage_para.para_test_am_family_no)
        self.inputStr_family_no(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesManage_locators.TAB_ONE)
        self.assertTrue(result)

    # 终端资产号
    def test_am_terminal_asset_no(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesManage_para.para_test_am_terminal_asset_no)
        self.inputStr_terminal_asset(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesManage_locators.TAB_ONE)
        self.assertTrue(result)

    # 终端地址
    def test_am_termianl_addr(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesManage_para.para_test_am_termianl_addr)
        self.inputStr_terminal_addr(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesManage_locators.TAB_ONE)
        self.assertTrue(result)

    # 用户编号明细
    def test_am_family_no_detail(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesManage_para.para_test_am_family_no)
        self.inputStr_family_no(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        self.btn_user_no_detail()

        # 校验
        result = self.assert_context(*ArchivesManage_locators.TAB_USER_ASSERT)
        self.assertTrue(result)
        self.btn_menu()

    # 终端资产号明细
    def test_am_terminal_asset_no_detail(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesManage_para.para_test_am_terminal_asset_no)
        self.inputStr_terminal_asset(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        self.btn_terminal_asset_detail()
        # 校验
        result = self.assert_context(*ArchivesManage_locators.BTN_CONFIRM)
        self.assertTrue(result)
        self.btn_confirm()
        self.btn_menu()

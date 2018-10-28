# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesAnalysisOfAnomaly_count.py
@time: 2018/8/30 0030 9:11
@desc:
"""
import unittest

from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.base_app.archivesMan.archivesAnalysisOfAnomaly_para import ArchivesAnalysisOfAnomaly_para
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.pages.base_app.archivesMan.archivesAnalysisOfAnomaly_pages import *
from com.nrtest.sea.task.archivesManage import *


class test_archivesAnalysisOfAnomaly_detail(unittest.TestCase, ArchivesAnalysisOfAnomaly_detail_pages):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = archivesAnalysisOfAnomaly_detail()
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
        self.clear_values(ArchivesAnalysisOfAnomaly_detail_pages)

    # 用户类型
    def test_aaoad_user_cata(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesAnalysisOfAnomaly_para.para_test_aaoa_user_cata)
        self.inputStr_date(lip[0][1])
        print(lip[0][1])
        self.inputSel_user_cata(lip[0][0])
        print(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesAnalysisOfAnomaly_count_locators.TAB_ONE)
        self.assertTrue(result)

        # 档案类型

    def test_aaoad_archives_cata(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesAnalysisOfAnomaly_para.para_test_aaoa_user_cata)
        self.inputStr_date(lip[0][1])
        self.inputSel_user_cata(lip[0][0])
        self.inputRSel_archives_cata(lip[0][2])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesAnalysisOfAnomaly_count_locators.TAB_ONE)
        self.assertTrue(result)

    # 时间查询
    def test_aaoad_date(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesAnalysisOfAnomaly_para.para_test_aaoa_date)
        self.inputStr_date(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesAnalysisOfAnomaly_count_locators.TAB_ONE)
        self.assertTrue(result)

    # 用户编号明细
    def test_aaoad_user_no_detail(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesAnalysisOfAnomaly_para.para_test_aaoa_date)
        self.inputStr_date(lip[0][0])
        self.btn_qry()
        self.btn_user_no_detail()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesAnalysisOfAnomaly_detail_locators.BTN_USER_DATA_QRY)
        self.assertTrue(result)
        self.btn_menu_anchives_al()

        # 终端档案异常数

    def test_aaoad_terminal_anomals_detail(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesAnalysisOfAnomaly_para.para_test_aaoa_date)
        self.inputStr_date(lip[0][0])
        self.btn_qry()
        self.btn_terminal_asset_no_detail()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesAnalysisOfAnomaly_detail_locators.BTN_CONFIRM)
        self.assertTrue(result)
        self.btn_confirm()
        self.btn_menu_anchives_al()

    # 终端档案异常数
    def test_aaoad_anomals_detail(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesAnalysisOfAnomaly_para.para_test_aaoa_date)
        self.inputStr_date(lip[0][0])
        self.btn_qry()
        self.btnAnomalsDetail()

        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesAnalysisOfAnomaly_detail_locators.BTN_LOS)
        self.assertTrue(result)
        self.btn_los()
        self.btn_menu_anchives_al()

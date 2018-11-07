# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesMaintain_factory.py
@time: 2018/8/30 0030 15:30
@desc:
"""
import unittest

from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.base_app.archivesMan.archivesMaintain_para import ArchivesMaintain
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.pages.base_app.archivesMan.archivesMaintain_page import ArchivesMaintain_meter_pages
from com.nrtest.sea.task.archivesManage import *


class TestarchivesMaintain_meter(unittest.TestCase, ArchivesMaintain_meter_pages):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = archivesMaintain_meter()
        cls.orl = Oracle()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        self.clear_values(ArchivesMaintain_meter_pages)

    # 终端资产号
    def test_amm_terminal_asset_no(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesMaintain.para_test_amm_terminal_asset_no)
        self.inputStr_termainalAssetNo(lip[0][0])
        self.btn_meterQry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesMaintain_locators.TAB_ONE)
        self.assertTrue(result)

    # 终端地址
    def test_amm_terminal_addr(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesMaintain.para_test_amm_terminal_addr)
        self.inputStr_termainalAddr(lip[0][0])
        self.btn_meterQry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesMaintain_locators.TAB_ONE)
        self.assertTrue(result)

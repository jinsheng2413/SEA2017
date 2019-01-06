# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesMaintain_factory.py
@time: 2018/8/30 0030 15:30
@desc:
"""
from unittest import TestCase

from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.base_app.archivesMan.archivesMaintain_para import ArchivesMaintain
from com.nrtest.sea.data.common.data_common import DataCommon
from com.nrtest.sea.pages.base_app.archivesMan.archivesMaintain_page import ArchivesMaintain_factory_pages
from com.nrtest.sea.task.archivesManage import *


class TestarchivesMaintain_factory(TestCase, ArchivesMaintain_factory_pages):
    @classmethod
    def setUpClass(cls):
        cls.driver = archivesMaintain_factory()
        cls.orl = Oracle()

    @classmethod
    def tearDownClass(cls):
        # 关闭菜单
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

    # 电压等级
    def test_amf_eleGrade(self):
        lip = self.orl.queryAll(DataCommon.sql_commom,
                                ArchivesMaintain.para_test_amf_eleGrade)
        self.inputSel_eleGrade(lip[0][0])
        self.btn_factoryQry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(ArchivesMaintain_locators.TAB_ONE)
        self.assertTrue(result)

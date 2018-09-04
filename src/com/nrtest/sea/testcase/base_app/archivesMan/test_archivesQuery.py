# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesManage.py
@time: 2018/8/29 0029 14:26
@desc:
'''
from com.nrtest.sea.task.archivesManage import *
from com.nrtest.sea.pages.base_app.archivesMan.archivesQuery_pages import ArchivesQuery_pages
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.data.base_app.archivesMan.archivesQuery_para import ArchivesQuery_para
from com.nrtest.sea.data.common.data_common import DataCommon
import unittest
class test_archivesManage(unittest.TestCase,ArchivesQuery_pages):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = archivesQuery()
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
        self.clear_values(ArchivesQuery_pages)

    #用户类型
    def test_aq_user_cata(self):
        lip = self.orl.queryAll(DataCommon.sql_commom, ArchivesQuery_para.para_test_aq_user_cata)
        self.inputSel_user_cata(lip[0][0])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesManage_locators.TAB_ONE)
        self.assertTrue(result)



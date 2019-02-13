# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesManage.py
@time: 2018/8/29 0029 14:26
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_para import ArchivesManData
from com.nrtest.sea.pages.base_app.archivesMan.archivesQuery_pages import ArchivesQueryPages
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→档案管理→档案查询
@ddt
class TestArchivesQuery(TestCase, ArchivesQueryPages):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(ArchivesManData.para_archivesQuery)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(ArchivesManData.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        cls.closePages(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        pass

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并点击
        self.openLeftTree(para['TREE_NODE'])

        # 选择用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])

        # 输入抄表段号
        self.inputStr_mr_sect_no(para['MR_SECT_NO'])

        # 选择终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 查询
        self.btn_qry()
        self.sleep_time(2)

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesManData.para_archivesQuery))
    def test_query(self, para):
        """基本应用→档案管理→档案查询

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesManData.para_archivesQuery, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

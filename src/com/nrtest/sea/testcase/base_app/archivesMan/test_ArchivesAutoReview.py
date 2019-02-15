# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_ArchivesAutoReview.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_data import ArchivesMan_data
from com.nrtest.sea.pages.base_app.archivesMan.archivesAutoReview_page import ArchivesAutoReviewPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→档案管理→电表批量导出(冀北)
@ddt
class TestArchivesAutoRevie(TestCase, ArchivesAutoReviewPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(ArchivesMan_data.archivesAutoReview_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(ArchivesMan_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(ArchivesAutoReviewPage)
        # 回收左边树
        # self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 选择导入电表信息
        self.inputSel_leadinto_meter(para['LEADINTO_METER'])

        # 输入日期
        self.inputDt_stat_date(para['STAT_DATE'])

        # 查询
        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
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
    @data(*DataAccess.getCaseData(ArchivesMan_data.archivesAutoReview_para))
    def test_query(self, para):
        """基本应用→档案管理→电表批量导出(冀北)
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesMan_data.archivesAutoReview_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

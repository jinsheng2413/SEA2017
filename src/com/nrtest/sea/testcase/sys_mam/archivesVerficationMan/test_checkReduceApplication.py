# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_checkReduceApplication.py
@time: 2018/11/20 0020 10:20
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.archivesVerficationMan.archivesVerficationMan_data import ArchivesVerficationMan_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.sys_mam.archivesVerficationMan.checkReduceApplication_page import CheckReduceApplicationPage


# 系统管理--》档案核查管理--》考核减免申请
@ddt
class TestCheckReduceApplication(TestCase, CheckReduceApplicationPage):

    @classmethod
    def setUpClass(cls):        
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(ArchivesVerficationMan_data.checkReduceApplication_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(ArchivesVerficationMan_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 开始日期
        self.inputDt_start_time(para['START_TIME'])
        # 结束日期
        self.inputDt_end_time(para['END_TIME'])
        # 申请单号
        self.inputStr_applyNo(para['APPLY_NO'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context()
        # self.assertTrue(result)

    # @BeautifulReport.add_test_img()
    # @data(*DataAccess.getCaseData(ArchivesVerficationMan_data.checkReduceApplication_para))
    # def test_query(self, para):
    #     self.query(para)

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
    @data(*DataAccess.getCaseData(ArchivesVerficationMan_data.checkReduceApplication_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesVerficationMan_data.checkReduceApplication_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

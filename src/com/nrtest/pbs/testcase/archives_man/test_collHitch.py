# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: test_collHitch.py
@time: 2019/3/15 14:18
@desc:
"""

# 档案管理--采集点挂接

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.pbs.data.archives_man.ArchivesMan_data import ArchivesMan_data
from com.nrtest.pbs.page.archives_man.collHitch_page import CollHitchPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


@ddt
class test_CollHitch(TestCase, CollHitchPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(ArchivesMan_data.collHitch_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        cls.goto_frame(cls)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(CollOperMain_data.collSuccRate_tab)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.goto_home_page(cls)

        # 关闭菜单页面
        # cls.main_page(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        每个测试用例测试结束后的操作，在这里做相关清理工作
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
        # 查询对象
        self.openLeftTree(para['TREE_NODE'])

        # 输入框
        self.input_name(para['INPUT_NAME'])

        # 查询
        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        # self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        self.assertTrue(self.check_query_criteria(para))

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesMan_data.collHitch_para))
    def test_query(self, para):
        """ 数据查询→谣测值
 """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesMan_data.collHitch_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

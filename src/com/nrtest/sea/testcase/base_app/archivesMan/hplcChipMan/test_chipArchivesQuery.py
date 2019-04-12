# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: test_chip_archives_query.py
@time: 2019-04-11 17:14:26
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.hplcChipMan.hplcChipMan_data import HPLCChipMan_data
from com.nrtest.sea.pages.base_app.archivesMan.hplcChipMan.chipArchivesQuery_page import ChipArchivesQueryPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用→档案管理→HPLC芯片管理→芯片档案查询功能
@ddt
class TestChipArchivesQuery(TestCase, ChipArchivesQueryPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(HPLCChipMan_data.chipArchivesQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage()
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
        # 所属单位
        self.openLeftTree(para['TREE_NODE'])

        # 设备类型
        self.inputSel_equip_type(para['EQUIP_TYPE'])

        # 芯片ID号
        self.inputStr_chipid(para['CHIPID'])

        # 所属终端地址
        self.inputStr_terminal_addr(para['TERMINAL_ADDR'])

        # 规约
        self.inputSel_protocal_code(para['PROTOCAL_CODE'])

        # 查询
        self.btn_qry()

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
        self.assertTrue(self.check_query_criteria(para))

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(HPLCChipMan_data.chipArchivesQuery_para))
    def test_query(self, para):
        """基本应用→档案管理→HPLC芯片管理→芯片档案查询功能
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(HPLCChipMan_data.chipArchivesQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

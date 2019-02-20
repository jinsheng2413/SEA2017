# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_generalGroupSet.py
@time: 2018/11/12 15:18
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.groupMan.groupMan_data import GroupMan_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.groupMan.generalGroupSet_page import *


# 运行管理→群组管理→普通群组设置
@ddt
class TestGeneralGroupSet(TestCase, GeneralGroupSetPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(GroupMan_data.GeneralGroupSet_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(SysConfigManData.SysAbnormalParaSet_tabName)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        self.sleep_time(3)
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 群组操作处理
        self.inputChk_group_deal(para['GROUP_DEAL'])
        if self.get_para_value(para['GROUP_DEAL']) == '管理群组':
            # 名称  群组名称
            self.inputStr_group_name(para['GROUP_NAME'])
            # 类别  群组类别
            self.inputChk_group_type(para['GROUP_TYPE'])
            # 有效日期
            self.inputChk_valid_date(para['VALID_DATE'])

            # 是否勾选有效日期
            if bool(self.get_para_value(para['VALID_DATE'])):
                # 开始日期
                self.inputDt_start_date(para['START_DATE'])
                # 至
                self.inputDt_end_date(para['END_DATE'])
            # 查询按钮
            self.btn_search()
        else:
            self.openLeftTree(para['TREE_NODE'])

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
    @data(*DataAccess.getCaseData(GroupMan_data.GeneralGroupSet_para))
    def test_query(self, para):
        """运行管理→群组管理→普通群组设置

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GroupMan_data.GeneralGroupSet_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

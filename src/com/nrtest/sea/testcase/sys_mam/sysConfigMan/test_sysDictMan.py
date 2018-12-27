# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_sysDictMan.py
@time: 2018/9/13 11:23
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysConfigMan.sysConfigMan_data import SysConfigManData
from com.nrtest.sea.pages.sys_mam.sysConfigMan.sysDictMan_page import SysDictManPage
from com.nrtest.sea.task.commonMath import *


# 系统管理--》系统配置管理--》数据字典管理
@ddt
class TestSysDict(unittest.TestCase, SysDictManPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # cls.driver = openMenu(SysConfigManData.para_SysDictMan)
        # sleep(2)
        # cls.exec_script(cls, SysDictManLocators.START_DATE_JS)
        # cls.exec_script(cls, SysDictManLocators.END_DATE_JS)
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(SysConfigManData.para_SysDictMan)
        super(unittest.TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(SysConfigManData.SysAbnormalParaSet_tabName)
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
        # self.clear_values(SysDictManPage)
        # 回收左边树
        # self.recoverLeftTree()

    def query(self, para):
        """
        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 分类名称
        self.inputStr_catalog_name(para['CATALOG_NAME'])
        # 生效日期
        self.inputStr_start_date(para['START_DATE'])
        # 失效日期
        self.inputStr_end_date(para['END_DATE'])
        # 维护类型
        self.inputRSel_cons_type(para['EDIT_TYPE'])
        # 维护人员
        self.inputStr_editor(para['EDITOR'])
        # 数据来源
        self.inputRSel_data_source(para['DATA_SOURCE'])

        self.btn_query()

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
    @data(*DataAccess.getCaseData(SysConfigManData.para_SysDictMan))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SysConfigManData.para_SysDictMan, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)

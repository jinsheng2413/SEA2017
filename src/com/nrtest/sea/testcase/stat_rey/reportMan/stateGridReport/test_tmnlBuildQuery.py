# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: test_tmnlBuildQuery.py
@time: 2018/11/8 9:21
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.reportMan.stateGridReport.tmnlBuildQuery_data import TmnlBuildQuery_data
from com.nrtest.sea.pages.stat_rey.reportMan.stateGridReport.tmnlBuildQuery_page import TmnlBuildQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询--》报表管理--》国网报表--》智能电能表及终端设备建设情况
@ddt
class TestTmnlBuildQuery(TestCase, TmnlBuildQueryPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        menuPage = MenuPage.openMenu(TmnlBuildQuery_data.TmnlBuildQuery_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
       #menuPage.clickTabPage(DataGatherMan_data.tmnlInstallDetail_tabOne)
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
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])

        # 统计分类
        self.inputChk_stat_type(para['STAT_TYPE'])

        # 日期
        self.inputStr_startDate(para['START_DATE'])

        # 到
        self.inputStr_endDate(para['END_DATE'])

        # 终端类型
        self.inputSel_tmnlType(para['TMNL_TYPE'])

        # 终端厂商
        self.inputSel_tmnlFac(para['TMNL_FAC'])

        # 统计口径
        self.inputSel_statWay(para['STAT_WAY'])

        self.btn_qry()
        self.sleep_time(2)

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
    @data(*DataAccess.getCaseData(TmnlBuildQuery_data.TmnlBuildQuery_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TmnlBuildQuery_data.TmnlBuildQuery_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

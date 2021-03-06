# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_runStatusMonitorDetail.py
@time: 2019-02-02 11:47:06
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.runStatusMonitor.runStatusMonitor_data import RunStatusMonitor_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.runStatusMonitor.runStatusMonitor_page import RunStatusMonitorDetailPage


# 运行管理→采集信道管理→运行情况监测:终端在线明细

@ddt
class TestRunStatusMonitorDetail(TestCase, RunStatusMonitorDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(RunStatusMonitor_data.runStatusMonitor_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(RunStatusMonitor_data.runStatusMonitor_detail)
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
        # 供电单位
        self.openLeftTree(para['TREE_NODE'])

        # 查询日期
        self.inputDt_query_date(para['QUERY_DATE'])

        # 实时
        self.inputChk_real_time(para['REAL_TIME'])

        # 采集方式
        self.inputSel_coll_mode(para['COLL_MODE'])

        # 终端状态
        self.inputSel_tmnl_status(para['TMNL_STATUS'])

        # 运营商
        self.inputSel_operator(para['OPERATOR'])

        # 当前状态
        self.inputSel_cur_status(para['CUR_STATUS'])

        # 终端逻辑地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])

        # 终端规约
        self.inputSel_tmnl_protocol(para['TMNL_PROTOCOL'])

        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])

        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])

        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])

        # 线路编号
        self.inputStr_line_no(para['LINE_NO'])

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
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RunStatusMonitor_data.runStatusMonitor_para,
                                  RunStatusMonitor_data.runStatusMonitor_detail))
    def test_query(self, para):
        """运行管理→采集信道管理→运行情况监测:终端在线明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RunStatusMonitor_data.runStatusMonitor_para,
                                  RunStatusMonitor_data.runStatusMonitor_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

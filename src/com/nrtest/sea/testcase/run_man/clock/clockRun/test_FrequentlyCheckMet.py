# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_Tmnl.py
@time: 2018/10/30 13:46
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.clock.clock_data import ClockData
from com.nrtest.sea.pages.run_man.clock.clockRun_page import FrequentlyCheckMetPage
from com.nrtest.sea.task.commonMath import *


# 运行管理→时钟管理→时钟运行质量分析
# 频繁对时终端
@ddt
class TestFrequentlyCheckMet(TestCase, FrequentlyCheckMetPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(ClockData.para_ClockRun)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(ClockData.para_ClockRun_checkmet)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭页面
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
        # 电能表厂商
        self.inputSel_met_fac(para['MET_FAC'])
        # 电表类别
        self.inputSel_met_type(para['MET_TYPE'])
        # 电能表资产号
        self.inputStr_met_asset_no(para['MET_ASSET_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 查询日期
        self.inputStr_query_date(para['QUERY_DATE'])

        self.btn_qry()
        self.sleep_time(2)

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(ClockData.para_ClockRun,
                                  ClockData.para_ClockRun_checkmet))
    def test_query(self, para):
        """
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ClockData.para_ClockRun,
                                  ClockData.para_ClockRun_checkmet, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)

    # def test_test(self):
    #     # 供电单位
    #     sleep(2)
    #     openLeftTree('13401')
    #     # 偏差范围
    #     self.inputRSel_offset_range('全部')
    #     # 终端类型
    #     self.inputRSel_tmnl_type('全部')
    #     # 终端型号
    #     self.inputStr_tmnl_model('')
    #     # 终端厂家
    #     self.inputRSel_tmnl_fac('宁波三星')
    #     # 终端地址
    #     self.inputStr_tmnl_addr('')
    #     # 是否在线
    #     self.inputRSel_is_online('全部')
    #     # 查询日期
    #     self.inputStr_query_date('2018-09')
    #     # 对时结果
    #     self.inputRSel_call_status('全部')
    #
    #     self.btn_query()
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(TmnlClockDetailLocators.TABLE_DATA)
    #     self.assertTrue(result)
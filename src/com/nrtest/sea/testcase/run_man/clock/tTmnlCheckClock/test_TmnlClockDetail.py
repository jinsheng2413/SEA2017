# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_TmnlClockDetail.py
@time: 2018/10/30 13:46
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.clock.clock_data import ClockData
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.clock.tTmnlCheckClock_page import TmnlClockDetailPage


# 运行管理→时钟管理→终端对时
# 终端时钟明细
@ddt
class TestTmnlClockDetail(TestCase, TmnlClockDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(ClockData.para_TTmnlCheckClock)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(ClockData.para_TTmnlCheckClock_detail)
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
        # 偏差范围
        self.inputSel_offset_range(para['OFFSET_RANGE'])
        # 终端类型
        self.inputSel_tmnl_type(para['TMNL_TYPE'])
        # 终端型号
        self.inputStr_tmnl_model(para['TMNL_MODEL'])
        # 终端厂家
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 是否历史
        # self.inputChk_is_history(para['IS_HISTORY'])
        # 是否在线
        self.inputSel_is_online(para['IS_ONLINE'])
        # 查询日期
        self.inputDt_query_date(para['QUERY_DATE'])
        # 对时结果
        self.inputSel_call_status(para['CALL_STATUS'])

        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(ClockData.para_TTmnlCheckClock,
                                  ClockData.para_TTmnlCheckClock_detail))
    def test_query(self, para):
        """运行管理→时钟管理→终端对时:终端时钟明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ClockData.para_TTmnlCheckClock,
                                  ClockData.para_TTmnlCheckClock_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

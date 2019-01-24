# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_TmnlInstallDetai_debug.py
@time: 2018/9/10 0010 9:21
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.tmnlInstallDetai_page import TmnlInstallDetaiPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用--终端管理--远程调试（第二个tab页）
@ddt
class TestTmnlInstallDetai_debug(TestCase, TmnlInstallDetaiPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(DataGatherMan_data.tmnlInstallDetail_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(DataGatherMan_data.tmnlInstallDetail_tabOne)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        # cls.closePages(cls)

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

        # 开始时间
        self.inputDt_startTime_count(para['START_TIME'])

        # 结束时间
        self.inputDt_endTime_Count(para['END_TIME'])

        # 运行状态
        self.inputSel_runState_count(para['RUN_STATE'])

        # 流程标识
        self.inputSel_processID_count(para['PROCESS_ID'])

        # 申请单号
        self.inputStr_app_no_count(para['APP_NO'])

        # 用户编号
        self.inputStr_cons_no_count(para['CONS_NO'])

        # 终端地址
        self.inputStr_tmnl_addr_count(para["TMNL_ADDR"])

        # 终端厂家
        self.inputSel_tmnl_factory_count(para['TMNL_FACTORY'])

        # 装接类型
        self.inputSel_moutingType_count(para['MOUNTING_TYPE'])

        # 终端类型
        self.inputSel_tmnlType_count(para['TMNL_TYPE'])

        # 通信规约
        self.inputSel_LCT_count(para['LCT'])

        # 表类型
        self.inputSel_surfaceType_count(para['SURFACE_TYPE'])

        self.btn_tmnl_qry()
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
    @data(*DataAccess.getCaseData(DataGatherMan_data.tmnlInstallDetail_para, DataGatherMan_data.tmnlInstallDetail_tabOne))
    def test_query(self, para):
        """基本应用--终端管理--远程调试（第二个tab页）
        :param para:用例数据
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.tmnlInstallDetail_para, DataGatherMan_data.tmnlInstallDetail_tabOne, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

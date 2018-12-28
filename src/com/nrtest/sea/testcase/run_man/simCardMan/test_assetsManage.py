# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_assetsManage.py
@time: 2018/11/8 0008 14:55
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.simCardMan.simCardMan_data import SimCardMan
from com.nrtest.sea.pages.run_man.simCardMan.assetsManage_page import AssetsManagePage
from com.nrtest.sea.task.commonMath import *


#运行管理-->SIM卡管理-->资产管理
@ddt
class TestAssetsManage(TestCase,AssetsManagePage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SimCardMan.assetsManage_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(ClockData.para_ClockResult_static)
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

        # 注册菜单
        self.menu_name = para['MENU_NAME']

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])
        #sim卡段
        self.inputStr_simCardNo(para['SIM_CARD_NO'])
        #至
        self.inputStr_simCardNoTO(para['SIM_CARD_NO_TO'])
        #sim卡状态
        self.inputSel_simCardStatus(para['SIM_CARD_STATUS'])
        #运营商
        self.inputSel_operator(para['OPERATOR'])
        #导入日期
        self.inputStr_leadTime(para['LEAD_TIME'])
        #所属系统
        self.inputSel_subordinateSystem(para['SUBORDINATE_SYSTEM'])
        #时间至
        self.inputStr_timeTO(para['TIME_TO'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*AssetsManageLocators.TAB_ONE)
        # self.assertTrue(result)

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
    @data(*DataAccess.getCaseData(SimCardMan.assetsManage_para))
    def test_query(self, para):
        """
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        :return:
        """
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SimCardMan.assetsManage_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)

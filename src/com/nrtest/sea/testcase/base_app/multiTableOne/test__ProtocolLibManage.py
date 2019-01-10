# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test__ProtocolLibManage.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.multiTableOne.multiTableOne import MultiTableOne
from com.nrtest.sea.pages.base_app.multiTableOne.protocolLibManage_page import ProtocolLibManageLocatorsPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 基本应用--》多表合一--》协议管理
@ddt
class TestProtocolLibManage(TestCase, ProtocolLibManageLocatorsPage):

    @classmethod
    def setUpClass(cls):

        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(MultiTableOne.protocolLibManage_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        # menuPage.clickTabPage(MultiTableOne.tmnlInstallDetail_tabOne)
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
        # 回收左边树
        # self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 协议名称
        self.inputStr_protocolName(para['PROTOCOL_NAME'])
        # 厂商名称
        self.inputStr_manufacturerName(para['MANUFACTURER_NAME'])
        # 协议类型
        self.inputStr_protocolType(para['PROTOCOL_TYPE'])
        # 表记类型
        self.inputStr_surfaceType(para['SURFACE_TYPE'])
        # 维护时间
        self.inputStr_maintenanceTmie(para['MANUFACTURER_TMIE'])
        # 结束时间
        self.inputStr_endTime(para['END_TIME'])
        # 有效标志
        self.inputSel_effectiveSign(para['EFFECTIVE_SIGN'])
        # 协议版本号
        self.inputStr_protocolVersionNo(para['PROTOCOL_VERSION_NO'])
        # 协议代码
        self.inputStr_protocolCode(para['PROTOCOL_CODE'])
        # 查询方式
        self.inputChk_queryType(para['QUERY_TYPE'])

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
    @data(*DataAccess.getCaseData(MultiTableOne.protocolLibManage_para))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MultiTableOne.protocolLibManage_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

# -*- coding: utf-8 -*-


"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_ModuleAttributeRelationshipMantain.py
@time: 2018/11/2 0002 13:38
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.runStatusMonitor.communicationModuleManagement.communicationModuleManagement import \
    CommunicationModuleManagement
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.runStatusMonitor.communicationModuleManagement.commModulPropMain_page import \
    ModuleAttributeRelationshipMantainPage


# 运行管理→采集信道管理→通信模块管理→通信模块属性维护：模块属性关系维护
@ddt
class TestModuleAttributeRelationshipMantain(TestCase, ModuleAttributeRelationshipMantainPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(CommunicationModuleManagement.commModulPropMain_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(CommunicationModuleManagement.commModulPropMain_tab_relationship)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

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
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])

        # 终端厂商
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])

        # 维护状态
        self.inputChk_mainten_status(para['MAINTEN_STATUS'])

        self.btn_qry()

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
    @data(*DataAccess.getCaseData(CommunicationModuleManagement.commModulPropMain_para,
                                  CommunicationModuleManagement.commModulPropMain_tab_relationship))
    def test_query(self, para):
        """运行管理→采集信道管理→通信模块管理→通信模块属性维护：模块属性关系维护
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CommunicationModuleManagement.commModulPropMain_para,
                                  CommunicationModuleManagement.commModulPropMain_tab_relationship, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_ModuleAttributeRelationshipMantain.py
@time: 2018/11/2 0002 13:38
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.runStatusMonitor.communicationModuleManagement.communicationModuleManagement import \
    CommunicationModuleManagement
from com.nrtest.sea.pages.run_man.runStatusMonitor.communicationModuleManagement.commModulPropMain_page import \
    ModuleAttributeRelationshipMantainPage, ModuleAttributeRelationshipMantainLocators
from com.nrtest.sea.task.commonMath import *


# 运行管理--》采集信道管理--》通信模块管理--》通信模块属性维护

@ddt
class TestModuleAttributeRelationshipMantain(unittest.TestCase, ModuleAttributeRelationshipMantainPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            CommunicationModuleManagement.commModulPropMain_para, True)
        clickTabPage(
            CommunicationModuleManagement.commModulPropMain_tab_relationship)
        cls.clickCheckBox(cls, CheckBoxName='已维护')
        sleep(2)
        cls.exec_script(
            cls, ModuleAttributeRelationshipMantainLocators.TMNL_FACTORY_JS)

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
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        sleep(2)
        # 打开左边树并选择

        self.driver = openLeftTree(para['ORG_NO'])

        # 终端地址
        self.inputStr_tmnlAddr(para['TMNL_ADDR'])
        # 终端厂商
        self.inputStr_tmnlFactory(para['TMNL_FACTORY'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(
            *ModuleAttributeRelationshipMantainLocators.TAB_ONE)
        self.assertTrue(result)

    # @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(CommunicationModuleManagement.commModulPropMain_para,
                                  CommunicationModuleManagement.commModulPropMain_tab_relationship))
    def test_query(self, para):
        self.query(para)

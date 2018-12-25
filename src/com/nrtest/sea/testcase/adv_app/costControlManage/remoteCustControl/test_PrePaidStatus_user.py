# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.costControlManage.remoteCustControl.remoteCustControl_data import \
    RemoteCustControl_data
from com.nrtest.sea.pages.adv_app.costControlManage.remoteCustControl.PrePaidStatus_page import \
    PrePaidStatusPage, PrePaidStatus_Locators
from com.nrtest.sea.task.commonMath import *


# 高级应用--》费控管理--》远程费控--》远程费控执行统计
@ddt
class TestPrePaidStatus(unittest.TestCase, PrePaidStatusPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(RemoteCustControl_data.prePaidStatus_para)

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
        self.recoverLeftTree()

    def userQuery(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        # 选择tab页
        # 注册菜单
        self.menu_name = para['MENU_NAME']
        clickTabPage(para['TAB_NAME'])
        sleep(2)
        self.exec_script(PrePaidStatus_Locators.START_DATE_TWO_JS)

        self.exec_script(PrePaidStatus_Locators.END_DATE_TWO_JS)

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 控制类型
        self.inputRSel_controlType_Two(para['CONTROL_TYPE'])
        # 开始时间
        self.inputStr_start_timeTwo(para['START_TIME'])
        # 结束时间
        self.inputStr_end_timeTwo(para['END_TIME'])

        self.btn_query(True)
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
    @data(*DataAccess.getCaseData(RemoteCustControl_data.prePaidStatus_para, RemoteCustControl_data.Tab_Two))
    def test_userQuery(self, para):
        self.userQuery(para)
        self.start_case(para)
        self.assert_query_result(para)
        self.end_case(para)
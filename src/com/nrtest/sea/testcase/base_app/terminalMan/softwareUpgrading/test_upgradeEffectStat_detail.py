# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_upgradeEffectStat_detail.py
@time: 2018/12/11 15:01
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.terminalMan.softwareUpgrading.softwareUpgrading_date import SoftwareUpgrading_data
from com.nrtest.sea.pages.base_app.terminalMan.softwareUpgrading.upgradeEffectStatistics_page import \
    UpgradeEffectStatisticsPage
from com.nrtest.sea.task.commonMath import *


# 基本应用→终端管理→软件升级→升级效果统计→终端升级明细
@ddt
class TestUpgradeEffectStst_detail(unittest.TestCase, UpgradeEffectStatisticsPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SoftwareUpgrading_data.UpgradeEffectStatistics_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.refreshPage(cls)

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
        # # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(UpgradeTaskExecutionPage)
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

        clickTabPage('终端升级明细')
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['TREE_NODE'])  # 'DETAIL_TREE_ORG_NO'])
        # 终端厂家
        self.inputSel_detail_tmnl_factory(para['DETAIL_TMNL_FACTORY'])
        # 升级目的
        self.inputSel_detail_upgrade_purpose(para['DETAIL_UPGRADE_PURPOSE'])
        # 升级类型
        self.inputSel_detail_upgrade_type(para['DETAIL_UPGRADE_TYPE'])
        # 终端用途
        self.inputSel_detail_tmnl_purpose(para['DETAIL_TMNL_PURPOSE'])
        # 是否成功
        self.inputSel_detail_whether_success(para['DETAIL_WHETHER_SUCCESS'])
        # 终端类型
        self.inputSel_detail_tmnl_type(para['DETAIL_TMNL_TYPE'])
        # 升级状态
        self.inputSel_detail_upgrade_ststus(para['DETAIL_UPGRADE_STATUS'])
        # 确认状态
        self.inputSel_detail_affirm_status(para['DETAIL_AFFIRM_STATUS'])
        # 确认结果
        self.inputSel_detail_affirm_result(para['DETAIL_AFFIRM_RESULT'])
        # 执行开始日期
        self.inputDt_detail_start_date(para['DETAIL_START_DATE'])
        # 执行结束日期
        self.inputDt_detail_end_date(para['DETAIL_END_DATE'])
        # 确认开始日期
        self.inputDt_affirm_start_date(para['AFFIRM_START_DATE'])
        # 确认结束日期
        self.inputDt_affirm_end_date(para['AFFIRM_END_DATE'])
        # 点击查询按钮
        self.btn_detail_search()

        # 校验

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
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEffectStatistics_para,
                                  SoftwareUpgrading_data.UpgradeEffectStatistics_tabName_detail))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SoftwareUpgrading_data.UpgradeEffectStatistics_para,
                                  SoftwareUpgrading_data.UpgradeEffectStatistics_tabName_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)

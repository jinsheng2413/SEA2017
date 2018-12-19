# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_tmnlSimFlowJB_tab2.py
@time: 2018-11-12 10:52
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.simCardMan.runSituationCount.tmnlSimFlowJB_data import RunSituationCount_data
from com.nrtest.sea.pages.run_man.simCardMan.runSituationCount.tmnlSimFlowJB_page import TmnlSimFlowJB_2Locators, \
    TmnlSimFlowJB_2Page
from com.nrtest.sea.task.commonMath import *


# 运行管理--SIM卡管理--运行情况分析--终端流量统计（冀北）（第一个tab页）
@ddt
class Test_TnmlSimFlowJB_2(unittest.TestCase, TmnlSimFlowJB_2Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(RunSituationCount_data.para_TmnlSimFlowJB)
        sleep(2)
        clickTabPage('月流量统计')
        cls.exec_script(cls, TmnlSimFlowJB_2Locators.DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(SysDictManPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        sleep(4)
        # 打开左边树选择供电单位
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # Sim卡号
        self.inputStr_sim_no(para['SIM_NO'])
        # 开始日期
        self.inputStr_date(para['DATE'])
        # 点击零流量
        self.click(*TmnlSimFlowJB_2Locators.QRY_ZERO_FLOW)

        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*TmnlSimFlowJB_2Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RunSituationCount_data.para_TmnlSimFlowJB,
                                  RunSituationCount_data.TmnlSimFlowJB_tab_count_month))
    def test_query(self, para):
        self.query(para)

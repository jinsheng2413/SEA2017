# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_simInstallStat.py
@time: 2018/11/9 0009 9:17
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.simCardMan.runSituationCount.runSituationCount_data import RunSituationCount_data
from com.nrtest.sea.pages.run_man.simCardMan.runSituationCount.simInstallStat_page import SimInstallStatPage, \
    SimInstallStatLocators
from com.nrtest.sea.task.commonMath import *


# 运行管理-->SIM卡管理-->运行情况分析-->安装情况统计
@ddt
class TestSimInstallStat(unittest.TestCase,SimInstallStatPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(RunSituationCount_data.simInstallStat_para)

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

        #打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        #运营商
        self.inputSel_operator(para['OPERATOR'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*SimInstallStatLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(RunSituationCount_data.simInstallStat_para))
    def test_query(self, para):
        self.query(para)




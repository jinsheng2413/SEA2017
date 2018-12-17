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

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.dataAnalyse.loadAanlyse.loadAanlyse_data import LoadAanyse_data
from com.nrtest.sea.pages.stat_rey.dataAnalyse.loadAanyse.LoadSortAnalyse_pages import LoadSortAnalysePage, \
    LoadSortAnalyseLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestDemo(unittest.TestCase, LoadSortAnalysePage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(LoadAanyse_data.loadSortAnalyse_para)
        sleep(2)
        cls.exec_script(cls, LoadSortAnalyseLocators.START_DATE_JS)
        cls.exec_script(cls, LoadSortAnalyseLocators.END_DATE_JS)

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

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 开始时间
        self.inputStr_startDate(para['START_DATE'])
        # 结束时间
        self.inputStr_end_time(para['END_TIME'])
        # 用户类型
        self.inputSel_userType(para['USER_TYPE'])
        # 排名数量
        self.inputStr_anking_number(para['RANKING_NUMBER'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @data(*DataAccess.getCaseData(LoadAanyse_data.loadSortAnalyse_para))
    def test_query(self, para):
        self.query(para)

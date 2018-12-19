# -*- coding:utf-8 -*-
"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: test_lpConRunQuery.py
@time: 2018/11/7 13:41
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.reportMan.stateGridReport.lpConRunQuery_data import IpConRunQuery_data
from com.nrtest.sea.pages.stat_rey.reportMan.stateGridReport.lpConRunQuery_page import IpConRunQueryPage, \
    IpConRunQueryLocators
from com.nrtest.sea.task.commonMath import *


# 统计查询--》报表管理--》国网报表--》低压用户运行指标
@ddt
class TestIpConRunQuery(unittest.TestCase, IpConRunQueryPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        cls.driver = openMenu(IpConRunQuery_data.IpConRunQuery_para)
        sleep(2)
        cls.exec_script(cls, IpConRunQueryLocators.START_DATE_JS)

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

        sleep(2)
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])

        # 查询月份
        self.inputStr_date(para['DATE'])
        # 统计口径
        self.inputSel_statWay(para['STAT_WAY'])

        self.btn_qry()
        self.sleep_time(2)

        # 校验
        #  result = self.assert_context(*IpConRunQueryLocators.TAB_ONE)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(IpConRunQuery_data.IpConRunQuery_para))
    def test_query(self, para):
        self.query(para)

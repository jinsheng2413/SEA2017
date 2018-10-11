# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_multipleTableDataQuery.py
@time: 2018/10/11 15:07
@desc:
'''

import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.pages.stat_rey.synthQuery.multipleTableDataQuery_page import MultipleTableDataQueryPage
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.task.commonMath import *
from ddt import ddt,data

# 统计查询→综合查询→多表合一抄表数据查询
@ddt
class TestMultipleTableDataQuery(unittest.TestCase,MultipleTableDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.MultipleTableDataQuery_para)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 用户编号
        self.inputStr_cons_cons_no(para['CONS_CONS_NO'])
        #开始时间
        self.inputDt_cons_start_date(para['CONS_START_DATE'])
        #结束时间
        self.inputDt_cons_end_date(para['CONS_END_DATE'])
        # 用户状态
        self.inputSel_cons_cons_status(para['CONS_CONS_STATUS'])
        #查询按钮
        self.btn_search()

    @data(*DataAccess.getCaseData(SynthQuery_data.MultipleTableDataQuery_para))
    def test_der(self, para):
        self.query(para)
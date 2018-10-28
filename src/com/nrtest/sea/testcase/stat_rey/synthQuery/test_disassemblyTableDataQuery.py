# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_disassemblyTableDataQuery.py
@time: 2018/10/9 14:21
@desc:
'''

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.locators.stat_rey.synthQuery.disassemblyTableDataQuery_locators import \
    DisassemblyTableDataQueryLocators
from com.nrtest.sea.pages.stat_rey.synthQuery.disassemblyTableDataQuery_page import DisassemblyTableDataQueryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→销户和拆表数据查询
@ddt
class TestDisassemblyTableDataQuery(unittest.TestCase, DisassemblyTableDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.DisassemblyTableDataQuery_para)

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
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 用户名称
        self.inputStr_user_name(para['USER_NAME'])
        # 用户编号
        self.inputStr_user_no(para['USER_NO'])
        # 用户类型
        self.inputSel_user_type(para['USER_TYPE'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 电能表资产号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 开始时间
        self.inputDt_start_date(para['START_DATE'])
        # 结束时间
        self.inputDt_end_date(para['END_DATE'])
        # 查询按钮
        self.btn_search()
        self.sleep_time(10)
        # 校验
        result = self.assert_context(*DisassemblyTableDataQueryLocators.CHECK_FIRST)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(SynthQuery_data.DisassemblyTableDataQuery_para))
    def test_der(self, para):
        self.query(para)

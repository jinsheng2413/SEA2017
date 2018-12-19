# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_recordsQuery_tab.py
@time: 2018/10/26 17:28
@desc:
'''
import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.intelligentLock.intelligentLock_data import IntelligentLock_data
from com.nrtest.sea.locators.adv_app.intelligentLock.recordsQuery_locators import RecordsQueryLocators
from com.nrtest.sea.pages.adv_app.intelligentLock.recordsQuery_page import RecordsQueryPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→智能锁具→记录查询→资产管理记录查询
@ddt
class TestRecordsQuery(unittest.TestCase, RecordsQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(IntelligentLock_data.RecordsQuery_para)

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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'TAB_TREE_ORG_NO'])
        # 操作员名称
        self.inputStr_tab_staff_name(para['TAB_STAFF_NAME'])
        # 电子钥匙编号
        self.inputStr_tab_key_no(para['TAB_KEY_NO'])
        # 锁封编号
        self.inputStr_tab_lock_no(para['TAB_LOCK_NO'])
        # 锁封用户编号
        self.inputStr_tab_lock_user_no(para['TAB_LOCK_USER_NO'])
        # 开始日期
        self.inputDt_tab_start_date(para['TAB_START_DATE'])
        # 结束日期
        self.inputDt_tab_end_date(para['TAB_END_DATE'])
        # 查询按钮
        self.tab_btn_search()
        # 校验
        result = self.assert_context(*RecordsQueryLocators.TAB_CHECK_FIRST)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(IntelligentLock_data.RecordsQuery_para))
    def test_der(self, para):
        clickTabPage('资产管理记录查询')
        self.query(para)

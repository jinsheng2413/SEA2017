# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_assetMan.py
@time: 2018/10/26 14:03
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.intelligentLock.intelligentLock_data import IntelligentLock_data
from com.nrtest.sea.pages.adv_app.intelligentLock.assetMan_page import AssetManPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 高级应用→智能锁具→资产管理:已增锁封列表
@ddt
class TestAssetMan(TestCase, AssetManPage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(IntelligentLock_data.AssetMan_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(IntelligentLock_data.AssetMan_tabName_lock)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        # menuPage.remove_dt_readonly()

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
        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])
        # 锁封编号
        self.inputStr_lock_no(para['LOCK_NO'])
        # 台区名称
        self.inputStr_tg_name(para['TG_NAME'])
        # 用户名称
        self.inputStr_user_name(para['CONS_NAME'])
        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 锁封资产状态
        self.inputSel_lock_asset_ststus(para['LOCK_ASSET_STATUS'])
        # 锁封状态
        self.inputSel_lock_status(para['LOCK_STATUS'])
        # 锁封类型
        self.inputSel_lock_type(para['LOCK_TYPE'])
        # 查询按钮
        self.btn_query()

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
    @data(*DataAccess.getCaseData(IntelligentLock_data.AssetMan_para, IntelligentLock_data.AssetMan_tabName_lock))
    def test_query(self, para):
        """高级应用→智能锁具→资产管理:已增锁封列表

        :param para:
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(IntelligentLock_data.AssetMan_para, IntelligentLock_data.AssetMan_tabName_lock))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

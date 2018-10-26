# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_assetMan.py
@time: 2018/10/26 14:03
@desc:
'''

import unittest
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.locators.adv_app.intelligentLock.assetMan_locators import AssetManLocators
from com.nrtest.sea.pages.adv_app.intelligentLock.assetMan_page import AssetManPage
from com.nrtest.sea.data.adv_app.intelligentLock.intelligentLock_data import IntelligentLock_data
from com.nrtest.sea.task.commonMath import *
from ddt import ddt,data

# 高级应用→智能锁具→资产管理
@ddt
class TestAssetMan(unittest.TestCase,AssetManPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(IntelligentLock_data.AssetMan_para,True)

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
        #打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        #锁封编号
        self.inputStr_lock_no(para['LOCK_NO'])
        #台区名称
        self.inputStr_tg_name(para['TG_NAME'])
        #用户名称
        self.inputStr_user_name(para['USER_NAME'])
        #用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        #锁封资产状态
        self.inputSel_lock_asset_ststus(para['LOCK_ASSET_STATUS'])
        #锁封状态
        self.inputSel_lock_status(para['LOCK_STATUS'])
        #锁封类型
        self.inputSel_lock_type(para['LOCK_TYPE'])
        #查询按钮
        self.btn_search()
        #校验
        result = self.assert_context(*AssetManLocators.CHECK_FIRST)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(IntelligentLock_data.AssetMan_para))
    def test_der(self, para):
        self.query(para)
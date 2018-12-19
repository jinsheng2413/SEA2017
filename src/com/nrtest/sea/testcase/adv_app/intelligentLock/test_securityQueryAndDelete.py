# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_securityQueryAndDelete.py
@time: 2018/10/29 9:26
@desc:
'''

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.intelligentLock.intelligentLock_data import IntelligentLock_data
from com.nrtest.sea.locators.adv_app.intelligentLock.securityQueryAndDelete_locators import \
    SecurityQueryAndDeleteLocators
from com.nrtest.sea.pages.adv_app.intelligentLock.securityQueryAndDelete_page import SecurityQueryAndDeletePage
from com.nrtest.sea.task.commonMath import *


# 高级应用→智能锁具→权限查询及删除
@ddt
class TestSecurityQueryAndDelete(unittest.TestCase, SecurityQueryAndDeletePage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(IntelligentLock_data.SecurityQueryAndDelete_para)

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
        openLeftTree(para['TREE_NODE'])  # 'TREE_ORG_NO'])
        # 电子钥匙编号
        self.inputStr_key_no(para['KEY_NO'])
        # 锁封编号
        self.inputStr_lock_no(para['LOCK_NO'])
        # 操作员编号
        self.inputStr_staff_no(para['STAFF_NO'])
        # 查询按钮
        self.btn_search()
        # 校验
        result = self.assert_context(
            *SecurityQueryAndDeleteLocators.CHECK_FIRST)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(IntelligentLock_data.SecurityQueryAndDelete_para))
    def test_der(self, para):
        self.query(para)

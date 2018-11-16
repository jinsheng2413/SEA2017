# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_sysAbnormalParaSet.py
@time: 2018/11/16 15:16
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysConfigMan.sysConfigMan_data import SysConfigManData
from com.nrtest.sea.pages.sys_mam.sysConfigMan.sysParameterMan_page import SysAbnormalParaSetPage, \
    SysAbnormalParaSetLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→系统配置管理→系统参数管理
# 系统管理→系统配置管理→系统参数管理→系统异常参数设置
@ddt
class TestSysBasicParaSet(unittest.TestCase, SysAbnormalParaSetPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            SysConfigManData.SysParameterMan_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        clickTabPage('系统异常参数设置')
        # 参数名称
        self.inputSel_para_name(para['PARA_NAME'])
        # 参数编码
        self.inputStr_para_no(para['PARA_NO'])
        # 参数项名称
        self.inputStr_para_item_name(para['PARA_ITEM_NAME'])
        # 参数项编码
        self.inputStr_para_item_no(para['PARA_ITEM_NO'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*SysAbnormalParaSetLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(SysConfigManData.SysParameterMan_para, SysConfigManData.SysAbnormalParaSet_tabName))
    def test_der(self, para):
        self.query(para)

# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_orgVoltageStationSet.py
@time: 2018/11/21 11:23
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.templateMan.templateMan_data import TemplateManData
from com.nrtest.sea.pages.sys_mam.templateMan.orgVoltageStationSet_page import OrgVoltageStationSetPage, \
    OrgVoltageStationSetLocators
from com.nrtest.sea.task.commonMath import *


# 系统管理→模板管理→供电电压测点设置
@ddt
class TestOrgVoltageStationSet(unittest.TestCase, OrgVoltageStationSetPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            TemplateManData.OrgVoltageStationSet_para, True)

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
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 电表资产
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 注册信息
        self.inputSel_login_infor(para['LOGIN_INFOR'])
        # 查询按钮
        self.btn_search()
        sleep(2)
        # 校验
        result = self.assert_context(*OrgVoltageStationSetLocators.CHECK_FIRST)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(TemplateManData.OrgVoltageStationSet_para))
    def test_der(self, para):
        self.query(para)

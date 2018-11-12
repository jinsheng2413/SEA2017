# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_unControlPlantDetail.py
@time: 2018/11/12 11:33
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_data import UnControlPlant
from com.nrtest.sea.pages.adv_app.vipConsMan.unControlPlant.unControlPlantStat_page import \
    UnControlPlantDetailPage
from com.nrtest.sea.task.commonMath import *


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计→非统调电厂接入明细
@ddt
class TestUnControlPlantDetail(unittest.TestCase, UnControlPlantDetailPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            UnControlPlant.UnControlPlantStat_para, True)

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
        clickTabPage('非统调电厂接入明细')
        # 打开左边树并选择
        self.driver = openLeftTree(para['TREE_ORG_NO'])
        # 发电方式
        self.inputSel_elec_way(para['ELEC_WAY'])
        # 采集方式
        self.inputSel_gather_way(para['GATHER_WAY'])
        # 统计日期
        self.inputDt_date(para['DATE'])
        # 户号
        self.inputStr_cons_no(para['CONS_NO'])
        # 表资产编号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])
        # 终端资产编号
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 查询按钮
        self.btn_search()

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(UnControlPlant.UnControlPlantStat_para, tabName='非统调电厂接入明细'))
    def test_der(self, para):
        self.query(para)

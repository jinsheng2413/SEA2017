# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_userDataQuery.py
@time: 2018/8/9 0002 11:21
"""
import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.pages.stat_rey.synthQuery.userDataQuery_page import UserDataQueryPage
from com.nrtest.sea.task.synthQuery import UserDataQueryLog


# 统计查询→综合查询→用户数据查询
class TestUserDataQuery(unittest.TestCase, UserDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = UserDataQueryLog()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        cls.driver.quit()

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        self.orl = Oracle()
        self.clear_values(UserDataQueryPage)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

    # 基本档案，用户编号查询
    @BeautifulReport.add_test_img()
    def test_a_usernum(self):
        ud = UserDataQueryPage(self.driver)
        # 点击左边树-国网冀北电力有限公司
        ud.inputNode_jibei()
        # 点击展开-唐山供电公司
        ud.inputNode_tangshan()
        # 点击展开-直属用户
        ud.inputNode_directlyuser()
        # 点击选择-电网-国各庄
        ud.inputNode_guogezhuang()
        # 点击查询按钮
        ud.btn_search()

    # 基本档案，用户编号查询
    @BeautifulReport.add_test_img()
    def test_b_usernum_two(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()

    # 数据展示，电能示值
    @BeautifulReport.add_test_img()
    def test_c_electricenergy(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击电能示值--查询

        # 点击基本档案
        ud.btn_basicfile()

    # 数据展示，电压曲线
    @BeautifulReport.add_test_img()
    def test_d_voltagecurve(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击电压曲线
        ud.btn_voltagecurve()
        # 点击电压曲线--查询

        # 点击基本档案
        ud.btn_basicfile()

    # 数据展示，电流曲线
    @BeautifulReport.add_test_img()
    def test_e_currentcurve(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击电流曲线
        ud.btn_currentcurve()
        # 点击电流曲线--查询

        # 点击基本档案
        ud.btn_basicfile()

    # 数据展示，功率曲线
    @BeautifulReport.add_test_img()
    def test_f_currentcurve(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击功率曲线
        ud.btn_powercurve()
        # 点击功率曲线--查询

        # 点击基本档案
        ud.btn_basicfile()

    # 数据展示，功率因数曲线
    @BeautifulReport.add_test_img()
    def test_g_currentcurve(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击功率因数曲线
        ud.btn_powerfactorcurve()
        # 点击功率因数曲线--查询

        # 点击基本档案
        ud.btn_basicfile()

    # 数据展示，电量
    @BeautifulReport.add_test_img()
    def test_h_currentcurve(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击电量
        ud.btn_electricquantity()
        # 点击电量--查询

        # 点击基本档案
        ud.btn_basicfile()

    # 数据展示，负荷
    @BeautifulReport.add_test_img()
    def test_i_currentcurve(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击负荷
        ud.btn_load()
        # 点击负荷--查询

        # 点击基本档案
        ud.btn_basicfile()

    # 数据展示，用电异常
    @BeautifulReport.add_test_img()
    def test_j_currentcurve(self):
        ud = UserDataQueryPage(self.driver)
        # 在用户编号输入框输入“T1102676767”
        ud.inputStr_usernum('T1102676767')
        # 点击查询按钮
        ud.btn_search()
        # 点击数据展示
        ud.btn_datashow()
        # 点击用电异常
        ud.btn_abnormalelectricity()
        # 点击用电异常--查询

        # 点击基本档案
        ud.btn_basicfile()

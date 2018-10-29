# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_publicDataQueryPage.py
@time: 2018/8/16 0002 10:20
"""

import unittest

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.oracle_test import Oracle
from com.nrtest.sea.pages.stat_rey.synthQuery.publicDataQuery_page import PublicDataQueryPage
from com.nrtest.sea.task.synthQuery import PublicDataQueryLog


# 统计查询→综合查询→配变数据查询
class TestPublicDataQuery(unittest.TestCase, PublicDataQueryPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = PublicDataQueryLog()

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        cls.driver.quit()

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        self.orl = Oracle()
        self.clear_values(PublicDataQueryPage)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

    # 基本档案，查询
    @BeautifulReport.add_test_img()
    def test_a_publiccon(self):
        # 点击国网冀北电力有限公司
        self.inputNode_jibei()
        # 点击唐山供电公司
        self.inputNode_tangshan()
        # 点击直属用户
        self.inputNode_directlyuser()
        # 点击国网_狮子湾农改
        self.inputNode_shiziwan()
        # 点击查询按钮
        self.btn_search()
        self.sleep_time(2)

    # 数据展示，电压曲线
    @BeautifulReport.add_test_img()
    def test_b_voltagecurve(self):
        # 点击数据展示
        self.btn_datashow()
        # 点击数据展示→查询
        self.btn_voltagecurve_search()
        # 点击基本档案
        self.btn_basicfile()

    # 数据展示，电流曲线
    @BeautifulReport.add_test_img()
    def test_c_currentcurve(self):
        # 点击数据展示
        self.btn_datashow()
        # 点击数据展示→电流曲线
        self.btn_currentcurve()
        # 点击数据展示→电流曲线→查询
        self.btn_currentcurve_search()
        # 点击基本档案
        self.btn_basicfile()

    # 数据展示，功率曲线
    @BeautifulReport.add_test_img()
    def test_d_powercurve(self):
        # 点击数据展示
        self.btn_datashow()
        # 点击数据展示→功率曲线
        self.btn_powercurve()
        # 点击数据展示→功率曲线→查询
        self.btn_powercurve_search()
        # 点击基本档案
        self.btn_basicfile()

    # 数据展示，功率因数曲线
    @BeautifulReport.add_test_img()
    def test_e_powerfactorcurve(self):
        # 点击数据展示
        self.btn_datashow()
        # 点击数据展示→功率因数曲线
        self.btn_powerfactorcurve()
        # 点击数据展示→功率因数曲线→查询
        self.btn_powerfactorcurve_search()
        # 点击基本档案
        self.btn_basicfile()

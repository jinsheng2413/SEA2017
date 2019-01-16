# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: pbs5000.py
@time: 2019/01/08 16:41
@desc:
"""
from time import sleep
from unittest import TestCase

from ddt import ddt

from com.nrtest.pbs.tree.tree_page import TreePage
from com.nrtest.sea.pages.other.menu_page import MenuPage


@ddt
class TestPBS5000(TestCase, TreePage):
    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        # 20-含电压等级厂站树； 11-并且带复选框
        # 30-厂站档案设备树；   21-并且带复选框
        # 40-普通树；         41-并且带复选框；采集运维→手动对时
        # menuPage = MenuPage.openMenu('0000302')  # 电压等级树--20
        # menuPage = MenuPage.openMenu('0000101')  # 厂站设备--30
        # menuPage = MenuPage.openMenu('0000204')  # 带勾选--41
        menuPage = MenuPage.openMenu('0001103')  # 电压等级树--40
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        menuPage.goto_frame()
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        # cls.closePages(cls)
        cls.goto_home_iframe(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        sleep(5)
        self.colseLeftTree()

    def test_query(self):
        """PBS500菜单及左边树功能测试

        :return:
        """
        # node_no = '{"NODE_FLAG": "01", "NODE_VALE": "01070110203"}'       # 电压等级树
        # node_no = '{"NODE_FLAG": "01", "NODE_VALE": "0107012010301"}'     # 厂站档案
        # node_no = '{"NODE_FLAG": "01", "NODE_VALE": "010701"}'            # 带复选框
        node_no = '{"NODE_FLAG": "01", "NODE_VALE": "020301"}'  # 普通树
        self.openLeftTree(node_no)

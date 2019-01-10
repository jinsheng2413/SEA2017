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
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu('0000302')
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        menuPage.to_frame()
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        # cls.closePages(cls)
        cls.to_home_iframe(cls)

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
        sleep(5)
        self.colseLeftTree()

    def test_query(self):
        node_no = '{"NODE_FLAG": "01", "NODE_VALE": "0107010203"}'
        self.openLeftTree(node_no)

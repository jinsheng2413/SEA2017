# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_manualEdit.py
@time: 2018-11-07 15:47
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.manualEidt_data import InterfaceManager_data
from com.nrtest.sea.pages.base_app.interfaceMan.manualEdit_page import ManualEditPage, ManualEdit_Locators
from com.nrtest.sea.task.commonMath import *


# 基本应用--接口管理--人工补录
@ddt
class Test_ManualEdit(unittest.TestCase, ManualEditPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(InterfaceManager_data.para_ManualEdit)
        cls.exec_script(cls, ManualEdit_Locators.DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.closePages(cls)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(SysDictManPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        sleep(4)
        # 打开左边树选择供电单位
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 用户编号
        self.inputStr_cons_no(para['CONS_NO'])
        # 处理类型
        self.inputSel_process_type(para['PROCESS_TYPE'])
        # 日期
        self.inputStr_date(para['DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*ManualEdit_Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(InterfaceManager_data.para_ManualEdit))
    def test_query(self, para):
        self.query(para)

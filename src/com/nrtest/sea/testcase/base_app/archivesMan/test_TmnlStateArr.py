# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_data import ArchivesMan_data
from com.nrtest.sea.pages.base_app.archivesMan.tmnlStateArr_Pages import TmnlStateArrPage, TmnlStateArrLocators
from com.nrtest.sea.task.commonMath import *


# 基本应用--》档案管理--》终端状态维护
@ddt
class TestTmnlStateArr(unittest.TestCase, TmnlStateArrPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(ArchivesMan_data.tmnlStateArr_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(TmnlStateArrPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 终端状态
        self.inputSel_tmnl_status(para['TMNL_STATUS'])
        # 统计时间
        self.inputStr_count_time(para['COUNT_TIME'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(TmnlStateArrLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(ArchivesMan_data.tmnlStateArr_para))
    def test_query(self, para):
        self.query(para)

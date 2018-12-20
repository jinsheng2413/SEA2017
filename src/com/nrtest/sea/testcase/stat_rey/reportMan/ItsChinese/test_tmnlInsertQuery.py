# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_tmnlInsertQuery.py
@time: 2018/11/7 0007 14:59
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.reportMan.ItsChinese.itsChinese import TtChinese
from com.nrtest.sea.pages.stat_rey.reportMan.ItsChinese.tmnlInsertQuery_page import TmnlInsertQueryPage, TmnlInsertQueryLocators
from com.nrtest.sea.task.commonMath import *


# 统计查询-->报表管理-->国网报表-->智能电能表及终端设备接入情况
@ddt
class TestTmnlInsertQuery(unittest.TestCase,TmnlInsertQueryPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(TtChinese.tmnlInsertQuery_para)


    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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

    def day_query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        sleep(2)
        #打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        self.exec_script(TmnlInsertQueryLocators.START_DATE_JS)
        self.exec_script(TmnlInsertQueryLocators.END_DATE_JS)

        self.clickRadioBox(para['BOX'])
        #日期
        self.inputStr_date(para['DATE'])
        #到
        self.inputStr_to(para["TO"])
        #终端类型
        self.inputSel_tmnlType(para['TMNL_TYPE'])
        #终端厂商
        self.inputSel_tmnlFactory(para['TMNL_FACTORY'])
        #统计口径
        self.inputSel_countCaliber(para['COUNT_CALIBER'])


        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*TmnlInsertQueryLocators.TAB_ONE)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TtChinese.tmnlInsertQuery_para,tabName='日'))
    def test_dayQuery(self, para):
        self.day_query(para)

    def month_query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])

        self.clickRadioBox(para['BOX'])
        # 终端类型
        self.inputSel_tmnlType(para['TMNL_TYPE'])
        # 终端厂商
        self.inputSel_tmnlFactory(para['TMNL_FACTORY'])
        # 统计口径
        self.inputSel_countCaliber(para['COUNT_CALIBER'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*TmnlInsertQueryLocators.TAB_ONE)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TtChinese.tmnlInsertQuery_para,tabName='月'))
    def test_monthQuery(self, para):
        self.month_query(para)





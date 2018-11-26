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
from com.nrtest.sea.data.stat_rey.dataAnalyse.loadrankanalyse_para import LoadRankAnalyse_para
from com.nrtest.sea.pages.stat_rey.dataAnalyse.gisPanoramaDisplay_page import GisPanoramaDisplayPage, \
    GisPanoramaDisplayLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestGisPanoramaDisplay(unittest.TestCase, GisPanoramaDisplayPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(LoadRankAnalyse_para.gisPanoramaDisplay_para)
        sleep(2)
        cls.exec_script(cls, GisPanoramaDisplayLocators.JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.refreshPage(cls)

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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 用户类型
        self.inputSel_userType(para['USER_TYPE'])
        # 逐日显示
        self.inputStr_day_display(para['DAY_DISPLAY'])
        # 查询日期
        self.inputStr_query_time(para['DATE'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @data(*DataAccess.getCaseData(LoadRankAnalyse_para.gisPanoramaDisplay_para))
    def test_query(self, para):
        self.query(para)

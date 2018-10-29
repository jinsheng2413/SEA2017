# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.allCollectSuccessRate_page import AllCollectSuccessRatePage, \
    AllCollectSuccessRateLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestAllCollectSuccessRate(unittest.TestCase, AllCollectSuccessRatePage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.allCollectSuccessRate_para)
        sleep(2)
        cls.exec_script(cls, AllCollectSuccessRateLocators.USERTYPE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        # 输入用户编号
        self.inputStr_userNo(para['USER_NO'])
        # 输入表资产号
        self.inputStr_surfaceAssetNo(para['SURFACE_ASSET_NO'])
        # 电能表抄读状态
        self.inputStr_meterReadState(para['METER_READ_STATE'])
        # 用户类型

        self.inputStr_userType(para['USER_TYPE'])
        # 终端运行状态
        self.inputStr_Tmnl_runState(para['TMNL_RUN_STATE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*AllCollectSuccessRateLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SynthQuery_data.allCollectSuccessRate_para))
    def test_query(self, para):
        self.query(para)

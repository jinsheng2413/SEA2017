# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/30 8:42
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.transformerMonitor.transformerMonitor_data import TradnsformerMonitorData
from com.nrtest.sea.locators.adv_app.transformerMonitor.powerFactorCount.powerFactorCountStatic_locators import \
    PowerFactorCountStaticLocators
from com.nrtest.sea.pages.adv_app.transformerMonitor.powerFactorCount.powerFactorCountStatic_page import \
    PowerFactorCountStaticPage
from com.nrtest.sea.task.commonMath import *


# 高级应用--》配变监测分析--》功率因数越限统计
# 功率因数越限统计
@ddt
class TestSpVoltAnalyseStatic(unittest.TestCase, PowerFactorCountStaticPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(TradnsformerMonitorData.para_PowerFactorCount)
        cls.driver.execute_script(PowerFactorCountStaticLocators.QUERY_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        # cls.refreshPage(cls)

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
        # self.clear_values(SysDictManPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """
        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 供电单位
        openLeftTree(para['ORG_NO'])
        # 用户类型
        self.inputRSel_cons_type(para['CONS_TYPE'])
        # 查询日期
        self.inputStr_query_date(para['QUERY_DATE'])

        self.btn_query()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*PowerFactorCountStaticLocators.TABLE_DATA)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(TradnsformerMonitorData.para_PowerFactorCount, '功率因数越限统计'))
    def test_que(self, para):
        self.query(para)

    # def test_test(self):
    #     # 供电单位
    #     openLeftTree('13401')
    #     # 用户类型
    #     self.inputRSel_cons_type('全部')
    #     # 查询日期
    #     self.inputStr_query_date('2018-09-01')
    #
    #     self.btn_query()
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(*PowerFactorCountStaticLocators.TABLE_DATA)
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

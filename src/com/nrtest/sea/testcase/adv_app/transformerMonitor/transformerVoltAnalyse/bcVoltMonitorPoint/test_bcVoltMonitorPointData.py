# -*- coding:utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 14:42
@desc:
"""

import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.transformerMonitor.transformerMonitor_data import TradnsformerMonitorData
from com.nrtest.sea.locators.adv_app.transformerMonitor.transformerVoltAnalyse.bcVoltMonitorPoint.bcVoltMonitorPointData_locators import \
    BcVoltMonitorPointDataLocators
from com.nrtest.sea.pages.adv_app.transformerMonitor.transformerVoltAnalyse.bcVoltMonitorPoint.bcVoltMonitorPointData_page import \
    BcVoltMonitorPointDataPage
from com.nrtest.sea.task.commonMath import *


# 高级应用--》配变监测分析--》电压质量分析--》B/C类电压监测点
# B/C类电压监测点数据
@ddt
class TestBcVoltMonitorPointDataQuery(unittest.TestCase, BcVoltMonitorPointDataPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(TradnsformerMonitorData.para_BcVoltMonitorPoint)
        clickTabPage('B/C类电压监测点数据')
        cls.driver.execute_script(BcVoltMonitorPointDataLocators.QUERY_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        # 监测点类型
        self.inputRSel_monitor_point_type(para['MONITOR_POINT_TYPE'])
        # 监测点名称
        self.inputStr_monitor_point_name(para['MONITOR_POINT_NAME'])
        # 查询日期
        self.inputStr_query_date(para['QUERY_DATE'])

        self.btn_query()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*BcVoltMonitorPointDataLocators.TABLE_DATA)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(TradnsformerMonitorData.para_BcVoltMonitorPoint, 'B/C类电压监测点数据'))
    def test_que(self, para):
        self.query(para)

    # def test_test(self):
    #     # 供电单位
    #     openLeftTree('13401')
    #     # 监测点类型
    #     self.inputRSel_monitor_point_type('全部')
    #     # 监测点名称
    #     self.inputStr_monitor_point_name('')
    #     # 查询日期
    #     self.inputStr_query_date('2018-09-01')
    #
    #     self.btn_query()
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(*BcVoltMonitorPointDataLocators.TABLE_DATA)
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

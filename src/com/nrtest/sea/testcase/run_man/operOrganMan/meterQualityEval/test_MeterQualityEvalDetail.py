# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_Tmnl.py
@time: 2018/11/13 9:20
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.operOrganMan.operOrganMan_data import OperOrganManData
from com.nrtest.sea.locators.run_man.operOrganMan.qualityEvaluate.meterQualityEval_locators import \
    MeterQualityEvalDetailLocators
from com.nrtest.sea.pages.run_man.operOrganMan.qualityEvaluate.meterQualityEval_page import \
    MeterQualityEvalDetailPage
from com.nrtest.sea.task.commonMath import *


# 运行管理→采集运维平台→采集终端质量评价
# 终端质量评价明细
@ddt
class TestDemo(unittest.TestCase, MeterQualityEvalDetailPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        cls.driver = openMenu(OperOrganManData.para_MeterQualityEval)
        clickTabPage(OperOrganManData.para_MeterQualityEvalDetail)
        sleep(2)
        cls.exec_script(cls, MeterQualityEvalDetailLocators.QUERY_START_DATE_JS)
        cls.exec_script(cls, MeterQualityEvalDetailLocators.QUERY_END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭页面
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

    def query(self, para):
        """
        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 供电单位
        sleep(2)
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 用户类型
        self.inputRSel_cons_type(para['CONS_TYPE'])
        # 故障严重程度
        self.inputRSel_fault_level(para['FAULT_LEVEL'])
        # 电表厂家
        self.inputRSel_meter_fac(para['METER_FAC'])
        # 故障类别
        self.inputRSel_fault_type(para['FAULT_TYPE'])
        # 故障开始日期
        self.inputStr_query_start_date(para['START_DATE'])
        # 故障开始日期
        self.inputStr_query_end_date(para['END_DATE'])

        self.btn_query()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*MeterQualityEvalDetailLocators.TABLE_DATA)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(
        *DataAccess.getCaseData(OperOrganManData.para_MeterQualityEval, OperOrganManData.para_MeterQualityEvalDetail))
    def test_query(self, para):
        self.query(para)

    # def test_test(self):
    #     # 供电单位
    #     openLeftTree('13401')
    #     # 终端类型
    #     self.inputRSel_tmnl_type('全部')
    #     # 终端厂家
    #     self.inputRSel_tmnl_fac('宁波三星')
    #     # 查询日期
    #     self.inputStr_query_date('2018-09')
    #
    #     self.btn_query()
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(*TmnlClockStaticLocators.TABLE_DATA)
    #     self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()

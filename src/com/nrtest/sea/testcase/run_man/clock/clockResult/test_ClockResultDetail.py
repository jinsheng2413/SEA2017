# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_Tmnl.py
@time: 2018/10/30 13:46
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.clock.clock_data import ClockData
from com.nrtest.sea.locators.run_man.clock.clockResult_locators import \
    ClockResultDetailLocators
from com.nrtest.sea.pages.run_man.clock.clockResult_page import ClockResultDetailPage
from com.nrtest.sea.task.commonMath import *


# 运行管理→时钟管理→对时结果分析
# 对时结果明细
@ddt
class TestDemo(unittest.TestCase, ClockResultDetailPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        cls.driver = openMenu(ClockData.para_ClockResult)
        clickTabPage('对时结果明细')
        sleep(2)
        cls.exec_script(cls, ClockResultDetailLocators.QUERY_DATE_JS)

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
        # 类别
        self.inputRSel_clock_model(para['CLOCK_MODEL'])
        # 电表资产号
        self.inputStr_met_asset_no(para['MET_ASSET_NO'])
        # 终端资产号
        self.inputStr_tmnl_asset_no(para['TMNL_ASSET_NO'])
        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        # 查询日期
        self.inputStr_query_date(para['QUERY_DATE'])

        self.btn_query()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ClockResultDetailLocators.TABLE_DATA)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ClockData.para_ClockResult, '对时结果明细'))
    def test_query(self, para):
        self.query(para)

    # def test_test(self):
    #     # 供电单位
    #     sleep(2)
    #     openLeftTree('13401')
    #     # 偏差范围
    #     self.inputRSel_offset_range('全部')
    #     # 终端类型
    #     self.inputRSel_tmnl_type('全部')
    #     # 终端型号
    #     self.inputStr_tmnl_model('')
    #     # 终端厂家
    #     self.inputRSel_tmnl_fac('宁波三星')
    #     # 终端地址
    #     self.inputStr_tmnl_addr('')
    #     # 是否在线
    #     self.inputRSel_is_online('全部')
    #     # 查询日期
    #     self.inputStr_query_date('2018-09')
    #     # 对时结果
    #     self.inputRSel_call_status('全部')
    #
    #     self.btn_query()
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(*TmnlClockDetailLocators.TABLE_DATA)
    #     self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()

# -*- coding: utf-8 -*-

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

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.realDataPage import RealDataPage, RealDataLocators
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→抄表数据查询（冀北）
@ddt
class TestRealData_Rdetail(unittest.TestCase, RealDataPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.realData_para)
        sleep(2)
        cls.exec_script(cls, RealDataLocators.QUERY_TIME_RDETAIL)

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
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        sleep(2)
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 选择抄表段号
        self.inputStr_ReadMeterSegmentNo_Rdetail(para['READ_METER_SEGMENT_NO'])
        # 电表资产号
        self.inputStr_MeterAssert_Rdetail(para['METER_ASSERT'])
        # 用户类型
        self.inputSel_userType_Rdetail(para['USER_TYPE'])
        # 相位
        self.inputSel_phase_Rdetail(para['PHASE'])
        # 查询日期
        self.inputStr_Time_Rdetail(para['QUERY_TIME'])
        # 数据类别
        self.inputSel_dataType(para['DATA_TYPE'])
        # 电能表抄读状态
        self.inputSel_meter_read_state_Rdetail(para['METER_READ_STATE'])
        # 终端运行状态
        self.inputSel_TmnlRunState_RDetail(para['TMNL_RUN_STATE'])

        self.btn_rdetail_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @data(*DataAccess.getCaseData(SynthQuery_data.realData_para, SynthQuery_data.realData_rdetail_tab))
    def test_query(self, para):
        self.query(para)

# -*- coding: utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: test_meterClockMan.py
@time: 2018/11/2 0002 14:12
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.meterMan.meterClockMan_data import MeterClockMan_data
from com.nrtest.sea.pages.run_man.meterMan.meterClockMan_pages import MeterClockManPage, MeterClockManLocators
from com.nrtest.sea.task.commonMath import *


# 运行管理-电能表管理-电能表状态查询
@ddt
class TestDemo(unittest.TestCase, MeterClockManPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        cls.driver = openMenu(MeterClockMan_data.MeterClockMan_para, True)
        sleep(2)
        cls.exec_script(cls, MeterClockManLocators.START_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        self.DisplayTreeMenu()
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        self.inputSel_eventtype(para['EVENT_TYPE'])
        self.inputSel_tmnlfactory(para['TMNL_FACORY'])
        self.inputSel_meterfactory(para['METER_FACTORY'])
        self.inputStr_tmnladdr(para['TMNL_ADDR'])
        self.inputStr_userno(para['USER_NO'])
        self.inputStr_meterno(para['METER_NO'])
        self.inputStr_date(para['DATE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MeterClockMan_data.MeterClockMan_para))
    def test_query(self, para):
        self.query(para)
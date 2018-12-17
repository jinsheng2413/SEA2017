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

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyManage_data import \
    DistributedEnergyMange_data
from com.nrtest.sea.pages.adv_app.vipConsMan.distributedEnergyMange.distributedEnergyStat_page import \
    DistributedEnergyStatPage, DistributedEnergyStatLocators
from com.nrtest.sea.task.commonMath import *


# 高级应用--》重点用户检测--》分布式电源管理--》分布式电源接入统计
@ddt
class TestDemo(unittest.TestCase, DistributedEnergyStatPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(DistributedEnergyMange_data.DistributedEnergyStat_para)
        clickTabPage('分布式电源接入统计')
        sleep(2)
        cls.exec_script(cls, DistributedEnergyStatLocators.START_DATE_JS)

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
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''

        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 发电量消纳方式
        self.inputSel_powerConsumptionMode(para['POWER_CONSUMPTION_MODE'])
        # 日期
        self.inputStr_date(para['DATE'])
        # 发电类型
        self.inputSel_powerMode(para['POWER_MODE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DistributedEnergyMange_data.DistributedEnergyStat_para))
    def test_query(self, para):
        self.query(para)

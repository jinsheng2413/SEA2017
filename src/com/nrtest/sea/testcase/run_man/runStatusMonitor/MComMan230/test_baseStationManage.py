# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_baseStationManage.py
@time: 2018/11/6 0006 16:04
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.runStatusMonitor.MComMan230.mComMan230 import MComMan230
from com.nrtest.sea.pages.run_man.runStatusMonitor.MComMan230.baseStationManage_page import BaseStationManagePage, \
    BaseStationManageLocators
from com.nrtest.sea.task.commonMath import *

#运行管理--》采集信道管理--》230M通信管理--》站点状态监控
@ddt
class TestbaseStationManage(unittest.TestCase, BaseStationManagePage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）

        cls.driver = openMenu(MComMan230.baseStationManage_para)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 关闭菜单页面
        cls.closePages(cls)

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
        sleep(2)
        # 通信地址
        self.inputStr_communicationAddr(para['COMMUNICATION_ADDR'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*BaseStationManageLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(MComMan230.baseStationManage_para))
    def test_query(self, para):
        self.query(para)

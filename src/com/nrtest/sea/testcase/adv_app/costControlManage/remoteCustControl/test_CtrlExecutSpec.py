# -*- coding:utf-8 -*-

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
from com.nrtest.sea.data.adv_app.costControlManage.remoteCustControl.remoteCustControl_data import \
    RemoteCustControl_data
from com.nrtest.sea.pages.adv_app.costControlManage.remoteCustControl.ctrlExecutSpec_page import CtrlExecutSpecPage, \
    CtrlExecutSpecLocators
from com.nrtest.sea.task.commonMath import *


# 高级应用--》费控管理--》远程费控--》专变用户远程费控执行
# CtrlExecutSpecPage


@ddt
class TestDemo(unittest.TestCase, CtrlExecutSpecPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(RemoteCustControl_data.CtrlExecutSpec_para)

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
        self.inputStr_userNo(para["USER_NO"])
        # 输入用户名称
        self.inputStr_userName(para['USER_NAME'])
        # 终端地址
        self.inputStr_tmnlAddr(para['TMNL_ADDR'])
        # 控制类型
        self.inputRSel_controlType(para['CONTROL_TYPE'])
        # 执行状态
        self.inputSel_exeStatus(para['EXE_STATUS'])
        # 工单号
        self.inputStr_workOrder(para['WORK_ORDER'])
        # 开始时间
        self.inputStr_startTime(para['START_TIME'])
        # 结束时间
        self.inputStr_endTime(para['END_TIME'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CtrlExecutSpecLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(RemoteCustControl_data.CtrlExecutSpec_para))
    def test_query(self, para):
        self.query(para)

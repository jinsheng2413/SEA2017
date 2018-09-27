# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
'''
from com.nrtest.sea.data.base_app.custMan.custMan_data import CustMan_data
from com.nrtest.sea.pages.base_app.custMan.ctrlExecutPage import CtrlExecutPage,CtrlExecutLocators
from com.nrtest.sea.task.commonMath import *
from com.nrtest.common.data_access import DataAccess
from ddt import ddt, data
import unittest
from time import sleep


#基本应用--》费控管理--》低压用户远程费控执行
@ddt
class TestCtrlExecut(unittest.TestCase,CtrlExecutPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(CustMan_data.ctrlExecut_para)
        sleep(2)
        cls.exec_script(cls,CtrlExecutLocators.START_DATE_JS)
        cls.exec_script(cls,CtrlExecutLocators.END_DATE_JS)

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
        # 去除查询干扰数据(要传入对应的page页面类)
        self.clear_values(CtrlExecutPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''

        #打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        #用户编号
        self.inputStr_userNo(para["USER_NO"])
        #用户名称
        self.inputStr_userName(para['USER_NAME'])
        #终端地址
        self.inputStr_tmnlAddr(para['TMNL_ADDR'])
        #控制类型
        self.inputSel_controlType(para['CONTROL_TYPE'])
        #抄表段号
        self.inputStr_sectNo(para['SECT_NO'])
        #执行状态
        self.inputSel_exeStatus(para["EXE_STATUS"])
        #数据来源
        self.inputSel_dataCome(para['DATA_COME'])
        #确认状态
        self.inputSel_confirmStatus(para['CONFIRM_STATUS'])
        #开始时间
        self.inputStr_startTime(para['START_TIME'])
        #结束时间
        self.inputStr_ENDTIme(para['END_TIME'])
        #工单号
        self.inputStr_workOrder(para['WORK_ORDER'])
        #执行结果状态
        self.inputSel_exeResultStatus(para['EXE_RESULT_STATUS'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*CtrlExecutLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(CustMan_data.ctrlExecut_para))
    def test_query(self, para):
        self.query(para)




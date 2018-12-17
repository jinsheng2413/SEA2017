# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
'''
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.tmnlInstallDetai_page import TmnlInstallDetaiPage, \
    TmnlInstallDetaiLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestTmnlInstallDetai_debug(unittest.TestCase, TmnlInstallDetaiPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(DataGatherMan_data.tmnlInstallDetail_para)

        clickTabPage(DataGatherMan_data.tmnlInstallDetail_tabOne)
        sleep(2)
        cls.exec_script(cls, TmnlInstallDetaiLocators.START_DATE_JS_COUNT)
        cls.exec_script(cls, TmnlInstallDetaiLocators.END_DATE_JS_COUNT)
        # 下拉选择无需移除readonly属性
        # cls.exec_script(cls, TmnlInstallDetaiLocators.LCT_JS_COUNT)
        # cls.exec_script(cls, TmnlInstallDetaiLocators.METER_TYPE_JS_COUNT)
        # cls.exec_script(cls, TmnlInstallDetaiLocators.TMNL_FACTORY_JS_COUNT)
        # cls.exec_script(cls, TmnlInstallDetaiLocators.TMNL_TYPE_JS_COUNT)

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
        # 注册菜单
        self.menu_name = para['MENU_NAME']

        sleep(2)
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 开始时间
        self.inputStr_startTime_count(para['START_TIME'])
        # 结束时间
        self.inputStr_enTime_Count(para['END_TIME'])
        # 运行状态
        self.inputSel_runState_count(para['RUN_STATE'])
        # 流程标识
        self.inputSel_processID_count(para['PROCESS_ID'])
        # 申请单号
        self.inputStr_applyNo_count(para['APPLY_NO'])
        # 用户编号
        self.inputStr_userNo_count(para['USER_NO'])
        # 终端地址
        self.inputStr_tmnlAddr_count(para["TMNL_ADDR"])
        # 终端厂家
        self.inputSel_tmnlFactory_count(para['TMNL_FACTORY'])
        # 装接类型
        self.inputSel_moutingType_count(para['MOUNTING_TYPE'])
        # 终端类型
        self.inputSel_tmnlType_count(para['TMNL_TYPE'])
        # 通信规约
        self.inputSel_LCT_count(para['LCT'])
        # 表类型
        self.inputSel_surfaceType_count(para['SURFACE_TYPE'])

        self.btn_tmnl_qry()
        self.sleep_time(2)

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(self.check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.tmnlInstallDetail_para, DataGatherMan_data.tmnlInstallDetail_tabOne))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.tmnlInstallDetail_para, DataGatherMan_data.tmnlInstallDetail_tabOne, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)

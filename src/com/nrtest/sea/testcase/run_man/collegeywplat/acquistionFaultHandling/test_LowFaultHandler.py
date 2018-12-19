# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_faultHandler.py
@time: 2018/11/12 0012 9:31
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.collegeywplat.acquistionFaultHandling.acquistionFaultHandling_data import \
    AcquistionFaultHandling_data
from com.nrtest.sea.pages.collegeywplat.acquistionFaultHandling.lowFaultHandler_page import LowFaultHandlerPage, LowFaultHandlerLocators
from com.nrtest.sea.task.commonMath import *


# 运行管理-->采集运维平台-->采集故障处理-->低压故障处理
@ddt
class TestFaultHandler(unittest.TestCase,LowFaultHandlerPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(AcquistionFaultHandling_data.lowFaultHandler_para)


    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        sleep(2)
        self.clickAlert()
        clickTabPage(para['TAB_NAME'])

        self.exec_script(LowFaultHandlerLocators.START_DATE_JS)
        self.exec_script(LowFaultHandlerLocators.END_DATE_JS)
        #打开左边树并选择
        self.driver = openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        #故障开始日期
        self.inputStr_faultStartDate(para['FAULT_START_DATE'])
        #故障结束日期
        self.inputStr_faultEndDate(para['FAULT_END_DATE'])
        #流程状态
        self.inputSel_process(para['PROCESS_STATUS'])
        #故障来源
        self.inputSel_faultFrom(para['FAULT_FROM'])
        #故障严重程度
        self.inputSel_faultSeverity(para['FAULT_SEVERITY'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*LowFaultHandlerLocators.TAB_ONE)
        # self.assertTrue(result)

    #@BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(AcquistionFaultHandling_data.lowFaultHandler_para,AcquistionFaultHandling_data.lowFaultHandler_tab_handler))
    def test_query(self, para):
        self.query(para)




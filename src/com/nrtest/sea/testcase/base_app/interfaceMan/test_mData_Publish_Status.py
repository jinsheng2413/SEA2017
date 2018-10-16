# -*- coding:utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_mData_Publish_Status.py
@time: 2018-09-21 10:47
@desc:
'''

from com.nrtest.common.dictionary import Dict
from com.nrtest.sea.pages.base_app.interfaceMan.mDataPublishStatus_page import MDataPublishStatusPage
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.locators.base_app.interfaceMan.mDataPublishStatus import MDataPublishStatus_locators
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.sea.data.base_app.interfaceMan.mDataPublishStatus_data import MDataPublishStatus_data
from com.nrtest.sea.task.commonMath import *
from ddt import ddt,data
import unittest
from time import sleep

@ddt
class Test_mData_Publish_StatusPage(unittest.TestCase, MDataPublishStatusPage):
    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(MDataPublishStatus_data.para_MDataPublishStatus)
        sleep(2)
        cls.exec_script(cls,MDataPublishStatus_locators.START_DATE_JS)
        cls.exec_script(cls,MDataPublishStatus_locators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        #cls.refreshPage(cls)

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
        print('-----')
        # 选择业务系统
        self.inputSel_BusinessSystem(para['BUSINESS_SYSTEM'])
        # 开始时间
        self.inputStr_receive_time(para['START_DATE'])
        # 结束时间
        self.inputStr_end_time(para['END_DATE'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*MDataPublishStatus_locators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(MDataPublishStatus_data.para_MDataPublishStatus))
    def test_query(self,para):
        self.query(para)

# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_mDataPublishStatus.py
@time: 2018-10-30 16:10
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.interfaceMan.mDataPublishStatus2_data import InterfaceManager_data
from com.nrtest.sea.pages.base_app.interfaceMan.mDataPublishStatus2_page import MDataPublishStatus2Page, \
    MDataPublishStatus2_locators
from com.nrtest.sea.task.commonMath import *


@ddt
class Test_mDataPublishStatus2(unittest.TestCase, MDataPublishStatus2Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(InterfaceManager_data.para_MDataPublishStatus2)
        sleep(2)
        cls.exec_script(cls, MDataPublishStatus2_locators.START_DATE_JS)
        cls.exec_script(cls, MDataPublishStatus2_locators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        self.inputSel_BusinessSystem(para['BUSINESS_SYSTEM'])
        # 开始时间
        self.inputStr_receive_time(para['START_DATE'])
        # 结束时间
        self.inputStr_end_time(para['END_DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*MDataPublishStatus2_locators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(InterfaceManager_data.para_MDataPublishStatus2))
    def test_query(self, para):
        self.query(para)

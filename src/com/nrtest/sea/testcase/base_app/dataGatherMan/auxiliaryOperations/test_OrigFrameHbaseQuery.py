# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_OrigFrameHbaseQuery.py
@time: 2018/11/9 0009 15:41
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.auxiliaryOperations.auxiliaryOperations_data import \
    AuxiliaryOperationsData
from com.nrtest.sea.pages.base_app.dataGatherMan.auxiliaryOperations.origFrameHbaseQuery_page import \
    OrigFrameHbaseQueryPage, OrigFrameHbaseQueryLocators
from com.nrtest.sea.task.commonMath import *


# 运行管理-->采集运维平台-->辅助运维--》报文查询
@ddt
class TestOrigFrameHbaseQuery(unittest.TestCase, OrigFrameHbaseQueryPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(AuxiliaryOperationsData.origFrameHbaseQuery_para)
        sleep(2)
        cls.exec_script(cls,OrigFrameHbaseQueryLocators.START_DATE_JS)

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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """


        #终端地址
        self.inputStr_tmnlAddr(para['TMNL_ADDR'])
        #查询时间
        self.inputStr_query_time(para['QUERY_TIME'])
        #报文类型
        self.inputSel_messageType(para['MESSAGE'])
        # #从
        # self.inputStr_from(para['FROM'])
        # #到
        # self.inputStr_to(para['TO'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context()
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(AuxiliaryOperationsData.origFrameHbaseQuery_para))
    def test_query(self, para):
        self.query(para)




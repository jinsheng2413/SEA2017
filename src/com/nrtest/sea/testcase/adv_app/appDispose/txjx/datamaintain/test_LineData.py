# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.txjx.datamaintain.datamaintain_data import Datamaintain_data
from com.nrtest.sea.pages.adv_app.txjx.datamaintain.lineData_page import LineDataPage,LineDataLocators
from com.nrtest.sea.task.commonMath import *
from ddt import ddt, data
from time import sleep
from com.nrtest.common.BeautifulReport import BeautifulReport
import unittest


@ddt
#高级应用-->台线系统--》资料维护--》线路资料维护
class TestDemo(unittest.TestCase,LineDataPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(Datamaintain_data.lineData_para,True)

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
        #输入负责人
        self.inputSel_master(para['MASTER'])
        #输入线路名称
        self.inputStr_lineName(para['LINE_NAME'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LineDataLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(Datamaintain_data.lineData_para))
    def test_query(self, para):
        self.query(para)




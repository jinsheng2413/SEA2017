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
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.batchFetch_page import BatchFetchPage, BatchFetchLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestDemo(unittest.TestCase, BatchFetchPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(DataGatherMan_data.batchFetch_para)
        sleep(2)
        cls.exec_script(cls, BatchFetchLocators.START_DATE_JS)

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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 任务名称
        self.inputStr_taskName(para['TASK_NAME'])
        # 操作人
        self.inputStr_performer(para['PERFORMER'])
        # 开始时间
        self.inputStr_startTime(para['START_TIME'])
        # 有效性
        self.inputSel_effectiveness(para['EFFECTIVENESS'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(BatchFetchLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(DataGatherMan_data.batchFetch_para))
    def test_query(self, para):
        self.query(para)

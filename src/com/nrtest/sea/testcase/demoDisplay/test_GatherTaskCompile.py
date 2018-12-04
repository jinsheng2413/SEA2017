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

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.dataGatherMan_data import DataGatherMan_data
from com.nrtest.sea.pages.base_app.dataGatherMan.GatherTaskCompile_Page import GatherTaskCompilePage
from com.nrtest.sea.task.commonMath import *


@ddt
class TestGatherTaskCompile(unittest.TestCase, GatherTaskCompilePage):

    @classmethod
    def setUpClass(cls):

        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(DataGatherMan_data.gatherTaskCompile_para)
        clickTabPage('任务查询')

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        sleep(2)

        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 任务类型
        self.inputSel_taskType(para['TASK_TYPE'])
        # 任务编号
        self.inputStr_taskNo(para['TASK_NO'])
        # 任务名称
        self.inputStr_taskName(para['TASK_NAME'])
        # 任务状态
        self.inputSel_taskState(para['TASK_STATE'])
        # 终端地址
        self.inputStr_TMNL_ADDR(para['TMNL_ADDR'])
        # 采集点名称
        self.inputStr_CollectionPointName(para['COLLECTION_POINT_NAME'])
        # 终端类型
        self.inputRSel_TmnlType(para['TMNL_TYPE'])

        self.btn_qry()
        self.sleep_time(2)

    def checkValue(self, tst_case_id):
        self.assertTrue(self.commonAssertValue(tst_case_id))

    @data(*(DataAccess.getCaseData(DataGatherMan_data.gatherTaskCompile_para)))
    def test_query(self, para):
        """
            查询结果校验
        :return:
        """
        self.query(para)
        self.checkValue(para['TST_CASE_ID'])
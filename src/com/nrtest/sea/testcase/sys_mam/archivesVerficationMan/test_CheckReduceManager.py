# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_CheckReduceManager.py
@time: 2018/11/16 0016 15:25
@desc:
"""
from com.nrtest.sea.data.sys_mam.archivesVerficationMan.archivesVerficationMan_data import ArchivesVerficationMan_data
from com.nrtest.sea.pages.sys_mam.archivesVerficationMan.checkReduceManager_page import CheckReduceManagerPage,CheckReduceManagerLocators
from com.nrtest.sea.task.commonMath import *
from com.nrtest.common.data_access import DataAccess
from ddt import ddt, data
from time import sleep
from com.nrtest.common.BeautifulReport import BeautifulReport
import unittest

CheckReduceManagerPage
@ddt
class TestCheckReduceManager(unittest.TestCase,CheckReduceManagerPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(ArchivesVerficationMan_data.VerficationResultDetail_para)

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

        #打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 开始时间
        self.inputStr_startTime(para['START_TIME'])
        # 结束时间
        self.inputStr_end_time(para['END_TIME'])
        #申请单号
        self.inputStr_applyNo(para['APPLY_NO'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesVerficationMan_data.checkReduceManager_para))
    def test_query(self, para):
        self.query(para)




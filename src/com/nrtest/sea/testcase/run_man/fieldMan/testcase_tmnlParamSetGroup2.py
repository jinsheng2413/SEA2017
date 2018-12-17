# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: testcase_tmnlParamSetGroup2.py
@time: 2018/11/8 0008 13:50
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.fieldMan.tmnlParamSetGroup2_data import TermParaSetGroup2_data
from com.nrtest.sea.pages.run_man.fieldMan.tmnlParamSetGroup2_pages import TermParaSetGroup2Page
from com.nrtest.sea.task.commonMath import *

TermParaSetGroup2Page

# 运行管理-现场管理-终端抄表参数设置
@ddt
class TestDemo(unittest.TestCase, TermParaSetGroup2Page):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        cls.driver = openMenu(TermParaSetGroup2_data.TermParaSetGroup2_para)
        sleep(2)

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
        sleep(2)
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        self.inputSel_tmnl_protory(para['TMNL_PROTORY'])
        self.inputSel_task_status(para['TASK_STATUS'])


        self.btn_qry()
        self.sleep_time(2)

        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TermParaSetGroup2_data.TermParaSetGroup2_para))
    def test_query(self, para):
        self.query(para)



# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_ConsDataQry.py
@time: 2018/11/28 0028 10:17
@desc:
"""
import unittest
from time import sleep

from ddt import ddt

from com.nrtest.sea.data.stat_rey.synthQuery.synthQuery_data import SynthQuery_data
from com.nrtest.sea.pages.stat_rey.synthQuery.consDataQry_page import ConsDataQryPage
from com.nrtest.sea.task.commonMath import *


# 统计查询→综合查询→用户数据
@ddt
class TestConsDataQry(unittest.TestCase,ConsDataQryPage):
    CheckBoxName = '电流曲线'

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(SynthQuery_data.consDataQry_para)
        sleep(2)
        clickTabPage(SynthQuery_data.consDataQry_tab_ele)

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
        #self.recoverLeftTree()

    def query(self):
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        #点击复选框
        self.clickRadioBox(self.CheckBoxName)


        # self.btn_qry()
        # self.sleep_time(2)
        # 校验


    #@BeautifulReport.add_test_img()
    #@data(*DataAccess.getCaseData())
    def test_query(self):
        """
        复选框
        :return:
        """
        self.query()




# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_news.py
@time: 2018-11-02 10:36
@desc:
"""

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.newsanswer.news_data import NewsAnswer
from com.nrtest.sea.pages.adv_app.newsanswer.news_page import News_Locators, News_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--问题交流平台--问题在线交流
@ddt
class Test_News(unittest.TestCase, News_Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(NewsAnswer.para_News)
        sleep(2)
        cls.exec_script(cls, News_Locators.START_DATE_JS)
        cls.exec_script(cls, News_Locators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        self.displayTreeMenu()
        # 打开左边树选择供电单位
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 问题标题
        self.inputStr_question_title(para['QUESTION_TITLE'])
        # 问题类型
        self.inputSel_question_type(para['QUESTION_TYPE'])
        # 问题版块
        self.inputSel_question_plate(para['QUESTION_PLATE'])
        # 紧急程度
        self.inputSel_emergency_degree(para['EMERGENCY_DEGREE'])
        # 查询方式
        self.inputSel_query_method(para['QUERY_METHOD'])
        # 问题状态
        self.inputSel_question_status(para['QUESTION_STATUS'])
        # 开始日期
        self.inputStr_start_date(para['START_DATE'])
        # 结束日期
        self.inputStr_end_date(para['END_DATE'])
        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*News_Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(NewsAnswer.para_News))
    def test_query(self, para):
        self.query(para)

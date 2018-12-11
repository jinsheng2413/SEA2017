# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: test_knowledge.py
@time: 2018-11-02 11:37
@desc:
'''

import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.newsanswer.knowledge_data import NewsAnswer
from com.nrtest.sea.pages.adv_app.newsanswer.knowledge_page import Knowledge_Locators, Knowledge_Page
from com.nrtest.sea.task.commonMath import *


# 高级应用--问题交流平台--问题在线交流
@ddt
class Test_Knowledge(unittest.TestCase, Knowledge_Page):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(NewsAnswer.para_Knowledge, True)
        sleep(2)
        cls.exec_script(cls, Knowledge_Locators.START_DATE_JS)
        cls.exec_script(cls, Knowledge_Locators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

    def query(self, para):
        sleep(3)
        self.displayTreeMenu()
        # 打开左边树选择供电单位
        self.driver = openLeftTree(para['ORG_NO'])
        # 文件类型
        self.inputSel_file_type(para['FILE_TYPE'])
        # 开始时间
        self.inputStr_start_date(para['START_DATE'])
        # 结束时间
        self.inputStr_end_date(para['END_DATE'])

        # 查询
        self.btn_qry()
        self.sleep_time(2)
        result = self.assert_context(*Knowledge_Locators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(NewsAnswer.para_Knowledge))
    def test_query(self, para):
        self.query(para)

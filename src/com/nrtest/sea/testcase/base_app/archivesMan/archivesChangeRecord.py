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
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_data import ArchivesMan_data
from com.nrtest.sea.pages.base_app.archivesMan.archivesChangeRecordPage import ArchivesChangeRecordPage, \
    ArchivesChangeRecordLocators
from com.nrtest.sea.task.commonMath import *


# 基本应用--》档案管理--》档案变更记录
@ddt
class TestArchivesChangeRecordPage(unittest.TestCase, ArchivesChangeRecordPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(ArchivesMan_data.archivesChangeRecord_para)
        sleep(2)
        cls.exec_script(cls, ArchivesChangeRecordLocators.START_DATE_JS)
        cls.exec_script(cls, ArchivesChangeRecordLocators.END_DATE_JS)

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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(ArchivesChangeRecordPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """
        # 点击低压
        self.btn_low()
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 选择设备类型
        self.inputSel_device_type(para['DEVICE_TYPE'])
        # 变更类型
        self.inputSel_change_type(para['CHANGE_TYPE'])
        # 开始时间
        self.inputStr_start_time(para['START_TIME'])
        # 结束时间
        self.inputStr_end_time(para['END_TIME'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesChangeRecordLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(ArchivesMan_data.archivesChangeRecord_para))
    def test_der(self, para):
        self.query(para)

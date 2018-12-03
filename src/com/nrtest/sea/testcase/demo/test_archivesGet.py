# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesGet.py
@time: 2018/11/28 0028 13:55
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_data import ArchivesMan_data
from com.nrtest.sea.pages.base_app.archivesMan.archivesGet_page import ArchivesGetPage
from com.nrtest.sea.task.commonMath import *


# 基本应用--》档案管理--》电表批量导出（冀北）
@ddt
class TestArchivesGetLocators(unittest.TestCase, ArchivesGetPage):

    # @classmethod
    # def setUpClass(cls):
    #     print("开始执行")
    #     # 打开菜单（需要传入对应的菜单编号）
    #     cls.driver = openMenu(ArchivesMan_data.archivesGet_para)

    # @classmethod
    # def tearDownClass(cls):
    #     print("执行结束")
    #     # 关闭菜单页面
    #     cls.closePages(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        self.driver = openMenu(ArchivesMan_data.archivesGet_para)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

        # 回收左边树
        self.recoverLeftTree()
        self.refreshPage()

    def query(self, para):
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        sleep(3)
        print(para['ORG_NO'])
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 输入用户类型
        self.inputSel_userType(para['USER_TYPE'])
        # 户号
        self.inputStr_userNO(para['USER_NO'])
        # 终端资产号
        self.inputStr_tmnlAssetNo(para['TMNL_ASSET_NO'])
        # 终端地址
        self.inputStr_tmnlAddr(para['TMNL_ADDR'])

        self.btn_qry()
        self.sleep_time(2)

    def checkValue(self, tst_case_id):
        self.assertTrue(self.commonAssertValue(tst_case_id))

    # @BeautifulReport.add_test_img()
    @data(*((DataAccess.getCaseData(ArchivesMan_data.archivesGet_para))))
    def test_query(self, para):
        """
        跳转验证
        :param para:
        :return:
        """
        print(para)
        self.query(para)
        self.checkValue(para['TST_CASE_ID'])

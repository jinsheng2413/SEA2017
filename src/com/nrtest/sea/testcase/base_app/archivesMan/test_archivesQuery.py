# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_archivesManage.py
@time: 2018/8/29 0029 14:26
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_para import ArchivesManData
from com.nrtest.sea.locators.base_app.archivesMan.archivesQuery_locators import ArchivesQuery_locators
from com.nrtest.sea.pages.base_app.archivesMan.archivesQuery_pages import ArchivesQueryPages
from com.nrtest.sea.task.commonMath import *


@ddt
class TestArchivesQuery(unittest.TestCase, ArchivesQueryPages):
    @classmethod
    def setUpClass(cls):
        print('开始执行')
        cls.driver = openMenu(ArchivesManData.para_archivesQuery)
        cls.sleep_time(cls, 2)
        cls.exec_script(cls, ArchivesQuery_locators.js)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        cls.refreshPage(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        """
        pass

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        """
        self.clear_values(ArchivesQueryPages)
        self.recoverLeftTree()

    def query(self, para):
        print(para)
        # 打开左边树并点击
        self.driver = openLeftTree(para['ORG_NO'])
        # 输入抄表段号
        self.inputStr_sect_no(para['SECT_NO'])
        # 选择用户类型
        self.inputCSel_cons_type(para['CONS_TYPE'])
        # 选择终端地址
        self.inputStr_tmnl_addr(para['TNML_ADDR'])
        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesQuery_locators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(ArchivesManData.para_archivesQuery))
    def test_query(self, para):
        # ljf getCaseData已处理Dict，此处不需要再转
        # self.query(Dict(para))
        self.query(para)

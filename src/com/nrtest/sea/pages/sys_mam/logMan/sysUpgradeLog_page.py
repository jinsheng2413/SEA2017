# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sysUpgradeLog_page.py
@time: 2018/11/30 10:56
@desc:
"""

from com.nrtest.common.base_page import Page

# 系统管理→日志管理→系统升级日志
class SysUpgradeLogPage(Page):
    # 版本类型
    def inputSel_version_type(self, options):
        self.selectDropDown(options)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)

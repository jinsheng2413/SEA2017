# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userDistributionStat_page.py
@time: 2018/11/13 14:33
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.sysUseStat.userDistributionStat_locators import *


# 系统管理→系统使用情况统计→用户分布情况统计
# 用户分布统计
class UserDistributionStatPage(Page):
    # 查询按钮
    def btn_qry(self):
        self.btn_query()

# 系统管理→系统使用情况统计→用户分布情况统计
# 注册用户明细
class UserRegisterDetailPage(Page):
    # 类型
    def inputSel_type(self, options):
        self.selectDropDown(options)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)

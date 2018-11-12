# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: simInstallStat_page.py
@time: 2018/11/9 0009 9:14
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.simCardMan.runSituationCount.simInstallStat_locators import SimInstallStatLocators



# 运行管理-->SIM卡管理-->运行情况分析-->安装情况统计
class SimInstallStatPage(Page):
    # 


    # 执行状态
    def inputSel_operator(self, name):
        self.click(*SimInstallStatLocators.QRY_OPERATOR)
        locator = self.get_select_locator(SimInstallStatLocators.QRY_OPERATOR_VALUE, name)
        self.click(*locator)



        # 查询
    def btn_qry(self):
            self.click(*SimInstallStatLocators.BTN_QRY)
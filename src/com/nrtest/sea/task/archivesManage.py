# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesManage.py
@time: 2018/8/28 0028 13:40
@desc:
"""

from com.nrtest.sea.locators.base_app.archivesMan.archivesMaintain_locators import ArchivesMaintain_locators
from com.nrtest.sea.locators.base_app.archivesMan.archivesManage_locators import ArchivesManage_locators
from com.nrtest.sea.pages.other.menu_page import MenuPage
# 档案管理
from com.nrtest.sea.task.login import Login


# 档案同步
def archivesMange():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = MenuPage(dr)
    # cp.menu_first(1)
    # cp.menu_second(1)
    # cp.menu_three(1)
    cp.btn_plus(1)
    cp.btn_company_plus(1)

    cp.btn_company_plus(3)
    cp.click(*ArchivesManage_locators.BTN_LG)

    return cp.driver


# 档案异常分析_统计
def archivesAnalysisOfAnomaly_count():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = MenuPage(dr)
    # cp.menu_first(1)
    # cp.menu_second(1)
    # cp.menu_three(2)
    cp.btn_plus(1)
    cp.btn_company_plus(1)
    cp.click(*ArchivesManage_locators.BTN_LG)
    js = "document.getElementsByTagName('input')[5].removeAttribute(\"readOnly\")"
    cp.exec_script(js)

    return cp.driver


# 档案异常分析_明细
def archivesAnalysisOfAnomaly_detail():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = MenuPage(dr)
    # cp.menu_first(1)
    # cp.menu_second(1)
    # cp.menu_three(2)
    cp.btn_plus(1)
    cp.btn_company_plus(1)
    cp.btn_company_plus(3)
    cp.click(*ArchivesManage_locators.BTN_MENU_ABNOLMAL_DETAIL)
    cp.click(*ArchivesManage_locators.BTN_LG_D)
    js = "document.getElementById('statDateDetail').removeAttribute(\"readOnly\")"
    cp.exec_script(js)

    return cp.driver


# 档案维护_厂站维护
def archivesMaintain_factory():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = MenuPage(dr)
    # cp.menu_first(1)
    # cp.menu_second(1)
    # cp.menu_three(3)
    cp.btn_plus(1)
    cp.btn_select_company(2)

    return cp.driver


# 档案维护_终端维护
def archivesMaintain_terminal():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = MenuPage(dr)
    # cp.menu_first(1)
    # cp.menu_second(1)
    # cp.menu_three(3)
    cp.click(*ArchivesMaintain_locators.BTN_MENU_TERMINAL_MAINTAIN)
    cp.btn_plus(1)
    cp.btn_select_company(4)

    return cp.driver


# 档案维护_电表维护
def archivesMaintain_meter():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = MenuPage(dr)
    # cp.menu_first(1)
    # cp.menu_second(1)
    # cp.menu_three(3)
    cp.click(*ArchivesMaintain_locators.BTN_MENU_METER_MAINTAIN)
    cp.btn_plus(1)
    cp.btn_select_company(2)

    return cp.driver


# 档案查询
def archivesQuery():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = MenuPage(dr)
    # cp.menu_first(1)
    # cp.menu_second(1)
    # cp.menu_three(4)
    cp.btn_plus(1)
    cp.btn_company_plus(1)
    cp.click(*ArchivesManage_locators.BTN_LG)
    js = "document.getElementsByName('consTypeCombox')[0].removeAttribute(\"readOnly\")"
    cp.exec_script(js)

    return cp.driver


if __name__ == '__main__':
    archivesQuery()

# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: loadRankAnalyse.py
@time: 2018/8/8 10:06
@desc:
"""
from com.nrtest.common.login import Login
from com.nrtest.sea.pages.other.common_page import Common_page


# 负荷排名分析
def loadrankanalyse():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = Common_page(dr)
    cp.btn_statrey()
    # 点击数据分析
    cp.btn_dataanalyse()
    cp.hover_loadanalyse()
    cp.btn_loadanalyse_rank()
    # js ="document.getElementsByTagName('input')[5].removeAttribute(\"readOnly\");"
    # cp.exec_script(js)
    # js = "document.getElementsByTagName('input')[6].removeAttribute(\"readOnly\");"
    # cp.exec_script(js)
    # cp.input('vsd',*(By.XPATH,"//div[@class=\"x-form-item \"]//label[contains(text(),'开始日期')]/../div[1]/div/input"))
    #

    return cp.driver


if __name__ == '__main__':
    loadrankanalyse()

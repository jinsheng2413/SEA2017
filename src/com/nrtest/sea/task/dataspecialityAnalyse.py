# -*- coding: utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: dataspecialityAnalyse.py
@time: 2018/8/15 14:26
@desc:
"""
from com.nrtest.sea.pages.other.common_page import Common_page
from com.nrtest.sea.task.login import Login


def dataspecialityanalyse():
    lg = Login()
    dr = lg.login()
    # 点击统计查询
    cp = Common_page(dr)
    cp.btn_statrey()
    # 点击数据分析
    cp.btn_dataanalyse()
    cp.hover_loadanalyse()
    cp.btn_load_speciality_analyse()

    return cp.driver


if __name__ == '__main__':
    dataspecialityanalyse()

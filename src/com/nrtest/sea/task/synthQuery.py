# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: test_userDataQuery.py
@time: 2018/8/13 0002 09:50
'''

from com.nrtest.sea.task.login import Login
from com.nrtest.common.setting import Setting
from com.nrtest.sea.pages.other.common_page import Common_page

#统计查询→综合查询→用户数据查询
def UserDataQueryLog():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    udq = Common_page(dr)
    #点击统计查询
    udq.btn_stat_rey()
    #点击综合查询
    udq.btn_synthquery()
    #点击用户数据查询
    udq.btn_userdataquery()
    return udq.driver

#统计查询→综合查询→用户数据查询
def TerminalDataQueryLog():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    tdq = Common_page(dr)
    # 点击统计查询
    tdq.btn_stat_rey()
    # 点击综合查询
    tdq.btn_synthquery()
    # 点击终端数据查询
    tdq.btn_terminaldataquery()
    return tdq.driver

#统计查询→综合查询→配变数据查询
def PublicDataQueryLog():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    pdq = Common_page(dr)
    # 点击统计查询
    pdq.btn_stat_rey()
    # 点击综合查询
    pdq.btn_synthquery()
    # 点击配变数据查询
    pdq.btn_publicdataquery()
    return pdq.driver

# 统计查询→综合查询→线路数据查询
def LineDataQueryLog():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    ldq = Common_page(dr)
    # 点击统计查询
    ldq.btn_stat_rey()
    # 点击综合查询
    ldq.btn_synthquery()
    # 点击线路数据查询
    ldq.btn_linedataquery()
    return ldq.driver

if __name__=='__main__':
 LineDataQueryLog()
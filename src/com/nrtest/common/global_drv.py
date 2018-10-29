# -*- coding:utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: global_drv.py
@time: 2018-09-10 18:30
@desc:
"""

from com.nrtest.common.setting import Setting
from com.nrtest.sea.task.login import Login

global driver


def __init():
    """
    初始化webdriver
    """
    global __driver
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    __driver = lg.login()

    print('complete global webdriver init.')


def get_driver():
    """
    :return: 获得一个全局webdriver,不存在则初始化并返回
    """
    try:
        return __driver
    except Exception as e:
        print(e)
        __init()
        return __driver


def quit():
    """
    关闭全局webdriver
    """
    print('closing global webdriver')
    __driver.quit()
    print('closed global webdriver')

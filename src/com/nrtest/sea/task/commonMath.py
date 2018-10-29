# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commonMath.py
@time: 2018/9/10 0010 10:59
@desc:
"""
from selenium.webdriver.common.by import By

from com.nrtest.common import global_drv
from com.nrtest.sea.pages.other.menu_page import MenuPage


def openMenu(menuNo, byName=False):
    """
    打开指定菜单页面
    :param menuNo: 菜单编号
    :param byName:
    :return:
    """
    p = MenuPage(global_drv.get_driver())
    p.click_menu(menuNo, byName)
    return p.driver


def openLeftTree(treeNo):
    """
    打开左边树
    :param treeNo:
    :return:
    """
    p = MenuPage(global_drv.get_driver())
    p.btn_left_tree(treeNo)
    return p.driver


def clickTabPage(name):
    """
    打开Tab页
    :param name:
    """
    p = MenuPage(global_drv.get_driver())
    locators = (By.XPATH, "(//*[@class=\"x-tab-strip-text \"])[text()='{0}']".format(name))
    print(locators)
    p.click(*locators)
    # return p.driver


if __name__ == "__main__":
    pass

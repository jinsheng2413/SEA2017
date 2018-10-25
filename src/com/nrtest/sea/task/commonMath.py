# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commonMath.py
@time: 2018/9/10 0010 10:59
@desc:
'''
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.common import global_drv
from selenium.webdriver.common.by import By
from time import sleep

# 打开
def openMenu(menuNo,byName=False):
    p = MenuPage(global_drv.get_driver())
    p.click_menu(menuNo,byName)
    return p.driver

    # 打开左边树


def openLeftTree(treeNo):
    p = MenuPage(global_drv.get_driver())
    p.btn_left_tree(treeNo)
    return p.driver

# 打开
def clickTabPage(name):
    p = MenuPage(global_drv.get_driver())
    locators = (By.XPATH, "(//*[@class=\"x-tab-strip-text \"])[text()='{0}']".format(name))
    print(locators)
    p.click(*locators)
    return p.driver

if __name__=="__main__":

    pass

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

# 打开
def openMenu(menuNo):
    p = MenuPage(global_drv.get_driver())
    p.click_menu(menuNo)
    return p.driver

    # 打开左边树


def openLeftTree(treeNo):
    p = MenuPage(global_drv.get_driver())
    p.btn_left_tree(treeNo)
    return p.driver
if __name__=="__main__":

    openMenu('99922120')
# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_locators.py
@time: 2018/8/28 0028 13:45
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.setting import Setting
from com.nrtest.sea.data.base_app.archivesMan.archivesAnalysisOfAnomaly_para import ArchivesAnalysisOfAnomaly_para
from com.nrtest.sea.locators.other.menu_locators import MenuLocators
from com.nrtest.sea.task.commonMath import *
from com.nrtest.sea.task.login import Login


class MenuPage(Page):
    # click_menu(ArchivesAnalysisOfAnomaly_para(1))

    def click_menu(self, menu_no, by_name=False):
        """
        定位级菜单element,并调用Base_Page类的click方法选择级菜单
        :param menu_no: 菜单编号
        :param by_name: True-按菜单名定位；False-按菜单坐标定位
        :return: 返回driver
        """

        #按菜单名定位菜单
        if (by_name):
            self.click_menu_by_name(menu_no);
            return self.driver

        # 静态函数可以直接调用，不需要实例化
        # kl = DataAccess()
        # coordinate = kl.getMenu(menu_no)
        coordinate = DataAccess.getMenu(menu_no, by_name)

        items = coordinate.split(';')
        l = len(items)
        for i in range(len(items)):
            locators = getattr(MenuLocators, 'MENU_LEVEL_IDX_' + str(i + 1))
            idx = int(items[i])
            # if i == 0:
            idx = idx + 1 if i == 0 else idx
            loc = (locators[0], locators[1] % idx)
            if (l == 4 and i == 2) or (l == 5 and i in (2, 3)):
                # pg = Page  #无效代码  ljf  2018-10-24
                self.hover(*loc)
            else:
                self.click(*loc)
        return self.driver

    def click_menu_by_name(self, menu_no, isPath=False):
        """
        定位级菜单element,并调用Base_Page类的click方法选择级菜单
        :param menu_no: 菜单编号
        :param isPath: True-menu_no是已确定的菜单路径，False-menu_no是菜单编码
        :return:各级菜单名，如：基本应用;档案管理;档案同步  一级菜单下第一个菜单下的第二个子菜单
        """
        menu_path = menu_no if isPath else DataAccess.getMenu(menu_no, True)
        print('菜单路径：', menu_path)
        items = menu_path.split(';')

        l = len(items)
        for i in range(len(items)):
            locators = getattr(MenuLocators, 'MENU_LEVEL' + str(i + 1))
            loc = (locators[0], locators[1] % items[i])
            if (l == 4 and i == 2) or (l == 5 and i in (2, 3)):
                # print('hover loc is ', loc)
                self.hover(*loc)
            else:
                # print('click loc is ', loc)
                self.click(*loc)
        return self.driver

    # 左边树
    def btn_plus(self, index):
        locator = self.get_select_locator(MenuLocators.BTN_LEFT_PLUS, index)
        self.click(*locator)

    def btn_company_plus(self, index):
        locator = self.get_select_locator(MenuLocators.BTN_COMPANY_PLUS, index)
        print(locator)
        self.click(*locator)

    # 选中省份
    def btn_select_province(self):
        self.click(*MenuLocators.BTN_LEFT_MENU_ELETRIC)

    # 选择公司
    def btn_select_company(self, number):
        nb = number + 1
        lr = self.get_select_locator(MenuLocators.BTN_COMPANY, nb)
        self.click(*lr)

        # 点击双向箭头

    def btn_left_arrow(self):
        self.click(*MenuLocators.BTN_LEFT_MENU)

    # 选择县

    def btn_select_county(self, index):
        lr = self.get_select_locator(MenuLocators.BTN_COUNTY, index)
        self.click(*lr)

    def page_assert_body(self):
        op = self.assert_body('电网结构')
        return op

    # 选择所

    def btn_select_user(self, index):
        lr = self.get_select_locator(MenuLocators.BTN_COUNTY_AND_USER, index)
        self.click(*lr)

    def btn_suitable_arrow(self):
        hp = self.page_assert_body()
        if hp == True:
            print('------------------------------------')
        elif hp == False:
            self.btn_left_arrow()

        else:
            print('省份选择错误')

    # 选择左边树

    def btn_left_tree(self, tree_no):
        kl = DataAccess()
        tree = kl.getLeftTree(tree_no)

        # self.btn_suitable_arrow()
        items = tree.split(';')
        l = len(items)

        if l is 2:
            self.btn_plus(1)
            self.btn_select_company(int(items[1]))
            print(int(items[1]))
        elif l in (3, 4):
            self.btn_plus(1)
            if int(items[1]) is 5:
                self.btn_plus(1)
            else:
                self.btn_company_plus(items[1])
            if l is 3:
                self.btn_select_county(int(items[2]) + 1)
            else:
                self.btn_company_plus(int(items[2]) + int(items[1]))
                self.btn_select_user(int(items[3]) + 1)
        elif l is 1:
            self.btn_select_province()

        return self.driver

    def clickLeftTree(self, tree):
        tree = tree.split(';')
        self.btn_plus(1)
        self.btn_company_plus(list[0])
        self.btn_company_plus(list[1])

    def getAssert(self, num):
        self.get_select_locator(MenuLocators.TAB_ONE, num)

    def getSecondAssert(self, num):
        self.get_select_locator(MenuLocators.TAB_TWO, num)

    def clickAllMenu(self):
        menus = DataAccess.getAllMenu()
        l = len(menus)
        for i in range(len(menus)):
            print('即将定位该菜单：', menus[i])
            try:
                self.click_menu_by_name(menus[i][2], True)
            except:
                print('该菜单定位报错：', menus[i])

if __name__ == '__main__':
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    p = MenuPage(lg.login())
    #p.click_menu('99913210', True) #'99913210', True)
    #p.clickTabPage('采集成功率统计')
    p.clickAllMenu()


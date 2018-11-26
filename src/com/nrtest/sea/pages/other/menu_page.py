# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_locators.py
@time: 2018/8/28 0028 13:45
@desc:
"""
from time import sleep

from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.setting import Setting
from com.nrtest.sea.locators.other.menu_locators import MenuLocators
from com.nrtest.sea.task.login import Login


class MenuPage(Page):
    def click_menu(self, menu_no, by_name=True):
        """
        定位级菜单element,并调用Base_Page类的click方法选择级菜单
        :param menu_no: 菜单编号
        :param by_name: True-按菜单名定位；False-按菜单坐标定位
        :return: 返回driver
        """

        # 按菜单名定位菜单
        if by_name:
            self.click_menu_by_name(menu_no)
            return self.driver

        coordinate = DataAccess.getMenu(menu_no, by_name)
        items = coordinate.split(';')
        l = len(items)
        for i in range(len(items)):
            locators = getattr(MenuLocators, 'MENU_LEVEL_IDX_' + str(i + 1))
            idx = int(items[i])
            idx = idx + 1 if i == 0 else idx
            loc = (locators[0], locators[1] % idx)
            if (l == 4 and i == 2) or (l == 5 and i in (2, 3)):
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
                self.hover(*loc)
            else:
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

    def btn_select_province(self):
        """
        选择省份
        """
        self.click(*MenuLocators.BTN_LEFT_MENU_ELETRIC)

    def btn_select_company(self, number):
        """
        选择公司
        :param number:
        """
        nb = number + 1
        lr = self.get_select_locator(MenuLocators.BTN_COMPANY, nb)
        self.click(*lr)

    def btn_left_arrow(self):
        """
        点击双向箭头
        """
        self.click(*MenuLocators.BTN_LEFT_MENU)

    def btn_select_county(self, index):
        """
        选择县
        :param index:
        """
        lr = self.get_select_locator(MenuLocators.BTN_COUNTY, index)
        self.click(*lr)

    def page_assert_body(self):
        op = self.assert_body('电网结构')
        return op

    def btn_select_user(self, index):
        """
        选供电所
        :param index:
        """
        lr = self.get_select_locator(MenuLocators.BTN_COUNTY_AND_USER, index)
        self.click(*lr)

    def btn_suitable_arrow(self):
        hp = self.page_assert_body()
        if hp is True:
            print('------------------------------------')
        elif hp is False:
            self.btn_left_arrow()
        else:
            print('省份选择错误')

    # 选择左边树
    def btn_left_tree(self, tree_no):
        tree = DataAccess.getLeftTree(tree_no)

        # self.btn_suitable_arrow()
        items = tree.split(';')
        l = len(items)

        if l == 2:
            self.btn_plus(1)
            self.btn_select_company(int(items[1]))
            print(int(items[1]))
        elif l in (3, 4):
            self.btn_plus(1)
            if int(items[1]) == 5:
                self.btn_plus(1)
            else:
                self.btn_company_plus(items[1])
            if l == 3:
                self.btn_select_county(int(items[2]) + 1)
            else:
                self.btn_company_plus(int(items[2]) + int(items[1]))
                self.btn_select_user(int(items[3]) + 1)
        elif l == 1:
            self.btn_select_province()

        return self.driver

    def btn_user_nodes(self, node_flag, node_value):
        """
        选择左边树用户Tab页面，并根据节点类型，输入并查询相应结果
        :param node_flag: 节点分类
        :param node_value: 节点值
        """
        # 定位左边树用户Tab页@todo 请完善选择用户Tab的xpath
        # self.click()

        # 根据node_flag选择相应的节点查询条件xpath，并输入查询条件
        xpath = None
        if node_flag == '02':  # 节点--用户编号
            xpath = MenuLocators.NODE_CONS_NO
        elif node_flag == '03':  # 节点--终端逻辑地址
            xpath = MenuLocators.NODE_TMNL_ADDR
        elif node_flag == '04':  # 节点--电能表资产
            xpath = MenuLocators.NODE_METER_ASSERT_NO
        self.input(node_value, *xpath)

        # 点击查询按钮
        self.click(MenuLocators.USER_TAB_BTN_QRY)

        # 等待查询结果，最好通过其他途径判断查询已返回
        sleep(3)

        # 定位查询结果，默认选择第一行记录
        # @TODO 是否需要格式化xpath根据实际情况定
        xpath = self.format_xpath(MenuLocators.NODE_USER_TAB_RSLT, node_value)
        self.click(xpath)

    # def clickLeftTree(self, tree):
    #     tree = tree.split(';')
    #     self.btn_plus(1)
    #     self.btn_company_plus(list[0])
    #     self.btn_company_plus(list[1])



    def clickAllMenu(self):
        menus = DataAccess.getAllMenu()
        # menus = [('999246000', '台区线损监测', 'advAppIcon;线损分析;线损统计分析;台区线损监测')]
        l = len(menus)
        for i in range(len(menus)):
            try:
                menu = menus[i]
                print('即将定位该菜单：', menu)
                self.click_menu_by_name(menu[2], True)
                sleep(1)
                self.closePages(menu[1])
            except Exception as e:
                print('该菜单定位报错：', menu, e)


if __name__ == '__main__':
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    p = MenuPage(lg.login())
    # p.click_menu('99913210', True) #'99913210', True)
    # p.clickTabPage('采集成功率统计')
    p.clickAllMenu()

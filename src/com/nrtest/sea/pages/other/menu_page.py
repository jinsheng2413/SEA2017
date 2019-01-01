# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_locators.py
@time: 2018/8/28 0028 13:45
@desc:
"""
from time import sleep

from com.nrtest.common import global_drv
from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.locators.other.menu_locators import MenuLocators
from com.nrtest.sea.task.login import Login


class MenuPage(Page):
    # def click_menu(self, menu_no, by_name=True):
    #     """
    #     定位级菜单element,并调用Base_Page类的click方法选择级菜单
    #     :param menu_no: 菜单编号
    #     :param by_name: True-按菜单名定位；False-按菜单坐标定位
    #     :return: 返回driver
    #     """
    #
    #     # 按菜单名定位菜单
    #     if by_name:
    #         self.click_menu(menu_no)
    #         return self.driver
    #
    #     coordinate = DataAccess.getMenu(menu_no, by_name)
    #     items = coordinate.split(';')
    #     l = len(items)
    #     for i in range(len(items)):
    #         locators = getattr(MenuLocators, 'MENU_LEVEL_IDX_' + str(i + 1))
    #         idx = int(items[i])
    #         idx = idx + 1 if i == 0 else idx
    #         loc = (locators[0], locators[1] % idx)
    #         if (l == 4 and i == 2) or (l == 5 and i in (2, 3)):
    #             self.hover(*loc)
    #         else:
    #             self.click(loc)
    #     return self.driver

    @staticmethod
    def openMenu(menuNo):
        """
        打开指定菜单页面
        :param menuNo: 菜单编号
        :return:
        """
        menuPage = MenuPage(global_drv.get_driver())
        menuPage.click_menu(menuNo)
        return menuPage

    def click_menu(self, menu_no, isPath=False):
        """
        定位级菜单element,并调用Base_Page类的click方法选择级菜单
        :param menu_no: 菜单编号
        :param isPath: True-menu_no是已确定的菜单路径，False-menu_no是菜单编码
        :return:各级菜单名，如：基本应用;档案管理;档案同步  一级菜单下第一个菜单下的第二个子菜单
        """
        menu_path = menu_no if isPath else DataAccess.getMenu(menu_no)
        print('菜单路径：', menu_path)
        items = menu_path.split(';')

        # 当前菜单名
        self.menu_name = items[-1]

        # 当菜单已打开已打开时不再重新打开
        if not self.exists_menu:
            item_cnt = len(items)
            for i in range(item_cnt):
                locators = getattr(MenuLocators, 'MENU_LEVEL' + str(i + 1))
                loc = (locators[0], locators[1] % items[i])
                if (item_cnt == 4 and i == 2) or (item_cnt == 5 and i in (2, 3)):
                    self.hover(loc)
                else:
                    self.click(loc)

        return self.driver

    # 左边树
    def btn_plus(self, index):
        locator = self.get_select_locator(MenuLocators.BTN_LEFT_PLUS, index)
        self.click(locator)

    def btn_company_plus(self, index):
        locator = self.get_select_locator(MenuLocators.BTN_COMPANY_PLUS, index)
        print(locator)
        self.click(locator)

    def btn_select_province(self):
        """
        选择省份
        """
        self.click(MenuLocators.BTN_LEFT_MENU_ELETRIC)

    def btn_select_company(self, number):
        """
        选择公司
        :param number:
        """
        nb = number + 1
        lr = self.get_select_locator(MenuLocators.BTN_COMPANY, nb)
        self.click(lr)

    def btn_left_arrow(self):
        """
        点击双向箭头
        """
        self.click(MenuLocators.BTN_LEFT_MENU)

    def btn_select_county(self, index):
        """
        选择县
        :param index:
        """
        lr = self.get_select_locator(MenuLocators.BTN_COUNTY, index)
        self.click(lr)

    def page_assert_body(self):
        op = self.assert_body('电网结构')
        return op

    def btn_select_user(self, index):
        """
        选供电所
        :param index:
        """
        lr = self.get_select_locator(MenuLocators.BTN_COUNTY_AND_USER, index)
        self.click(lr)

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
            self.btn_plus(1)#点击省公司加号
            if int(items[1]) == 5:#承德供电公司的加号xpath与前4个有所区别需要做特殊处理
                self.btn_plus(1)
            else:
                self.waitLeftTree()
                self.btn_company_plus(items[1])
            if l == 3:
                self.waitLeftTree()
                self.btn_select_county(int(items[2]) + 1) #点击公司加号
            else:
                self.waitLeftTree()
                self.btn_company_plus(int(items[2]) + int(items[1]))#点击公司加号
                self.btn_select_user(int(items[3]) + 1)
        elif l == 1:
            self.btn_select_province()

        return self.driver

    def btn_user_nodes(self, node_flag, node_value,number=1):

        """
        选择左边树用户Tab页面，并根据节点类型，输入并查询相应结果
        :param node_flag: 节点分类
        :param node_value: 节点值
        :param number:查询结果显示的区域，number：代表第几个行，默认是1

        """
        # 根据node_flag选择相应的节点查询条件xpath，并输入查询条件
        #{02:代表用户编号，03：代表终端逻辑地址，04：电能表资产号}

        # 点击用户标签页
        self.click(MenuLocators.NODE_USER)
        self.input(node_value, *MenuLocators.NODE[node_flag])

        # 点击查询按钮
        self.click(MenuLocators.USER_TAB_BTN_QRY)

        # 等待查询结果，最好通过其他途径判断查询已返回
        self.commonWait(MenuLocators.NODE_USER_TAB_RSLT_DEFAULT)
        self.clear(MenuLocators.NODE[node_flag])


        # 定位查询结果，默认选择第一行记录
        xpath = self.format_xpath(MenuLocators.NODE_USER_TAB_RSLT, number)
        print(xpath)

        self.click(xpath)
        print('------------')

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
                self.click_menu(menu[2], True)
                sleep(1)
                self.closePages(menu[1])
            except Exception as e:
                print('该菜单定位报错：', menu, e)


if __name__ == '__main__':
    login = Login()
    menuPage = MenuPage(login.login())
    #
    # # menuPage.click_menu('99913210', True) #'99913210')
    # # menuPage.clickTabPage('采集成功率统计')
    # menuPage.clickAllMenu()

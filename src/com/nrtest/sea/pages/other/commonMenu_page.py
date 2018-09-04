# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commonMenu_locators.py
@time: 2018/8/28 0028 13:45
@desc:
'''

from com.nrtest.sea.locators.other.commonMenu_locators import CommonMenu_locators
from com.nrtest.common.base_page import Page
class CommonMenu_page(Page):
    #一级菜单
    def menu_first(self,index):
        index = index + 1
        locator = self.get_select_locator(CommonMenu_locators.MENU_FIRST, index)
        self.click(*locator)


    #二级菜单
    def menu_second(self,index):
        locator = self.get_select_locator(CommonMenu_locators.MENU_SECOND, index)
        self.click(*locator)


    #三级菜单
    def menu_three(self,index):
        locator = self.get_select_locator(CommonMenu_locators.MENU_THREE, index)
        self.click(*locator)

    #悬停三级菜单
    def hover_menu(self,index):
        locator = self.get_select_locator(CommonMenu_locators.MENU_THREE, index)
        self.hover(*locator)


    # 【左边树】
    def btn_plus(self,index):
        locator = self.get_select_locator(CommonMenu_locators.BTN_LEFT_PLUS, index)
        self.click(*locator)

    def btn_company_plus(self, index):
        locator = self.get_select_locator(CommonMenu_locators.BTN_COMPANY_PLUS, index)
        self.click(*locator)

    # 选中省份
    def btn_select_province(self):
        self.click(*CommonMenu_locators.BTN_LEFT_MENU_ELETRIC)

    # 选择公司
    def btn_select_company(self, number):
        nb = number+1
        lr = self.get_select_locator(CommonMenu_locators.BTN_COMPANY,nb)
        self.click(*lr)

    #点击双向箭头
    def btn_left_arrow(self):
        self.click(*CommonMenu_locators.BTN_LEFT_MENU)

    # 选择县
    def btn_select_county(self,index):
        lr = self.get_select_locator(CommonMenu_locators.BTN_COUNTY,index)
        self.click(*lr)

    def page_assert_body(self):
        op = self.assert_body('电网结构')
        return op

    #选择用户
    def btn_select_user(self,index1,index2):

        lr = self.get_select_locator(CommonMenu_locators.BTN_COUNTY, index1)
        lr2 = (lr[0],lr[1]+'/ul/li['+str(index2)+']')
        print(lr2)

        self.click(*lr2)



    def btn_suitable_arrow(self):

        hp = self.page_assert_body()
        if hp == True:
            print('------------------------------------')
        elif hp == False:
            self.btn_left_arrow()

        else:
            print('省份选择错误')




    #选择左边树
    def btn_left_tree(self,num,list):
        self.btn_suitable_arrow()
        #市作为第一层
        if num is 1:
           self.btn_plus(1)
           self.btn_select_company(list[0])
        # 县作为第二层
        elif num is 2:
            self.btn_plus(1)
            self.btn_company_plus(list[0])
            self.btn_select_county(list[1])
        # 用户作为第三层
        elif num is 3:
            self.btn_plus(1)
            self.btn_company_plus(list[0])
            self.btn_company_plus(list[1])
            self.btn_select_user(list[1],list[2])
        elif num is 0:
            self.btn_select_province()

    #菜单
    def btn_select_menu(self,menu):
        self.menu_first(menu[0])
        self.menu_second(menu[1])
        self.menu_three(menu[2])


    #菜单
    def btn_hover_select_menu(self,menu):
        self.menu_first(menu[0])
        self.menu_second(menu[1])
        self.hover_menu(menu[2])


    def getAssert(self,num):
        self.get_select_locator(CommonMenu_locators.TAB_ONE,num)

    def getSecondAssert(self,num):
        self.get_select_locator(CommonMenu_locators.TAB_TWO, num)




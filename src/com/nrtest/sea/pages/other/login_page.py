# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: login_page.py
@time: 2018/5/27 0027 9:01
@desc:
'''
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.other.login_page_locators import LoginPageLocators


class LoginPage(Page):
    # 输入用户名
    def input_username(self, username):
        self.input(username, *LoginPageLocators.QRY_USERNAME)

    # 输入密码
    def input_password(self, password):
        self.input(password, *LoginPageLocators.QRY_PASSWWORD)

    # 输入验证码
    def input_identifying(self, code):
        self.input(code, *LoginPageLocators.INPUT_IDENTIFYING)

    # 点击登录按钮
    def btn_login(self):
        self.click(*LoginPageLocators.BTN_LOGIN)

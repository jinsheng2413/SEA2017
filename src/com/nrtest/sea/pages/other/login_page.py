# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: login_page.py
@time: 2018/5/27 0027 9:01
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.other.login_locators import *


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        if self.project_no == 'SEA':
            self.locator_class = LoginLocators
        elif self.project_no == 'SEA2.0':
            self.locator_class = LoginSEA20Locators
        elif self.project_no in (['D5000', 'PBS5000']):
            self.locator_class = LoginPBSLocators
        elif self.project_no.endswith('JLZDH'):
            self.locator_class = LoginJLZDHLocators

    # 输入用户名
    def input_username(self, username):
        self.input(username, *self.locator_class.QRY_USERNAME)

    # 输入密码
    def input_password(self, password):
        self.input(password, *self.locator_class.QRY_PASSWORD)

    # 输入验证码
    def input_identifying(self, code):
        self.input(code, *self.locator_class.INPUT_IDENTIFYING)

    # 点击登录按钮
    def btn_login(self):
        self.click(self.locator_class.BTN_LOGIN)

    # 等待登录按钮可点击
    def waitFor(self, seconds=5):
        self._element_ec_mode(self.locator_class.BTN_LOGIN, seconds)

    def is_login_success(self):
        """
        根据特殊标签，确认登录是否成功 还在登录界面则表示登录不成功
        :return: True-登录成功；False-登录失败
        """
        return not bool(self._direct_find_element(self.locator_class.QRY_USERNAME))

    def refresh_valid_mask(self):
        """
        刷新验证码
        """
        self.click(self.locator_class.BTN_IDENTIFYING_CODE)

    def clean_screen(self):
        """
        登录成功失败判断与清屏处理（如，告警提示框等）
        """
        # 登录异常弹窗确认
        el = self._find_displayed_element(self.locator_class.BTN_CONFIRM)
        if bool(el):
            el.click()
        super().clean_screen(self.locator_class)

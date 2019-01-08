# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: login_page.py
@time: 2018/5/27 0027 9:01
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.other.login_locators import LoginLocators

class LoginPage(Page):
    # 输入用户名
    def input_username(self, username):
        self.input(username, *LoginLocators.QRY_USERNAME)

    # 输入密码
    def input_password(self, password):
        self.input(password, *LoginLocators.QRY_PASSWWORD)

    # 输入验证码
    def input_identifying(self, code):
        self.input(code, *LoginLocators.INPUT_IDENTIFYING)

    # 点击登录按钮
    def btn_login(self):
        self.click(LoginLocators.BTN_LOGIN)

    # 等待验证码可点击
    # def waitForMask(self):
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(LoginLocators.BTN_IDENTIFYING_CODE))

    def is_login_success(self):
        """
        根据特殊标签，确认登录是否成功
        :return:
        """
        return bool(self._find_element(LoginLocators.LOGIN_SUCCESS, ec_mode=1))

    def refresh_valid_mask(self):
        """
        刷新验证码
        """
        self.click(LoginLocators.BTN_IDENTIFYING_CODE)

    def clean_screen(self):
        """
        登录成功失败判断与清屏处理（如，告警提示框等）
        :param driver:
        """
        con = self.find_element_by_tag_name('body').text
        if '重要信息推出' in con:
            if '登录异常' in con:
                self._find_element(LoginLocators.BTN_CONFIRM).click()
            if '账号异常信息' in con:
                self._find_element(LoginLocators.BTN_ARROW).click()

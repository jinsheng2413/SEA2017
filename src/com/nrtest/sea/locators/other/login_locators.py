# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: login_page_locators.py
@time: 2018/5/27 0027 8:47
@desc:
"""
from selenium.webdriver.common.by import By


class LoginLocators:
    # 【输入框】
    # -->用户名
    QRY_USERNAME = (By.XPATH, '//input[@id="staffNo_input"]')

    # -->密码
    QRY_PASSWORD = (By.XPATH, '//input[@id="password_input"]')

    # -->验证码
    INPUT_IDENTIFYING = (By.XPATH, '//input[@id="checkcode_input"]')


    # 【操作区】
    # -->登录按钮
    BTN_LOGIN = (By.XPATH, '//img[@src="./images/loginbutton.png"]')

    # 验证码刷新按钮
    BTN_IDENTIFYING_CODE = (By.XPATH, '//*[@id="imageMask"]')

    # 登录异常弹窗确认
    BTN_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')

    # 账号异常信息弹窗确认
    DLG_EXCEPT = (By.XPATH, '//div[@id="index.loginExceptionWin"]//div[contains(@class, "x-tool-close")]')
    # $x('//div[@id="index.loginExceptionWin"]//div[@class="x-tool x-tool-close "]')

    # 重要信息推出窗口关闭
    DLG_IMPORT = (By.XPATH, '//button[contains(text(), "不再提醒")]')


class LoginPBSLocators:
    # 【输入框】
    # -->用户名
    QRY_USERNAME = (By.XPATH, '//input[@id="nameLogin"]')

    # -->密码
    QRY_PASSWORD = (By.XPATH, '//input[@id="passwordLogin"]')

    # -->验证码
    # INPUT_IDENTIFYING = (By.XPATH, '//input[@id="checkcode_input"]')

    # 【操作区】
    # -->登录按钮
    BTN_LOGIN = (By.XPATH, '//button[@id="buttonLogin"]')

    # 验证码刷新按钮
    # BTN_IDENTIFYING_CODE = (By.XPATH, '//*[@id="imageMask"]')

    # # 登录异常弹窗确认
    # BTN_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')
    #
    # # 账号异常信息弹窗确认
    # DLG_EXCEPT = (By.XPATH, '//div[@id="index.loginExceptionWin"]//div[contains(@class, "x-tool-close")]')
    # # $x('//div[@id="index.loginExceptionWin"]//div[@class="x-tool x-tool-close "]')
    #
    # # 重要信息推出窗口关闭
    # DLG_IMPORT = (By.XPATH, '//button[contains(text(), "不再提醒")]')


class LoginSEA20Locators:
    # 【输入框】
    # -->用户名
    QRY_USERNAME = (By.XPATH, '//input[@id="staffNo_input"]')

    # -->密码
    QRY_PASSWORD = (By.XPATH, '//input[@id="password_input"]')

    # -->验证码
    INPUT_IDENTIFYING = (By.XPATH, '//input[@id="checkcode_input"]')

    # 【操作区】
    # -->登录按钮
    BTN_LOGIN = (By.XPATH, '//img[@src="./images/loginbutton.png"]')

    # 验证码刷新按钮
    BTN_IDENTIFYING_CODE = (By.XPATH, '//*[@id="imageMask"]')

    # 登录异常弹窗确认
    BTN_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')

    # 账号异常信息弹窗确认
    DLG_EXCEPT = (By.XPATH, '//div[@id="index.loginExceptionWin"]//div[contains(@class, "x-tool-close")]')
    # $x('//div[@id="index.loginExceptionWin"]//div[@class="x-tool x-tool-close "]')

    # 重要信息推出窗口关闭
    DLG_IMPORT = (By.XPATH, '//button[contains(text(), "不再提醒")]')


class LoginJLZDHLocators:
    # 【输入框】
    # -->用户名
    QRY_USERNAME = (By.XPATH, '//input[@id="staffNo_input"]')

    # -->密码
    QRY_PASSWORD = (By.XPATH, '//input[@id="password_input"]')

    # -->验证码
    INPUT_IDENTIFYING = (By.XPATH, '//input[@id="checkcode_input"]')

    # 【操作区】
    # -->登录按钮
    BTN_LOGIN = (By.XPATH, '//img[@src="./images/loginbutton.png"]')

    # 验证码刷新按钮
    BTN_IDENTIFYING_CODE = (By.XPATH, '//*[@id="imageMask"]')

    # 登录异常弹窗确认
    BTN_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')

    # 账号异常信息弹窗确认
    DLG_EXCEPT = (By.XPATH, '//div[@id="index.loginExceptionWin"]//div[contains(@class, "x-tool-close")]')
    # $x('//div[@id="index.loginExceptionWin"]//div[@class="x-tool x-tool-close "]')

    # 重要信息推出窗口关闭
    DLG_IMPORT = (By.XPATH, '//button[contains(text(), "不再提醒")]')
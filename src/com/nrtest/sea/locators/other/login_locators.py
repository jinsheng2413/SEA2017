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

    # 登陆页弹出的tip对话框
    TIP = (By.XPATH, '//a[@class="astyle" and text()="关闭"]')
    #     $x('//div[@id="notice" and starts-with(@style, "display: block;")]//a[@class="astyle" and text()="关闭"]')
    # div id="notice"  style="display: none;


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


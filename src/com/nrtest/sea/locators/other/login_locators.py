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
    # 国网标设
    QRY_USERNAME = (By.XPATH, '//input[@id="staffNo_input"]')
    # 电量PBS5000
    # QRY_USERNAME = (By.XPATH, '//input[@id="nameLogin"]')

    # -->密码
    # 国网标设
    QRY_PASSWWORD = (By.XPATH, '//input[@id="password_input"]')
    # 电量PBS5000
    # QRY_PASSWWORD = (By.XPATH, '//input[@id="passwordLogin"]')

    # -->验证码
    INPUT_IDENTIFYING = (By.XPATH, '//input[@id="checkcode_input"]')


    # 【操作区】
    # -->登录按钮
    # 国网标设
    BTN_LOGIN = (By.XPATH, '//img[@src="./images/loginbutton.png"]')
    # 电量PBS5000
    # BTN_LOGIN = (By.XPATH, '//button[@id="buttonLogin"]')

    # 验证码刷新按钮
    BTN_IDENTIFYING_CODE = (By.XPATH, '//*[@id="imageMask"]')

    # 登录异常弹窗确认
    BTN_CONFIRM = (By.XPATH, "//button[contains(.,'确定')]")

    # 账号异常信息弹窗确认
    BTN_ARROW = (By.XPATH, '//*[@id="index.loginExceptionWin"]/div[1]/div/div/div/div[1]')

    # 【校验区】
    # -->系统登录成功标志值
    # 国网标设
    LOGIN_SUCCESS = (By.XPATH, '//span[text()="工作台"]')
    # 电量PBS5000
    # LOGIN_SUCCESS = (By.XPATH, '//i[@onclick="modifypassword()"]')

    BTN_INFORMATAIN_PUS = (By.XPATH, "//span[contains(text(),'重要信息推出')]")
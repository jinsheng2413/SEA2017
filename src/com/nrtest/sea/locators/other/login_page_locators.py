# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: login_page_locators.py
@time: 2018/5/27 0027 8:47
@desc:
"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    # 【输入框】
    QRY_USERNAME = (By.XPATH, '//*[@id="staffNo_input"]')
    QRY_PASSWWORD = (By.XPATH, '//*[@id="password_input"]')
    INPUT_IDENTIFYING = (By.XPATH, '//*[@id="checkcode_input"]')

    # 【操作区】
    BTN_LOGIN = (By.XPATH, '//*[@id="inputform"]/table/tbody/tr[5]/td[2]/img')
    BTN_CONFIRM = (By.XPATH, "//button[contains(.,'确定')]")
    BTN_ARROW = (
        By.XPATH, '//*[@id="index.loginExceptionWin"]/div[1]/div/div/div/div[1]')
    # 验证码
    BTN_IDENTIFYING_CODE = (By.XPATH, '//*[@id="imageMask"]')
    #
    BTN_INFORMATAIN_PUS = (By.XPATH, "//span[contains(text(),'重要信息推出')]")


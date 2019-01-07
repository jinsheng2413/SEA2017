# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: login.py
@time: 2018/5/22 0022 14:04
@desc:
"""
from time import sleep

import pytesseract
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from com.nrtest.common.base_test import BaseTest
from com.nrtest.common.logger import Logger
from com.nrtest.common.setting import Setting
from com.nrtest.common.yamlSetting import YamlSetting
from com.nrtest.sea.locators.other.login_page_locators import LoginPageLocators
# from com.nrtest.common.yamlSetting import YamlSetting
from com.nrtest.sea.pages.other.login_page import LoginPage

logger = Logger(logger='Login').getlog()

class Login:
    def __init__(self):
        self.username = Setting.DEFAULT_USER
        self.password = Setting.DEFAULT_PASSWORD

    def _getMaskCode(self, driver):
        """
        验证码图片转文本处理
        :param driver:
        :return:
        """
        driver.save_screenshot(Setting.SCREENSHOTS_PATH + 'photo.png')
        imageMask = driver.find_element_by_id('imageMask')
        left = imageMask.location['x']
        top = imageMask.location['y']
        elementWidth = imageMask.location['x'] + imageMask.size['width']
        elementHeight = imageMask.location['y'] + imageMask.size['height']

        with Image.open(Setting.SCREENSHOTS_PATH + 'photo.png') as img_file:  # type: Image.Image
            img_sizes = img_file.size
            if img_sizes[0] == 1920:
                img_code = img_file.crop((left + 285, top + 130, elementWidth + 290, elementHeight + 130))
            else:
                img_code = img_file.crop((left, top, elementWidth, elementHeight))
            img_code.save(Setting.SCREENSHOTS_PATH + 'photo2.png')

        text = pytesseract.image_to_string(Setting.SCREENSHOTS_PATH + 'photo2.png')
        txt = text.replace(' ', '')
        return txt

    def _cleanScreen(self, driver):
        """
        登录成功失败判断与清屏处理（如，告警提示框等）
        :param driver:
        """
        con = driver.find_element_by_tag_name('body').text
        if '重要信息推出' in con:
            logger.info('%s成功登陆系统' % self.username)
            if '登录异常' in con:
                driver.find_element(*LoginPageLocators.BTN_CONFIRM).click()
            if '账号异常信息' in con:
                driver.find_element(*LoginPageLocators.BTN_ARROW).click()

    def login(self):
        baseTest = BaseTest()
        driver = baseTest.openBrowser(Setting.BROWSER)
        driver.maximize_window()
        driver.get(Setting.TEST_URL)

        is_failed = True
        while is_failed:
            # 验证码是否需要判断
            is_valid_mask = Setting.VALID_MASK.lower().startswith('y')
            if is_valid_mask:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable(LoginPageLocators.BTN_IDENTIFYING_CODE))
            loginPage = LoginPage(driver)
            loginPage.input_username(self.username)
            loginPage.input_password(self.password)
            if is_valid_mask:  # 验证码是否需要判断 yes是；no否
                mask_code = self._getMaskCode(driver)
                loginPage.input_identifying(mask_code)

            loginPage.btn_login()
            sleep(2)
            try:
                loginPage.driver.find_element(*LoginPageLocators.LOGIN_SUCCESS)
                is_failed = False
            except BaseException as ex:
                pass

            # 登录清屏处理
            if Setting.CLEAN_SCREEN.lower().startswith('y'):
                self._cleanScreen(loginPage.driver)

            # 登录失败时刷新验证码
            if is_valid_mask and is_failed:
                loginPage.click(LoginPageLocators.BTN_IDENTIFYING_CODE)
                sleep(1)
                logger.info('%s登陆失败,点击刷新验证码' % self.username)

        return loginPage.driver

    @classmethod
    def cookieLogin(cls, username):
        baseTest = BaseTest()
        driver = baseTest.openBrowser('firefox')
        driver.maximize_window()
        driver.get(Setting.TEST_URL)
        driver.add_cookie(YamlSetting.getCookie(username))
        driver.get(Setting.TEST_URL + '/index.jsp')

if __name__ == '__main__':
    login = Login()
    drv = login.login()
    # # cookie = drv.get_cookies()
    # # for i in cookie:
    # #     print(i)
    # pass

    # Login.cookieLogin('admin')

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

from com.nrtest.common.base_test import BaseTest
from com.nrtest.common.logger import Logger
from com.nrtest.common.setting import Setting
from com.nrtest.common.yamlSetting import YamlSetting
# from com.nrtest.common.yamlSetting import YamlSetting
from com.nrtest.sea.pages.other.login_page import LoginPage

logger = Logger(logger='Login').getlog()

class Login:
    def __init__(self):
        self.username = Setting.DEFAULT_USER
        self.password = Setting.DEFAULT_PASSWORD
        # 是否有验证码
        self.is_valid_mask = Setting.VALID_MASK.lower().startswith('y')

        # 是否需要登录后清屏处理
        self.is_clean_screen = Setting.CLEAN_SCREEN.lower().startswith('y')

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
        element_Width = left + imageMask.size['width']
        element_Height = top + imageMask.size['height']

        with Image.open(Setting.SCREENSHOTS_PATH + 'photo.png') as img_file:  # type: Image.Image
            img_sizes = img_file.size
            if img_sizes[0] == 1920:
                img_code = img_file.crop((left + 285, top + 130, element_Width + 290, element_Height + 130))
            else:
                img_code = img_file.crop((left, top, element_Width, element_Height))
            img_code.save(Setting.SCREENSHOTS_PATH + 'photo2.png')

        text = pytesseract.image_to_string(Setting.SCREENSHOTS_PATH + 'photo2.png')
        txt = text.replace(' ', '')
        return txt

    def login(self):
        baseTest = BaseTest()
        driver = baseTest.openBrowser(Setting.BROWSER)
        driver.maximize_window()
        driver.get(Setting.TEST_URL)
        sleep(2)

        is_failed = True
        while is_failed:
            loginPage = LoginPage(driver)
            loginPage.waitFor()
            loginPage.input_username(self.username)
            loginPage.input_password(self.password)
            if self.is_valid_mask:  # 是否需要验证码判断 yes是；no否
                mask_code = self._getMaskCode(driver)
                loginPage.input_identifying(mask_code)
            loginPage.btn_login()
            sleep(2)

            # 确认是否登录成功
            is_logined = loginPage.is_login_success()
            if is_logined:
                # 登录清屏处理
                if self.is_clean_screen:
                    loginPage.clean_screen()
                logger.info('%s成功登陆系统' % self.username)
                break
            elif self.is_valid_mask:
                # 登录失败后，刷新验证码
                loginPage.refresh_valid_mask()
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
    # cookie = drv.get_cookies()
    # for i in cookie:
    #     print(i)
    # pass

    # Login.cookieLogin('admin')

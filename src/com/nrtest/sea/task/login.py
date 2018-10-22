# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: login.py
@time: 2018/5/22 0022 14:04
@desc:
'''
from PIL import Image
from selenium import webdriver
from time import sleep
import pytesseract as pt
from PIL import Image

from com.nrtest.common.yamlSetting import YamlSetting
from com.nrtest.sea.pages.other.login_page import LoginPage
from com.nrtest.common.base_test import BaseTest
from com.nrtest.common.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from com.nrtest.common.setting import Setting
from com.nrtest.sea.locators.other.login_page_locators import LoginPageLocators
from com.nrtest.sea.pages.other.common_page import Common_page

from com.nrtest.common.setting import Setting

logger = Logger(logger="Login").getlog()

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        bool = True
        p = BaseTest()
        dr = p.openBrowser('c')
        dr.maximize_window()
        dr.get(Setting.TEST_URL)
        while (bool):
            WebDriverWait(dr, 30).until(EC.element_to_be_clickable(LoginPageLocators.BTN_IDENTIFYING_CODE))

            dr.save_screenshot(Setting.SCREENSHOTS_PATH+'photo.png')
            baidu = dr.find_element_by_id('imageMask')
            left = baidu.location['x']
            top = baidu.location['y']
            elementWidth = baidu.location['x'] + baidu.size['width']
            elementHeight = baidu.location['y'] + baidu.size['height']
            picture = Image.open(Setting.SCREENSHOTS_PATH+'photo.png')
            picture = picture.crop((left, top , elementWidth , elementHeight))
            picture.save(Setting.SCREENSHOTS_PATH+'photo2.png')

            image = Image.open(Setting.SCREENSHOTS_PATH+'photo2.png')
            text = pt.image_to_string(image)
            str = text.replace(' ','')

            loginPage = LoginPage(dr)
            loginPage.input_username(self.username)
            loginPage.input_password(self.password)
            loginPage.input_identifying(str)
            loginPage.btn_login()
            sleep(2)
            con = loginPage.driver.find_element_by_tag_name('body').text

            if '重要信息推出' in con:
                bool = False
                logger.info('{0}成功登陆系统'.format(self.username))
                if '登录异常' in con:
                    print("-----")
                    loginPage.driver.find_element(*LoginPageLocators.BTN_CONFIRM).click()
                if '账号异常信息' in con:
                    print("-----")
                    loginPage.driver.find_element(*LoginPageLocators.BTN_ARROW).click()

            else:
                loginPage.click(*LoginPageLocators.BTN_IDENTIFYING_CODE)
                logger.info('{0}登陆失败,点击刷新验证码'.format(self.username))

        return loginPage.driver

    @classmethod
    def cookieLogin(cls,username):
        p = BaseTest()
        dr = p.openBrowser('firefox')
        dr.maximize_window()
        dr.get(Setting.TEST_URL)
        dr.add_cookie(YamlSetting.getCookie(username))
        dr.get(Setting.TEST_URL+'/index.jsp')



#fdsdf
if __name__ == '__main__':
  lg = Login('gchb','123')
  dr = lg.login()
  dr.add_cookie({'name':'user','value':'gchb'})
  cookie = dr.get_cookies()
  for i in cookie:
      print(i)
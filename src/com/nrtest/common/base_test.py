# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: base_test.py
@time: 2018-05-31 15:03
@desc:
"""

# from lxml import etree
from selenium import webdriver

# from com.nrtest.sea.common.logger import Logger
from com.nrtest.common.logger import Logger
from com.nrtest.common.setting import Setting

logger = Logger(logger='BrowserEngine').getlog()


class BaseTest():
    # def __init__(self, browser):
    #     self.driver = self.openBrowser(browser)
    #     pass

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # 调自己封装类com.nrtest.common下的BeautifulReport.py
        path = Setting.IMG_PATH
        # 调LIB下类D:\Python\Python36-32\Lib\BeautifulReport.py
        # path = os.path.abspath(self.img_path)

        self.driver.get_screenshot_as_file('{}/{}.png'.format(path, img_name))

    @staticmethod
    def openBrowser(browser):
        """
        方法名：openBrowser
        说明：启动火狐、ie和谷歌浏览器中的任一个
         browser：浏览器的种类
         参数说明：chrome代表启动谷歌浏览器
        ie代表启动ie浏览器
        firefox代表启动火狐浏览器

        :param browser:
        :return:
        """
        if 'c' in browser:
            # 加启动配置
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')

            driver = webdriver.Chrome(chrome_options=option)
            logger.info('启动谷歌浏览器')
            return driver

        elif 'f' in browser:
            option = webdriver.FirefoxProfile()
            option.set_preference('plugin.state.flash', 2)
            driver = webdriver.Firefox(option)
            logger.info('启动火狐浏览器')
            return driver

        elif 'i' in browser:
            driver = webdriver.Ie()
            logger.info('启动IE浏览器.')
        return driver


if __name__ == '__main__':
    pass
    # t = BaseTest()
    # t.clear_values()

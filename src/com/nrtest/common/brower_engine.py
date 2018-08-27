# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: brower_engine.py
@time: 2018/5/23 0023 10:24
@desc:
方法名：openBrowser
        说明：启动火狐、ie和谷歌浏览器中的任一个
         kinder：浏览器的种类
         参数说明：chrome代表启动谷歌浏览器
           ie代表启动ie浏览器
           firefox代表启动火狐浏览器
'''
from com.nrtest.common.logger import Logger
from selenium import webdriver

'''
     

    '''
logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    # 启动浏览器
    def openBrowser(self, kinder):
        """
        方法名：openBrowser
        说明：启动火狐、ie和谷歌浏览器中的任一个
         kinder：浏览器的种类
         参数说明：chrome代表启动谷歌浏览器
        ie代表启动ie浏览器
           firefox代表启动火狐浏览器

        :param kinder:
        :return:
        """
        if 'c' in kinder:
            # 加启动配置
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')

            driver = webdriver.Chrome(chrome_options=option)
            logger.info('启动谷歌浏览器')
            return driver

        elif 'i' in kinder:
            driver = webdriver.Firefox()
            logger.info('启动ie浏览器.')
            return driver

        elif 'f' in kinder:
            driver = webdriver.Ie()
            logger.info('启动火狐浏览器')
            return driver


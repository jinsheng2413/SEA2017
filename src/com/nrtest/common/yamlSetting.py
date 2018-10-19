# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: yamlSetting.py
@time: 2018/10/9 0009 12:48
@desc:
'''
# import yaml
import tkinter as tk
from tkinter import filedialog
from com.nrtest.common.setting import Setting
class YamlSetting:
    base = "{'name': 'JSESSIONID', 'value': '%s', 'path': '/', 'domain': '192.168.176.10', 'expiry': None, 'secure': False, 'httpOnly': True}"

    @classmethod
    def get(cls,key):
        '''
        获取JSESSIONID
        :param key: 输入用户名
        :return:
        '''
        dic = yaml.load(open(Setting.CONIFG_PATH))
        value = (dic.get('JSESSIONID')).get(key)
        return value

    @classmethod
    def getCookie(cls,username):
        '''
        获取cookie
        :param username: 输入用户名
        :return:
        '''
        jd = cls.get(username)
        cookie = cls.base%jd

        return eval(cookie)

if __name__=='__main__':

    print(YamlSetting.getCookie('gchb'))

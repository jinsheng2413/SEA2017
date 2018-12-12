# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: setting.py
@time: 2018-05-30 19:03
@desc:
"""
import os
import platform
import sys

from com.nrtest.common.parse_nrtest import ParseNrTest

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'com'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


class Setting():
    def __init__(self):
        pass

    # 配置参数解析对象
    parse = ParseNrTest()
    # 默认用户名和密码

    # 默认浏览器
    BROWSER = parse.get('Base', 'DefaultBrowser')  # 'firefox'
    # 默认网址
    TEST_URL = parse.get('Base', 'Test_URL')  # 'http://testerlife.com'
    # 网址标题
    PAGE_TILE = parse.get('Base', 'PAGE_TILE')
    # 全局等待时间
    WAIT_TIME = parse.get('Base', 'WAIT_TIME')

    # 项目编号
    PROJECT_NO = parse.get('Project', 'PROJECT_NO').upper()

    # 区分windows与linux间不同的路径符号
    PATTERN = parse.pattern()[0]

    # 基础路径
    # BASE_PATH = r'D:\\PycharmProjects\\MyPython\\' if platform.system() == 'Windows' else r'/PycharmProjects/MyPython/'
    PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

    BASE_PATH = PROJECT_PATH.split('src')[0]

    CONIFG_PATH = BASE_PATH + '/src/com/nrtest/setup/nr_test.yaml'

    # 报表路径
    REPORT_PATH = BASE_PATH + r'{}reports/'.format(PATTERN)

    # 日志路径
    LOG_PATH = BASE_PATH + r'{}logs/'.format(PATTERN)

    # 截图路径

    IMG_PATH = BASE_PATH + r'{}img/'.format(PATTERN)

    # 自定义截图路径
    SCREENSHOTS_PATH = BASE_PATH + r'{}screenshots/'.format(PATTERN)

    # 校验图片路径
    SHOT_PATH = BASE_PATH + r'{}screenshots/'.format(PATTERN)
    # 数据库连接
    # 用户名
    DB_USER = parse.get('Db_setup', 'user_name')
    # 密码
    DB_PASSWORD = parse.get('Db_setup', 'password')
    # IP
    DB_HOST = parse.get('Db_setup', 'IP')
    # SID
    DB_NAME = parse.get('Db_setup', 'SID')
    DEFAULT_USER = parse.get('Login', 'user_name')
    DEFAULT_PASSWORD = parse.get('Login', 'password')
    GROUP_USER = parse.get('Login', 'user_group')


if __name__ == '__main__':
    p = Setting()
    print(p.PROJECT_NO)
    print(Setting.BASE_PATH)
    print(platform.system())

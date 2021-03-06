# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: setting.py
@time: 2018-05-30 19:03
@desc:
"""
import os
import sys

from com.nrtest.common.parse_nrtest import ParseNrTest

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'com'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


class Setting:
    def __init__(self):
        pass

    # 配置参数解析对象
    parse = ParseNrTest()
    # 默认用户名和密码

    # 默认浏览器
    BROWSER = parse.get('Base', 'DefaultBrowser')  # 'firefox'

    # 是否校验码验证
    VALID_MASK = parse.get('Base', 'Valid_Mask')

    #  登陆时，验证码是否需要加偏移量
    DEMAND_OFFSET = parse.get('Base', 'demand_offset')

    # 登录后是否需清屏
    CLEAN_SCREEN = parse.get('Base', 'clean_screen')

    # 是否关闭TIP，yes-是；no-否*
    CLOSE_TIP = parse.get('Base', 'close_tip')

    # 默认网址
    TEST_URL = parse.get('Base', 'Test_URL')  # 'http://testerlife.com'
    # 网址标题
    PAGE_TILE = parse.get('Base', 'PAGE_TILE')
    # 全局等待时间
    WAIT_TIME = parse.get('Base', 'WAIT_TIME')

    # 项目编号
    PROJECT_NO = parse.get('Project', 'PROJECT_NO').upper()

    # 区分windows与linux间不同的路径符号
    PATTERN = parse.pattern()

    # 基础路径
    # BASE_PATH = r'D:\\PycharmProjects\\MyPython\\' if platform.system() == 'Windows' else response'/PycharmProjects/MyPython/'
    PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

    BASE_PATH = PROJECT_PATH.split(PATTERN + 'src')[0]

    CONIFG_PATH = BASE_PATH + '/src/com/nrtest/setup/nr_test.yaml'

    # 报表路径
    REPORT_PATH = BASE_PATH + r'{}reports{}'.format(PATTERN, PATTERN)

    # 日志路径
    LOG_PATH = BASE_PATH + r'{}logs{}'.format(PATTERN, PATTERN)

    # 截图路径

    IMG_PATH = BASE_PATH + r'{}img{}'.format(PATTERN, PATTERN)

    # 自定义截图路径
    SCREENSHOTS_PATH = BASE_PATH + r'{}screenshots{}'.format(PATTERN, PATTERN)

    # 校验图片路径
    SHOT_PATH = BASE_PATH + r'{}screenshots{}'.format(PATTERN, PATTERN)
    # 数据库连接
    # 用户名
    DB_USER = parse.get('Db_setup', 'user_name')
    # 密码
    DB_PASSWORD = parse.get('Db_setup', 'password')
    # IP
    DB_HOST = parse.get('Db_setup', 'IP')
    # SID
    DB_NAME = parse.get('Db_setup', 'SID')
    # WEB用户账号与密码
    DEFAULT_USER = parse.get('Login', 'user_name')
    DEFAULT_PASSWORD = parse.get('Login', 'password')

    # 测试用例用户及用例组号
    GROUP_USER = parse.get('Login', 'user_group')
    GROUP_NO = parse.get('Login', 'group_no')

    # 根据下面分组配置执行：gt_for_menu_list.py
    GROUP_BY_MENU_LIST = parse.get('Login', 'group_by_menu_list')
    # jenkins的jop配置文件村长路径
    DEFAULT_CONFIG = BASE_DIR + '\common\default_config.xml'


if __name__ == '__main__':
    p = Setting()

    print(Setting.DEFAULT_CONFIG)

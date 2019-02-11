# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: user_except.py
@time: 2019-02-01 23:20
@desc:
"""


class PopupError(Exception):
    def __init__(self, action, error_info):
        super().__init__(self)  # 初始化父类
        self.action = action
        self.error_info = error_info

    def __str__(self):
        return self.error_info

    @property
    def get_action(self):
        """
        异常源对捕获该异常后的处理要求，action值为01时需再次抛异常
        :return: 00-没弹窗；01-截图，且抛异常；02-只截图，不抛异常；03-既不截图，也不抛异常; 04-没弹窗时，也截图，抛异常
        """
        return self.action


class TestImgError(Exception):
    def __init__(self, error_info):
        super().__init__(self)  # 初始化父类
        self.error_info = error_info

    def __str__(self):
        return self.error_info

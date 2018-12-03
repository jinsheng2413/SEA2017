# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: basePageContainsXpage.py
@time: 2018/12/3 0003 10:20
@desc:
"""
from selenium.webdriver.common.by import By


class BasePageContainsXpage:
    # 回收下拉框
    RECOVERY_DROP_DOWN = (By.XPATH, '//*[@id="info"]/tbody/tr/td[1]')

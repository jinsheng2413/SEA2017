# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: datarey_locators.py
@time: 2019/4/1 0001 11:26
@desc:
"""
from selenium.webdriver.common.by import By
class DataRey_locators:
    #电量数据查询
    A_FIRST_DROP_DOWN = (By.XPATH,'//div[starts-with(@id, "tb") and contains(@style, "display: block;")]/span[@class="combox1_xy"]//a')
    A_SECOND_DROP_DOWN = (
    By.XPATH, '(//div[starts-with(@id, "tb") and contains(@style, "display: block;")]/span[@class="combox1_xy"]//a)[{}]')
    # 下拉文本
    DROP_DOWN_TEXT = (By.XPATH, '//div[contains(@style,"block")]//div[contains(@class,"combobox-item") and text()="{}"]')


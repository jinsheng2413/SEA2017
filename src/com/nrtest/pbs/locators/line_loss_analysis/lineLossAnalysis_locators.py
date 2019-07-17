# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lineLossAnalysis_locators.py
@time: 2019/4/1 0001 9:06
@desc:
"""
from selenium.webdriver.common.by import By


class LineLossAnalysis_locators:
    # 损耗率--第二个输入框
    INPUT_SECOND = (By.XPATH, '(//span[contains(text(),"损耗率")]//input[contains(@class,"textbox-prompt")])[1]')
    # 损耗率--第五个输入框
    INPUT_FIFTH = (By.XPATH, '//span[contains(text(),"损耗率")]//input[contains(@class,"textbox-prompt")]')
    # 损耗率--第一个打开下拉A标签
    A_DOWN_FIRST = (By.XPATH, '(//span[contains(text(),"损耗率")]//a)[1]')
    # 损耗率--第二个打开下拉A标签
    A_DOWN_SECOND = (By.XPATH, '(//span[contains(text(),"损耗率")]//a)[2]')
    # 损耗率--第三个打开下拉A标签
    A_DOWN_THIRD = (By.XPATH, '(//span[contains(text(),"损耗率")]//a)[3]')
    # 下拉文本
    DROP_DOWN_TEXT = (By.XPATH, '//div[contains(@style,"block")]//div[contains(@class,"combobox-item") and text()="{}"]')


    #下拉区域
    DROP_DOWN_AREA = (By.XPATH,'(//*[text()="区域"]/..)[1]//a')

    #时间
    TIME_LOCATORS = (By.XPATH,'(//*[@id="search"]//input[@class="textbox-text validatebox-text"])[2]')

    #线损查询时间
    LINE_LOSS_TIME = (By.XPATH,'//span[@id="time2"]/span/input[1]')

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
    A_FIRST_DROP_DOWN = (By.XPATH,'(//div[starts-with(@id, "tb") and contains(@style, "display: block;")]/span[@class="combox1_xy"]//a)[1]')
    A_SECOND_DROP_DOWN = (
    By.XPATH, '(//div[starts-with(@id, "tb") and contains(@style, "display: block;")]/span[@class="combox1_xy"]//a)[2]')
    A_THIRD_DROP_DOWN = (
    By.XPATH, '(//div[starts-with(@id, "tb") and contains(@style, "display: block;")]/span[@class="combox1_xy"]//a)[3]')
    A_FOURTH_DROP_DOWN = (
    By.XPATH, '(//div[starts-with(@id, "tb") and contains(@style, "display: block;")]/span[@class="combox1_xy"]//a)[4]')
    # 下拉文本
    DROP_DOWN_TEXT = (By.XPATH, '//div[contains(@style,"block")]//div[contains(@class,"combobox-item") and text()="{}"]')
   #遥测值
    #日期
    TEST_DATE = (By.XPATH,'//*[@class=\"bg_fff search_xy panel-body panel-body-noheader layout-body\"]//input[@class="textbox-text validatebox-text"]')

   #遥测值
    FIRST_DROP = (By.XPATH,'(//*[@id="substation"]//a[@class="textbox-icon combo-arrow"])[1]')
    SECOND_DROP = (By.XPATH, '(//*[@id="substation"]//a[@class="textbox-icon combo-arrow"])[2]')
    THIRD_DROP = (By.XPATH, '//*[@id="tpanel"]//a[3]')


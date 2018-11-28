# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: skip.py
@time: 2018/11/27 0027 15:26
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.task.commonMath import *


class op(Page):

 def od(self):

    self.click(*(By.XPATH,'//*[text()=\'查询\']'))

openMenu('99911100')
driver = openLeftTree('134010101')
p = op(driver)
p.od()
p.clickSkip('用户编号,用户编号,用户数据查询')
# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: fr.py
@time: 2018/12/27 0027 11:06
@desc:
"""
import pytesseract

from com.nrtest.common.setting import Setting

text = pytesseract.image_to_string(Setting.SCREENSHOTS_PATH + 'photo2.png')
print(text)

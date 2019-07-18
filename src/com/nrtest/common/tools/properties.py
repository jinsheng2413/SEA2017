# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: properties.py
@time: 2019/7/18 0018 15:00
@desc:
"""
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
from com.nrtest.common.xls_rw import XlsRw


class op:
    def __init__(self):
        self.dr = webdriver.Chrome()

    def get(self, url):
        self.dr.maximize_window()
        self.dr.get(url)

    def input(self, xpath, value):
        self.dr.find_element_by_xpath(xpath).send_keys(value)

    def click(self, xpath):
        self.dr.find_element_by_xpath(xpath).click()

    def select(self, xpath, value):
        Select(self.dr.find_element_by_xpath(xpath)).select_by_visible_text(value)


if __name__ == '__main__':
    o = op()
    o.get('http://192.168.176.15:10010/')
    o.input('//*[@id="id1"]/span/input[1]','admin')
    o.input('//*[@id="id1"]/span/input[2]','Nari_sea3000')
    o.click('//*[@id="id1"]/span/button')

    x = XlsRw(r'C:\Users\Administrator\Desktop\web组git账号申请.xlsx')
    for item in range(5,x.r_row):
        line = x.read_row_out(item)
        o.click('/html/body/div[1]/div/div/div/div/ul/li[3]/a')
        o.click('/html/body/div[3]/div[2]/div/div/a[2]')

        o.select('//*[@name="namePanel:projectPath"]','WebProjectGW/manager/')
        o.input('//*[@id="name"]',line[2])
        o.input('//*[text()="描述"]/../input',line[1])
        o.click('//*[text()="限制查看，克隆和推送"]/../input')
        o.click('//*[text()="允许派生"]/../input')
        o.click('//*[@class="btn btn-appmenu"]')


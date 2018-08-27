# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: LineDataQueryLocators.py
@time: 2018-08-16 16:20
@desc:
'''

from selenium.webdriver.common.by import By

#统计查询→综合查询→线路数据查询
class LineDataQueryLocators:
#页面元素
    #线路编号
    QRY_LINENUM = (By.XPATH,'(//label[contains(text(),"线路编号")]/../div/input)[1]')
    #查询按钮
    BTN_SEARCH = (By.XPATH,'//div[@class="x-column-inner"]//button[contains(text(),"查询")]')
#操作对象选择区
    #电网结构
    TREE_ELECTRICPOWER = (By.XPATH,'(//span[contains(text(),"电网结构")])[1]')
    #营销电网结构
    TREE_MARKETING = (By.XPATH,'//span[contains(text(),"营销电网结构")]')
    #国网冀北电力有限公司
    TREE_JIBEI = (By.XPATH,'//div[@id="netTree"]//img[@class="x-tree-ec-icon x-tree-elbow-end-plus"]')
    # 电网_安各庄变电站
    TREE_ANGEZHUANG = (By.XPATH,'(//ul[@class="x-tree-node-ct"]/li[@class="x-tree-node"])[1]/div/img[1]')
    #电网_10kV523安变无税庄
    TREE_ANBIANWU = (By.XPATH,'//span[contains(text(),"电网_10kV523安变无税庄(交流10kV)")]')
#数据展示
    #查询日期_开始
    INPUTDT_STARTTIME = (By.XPATH,'(//div[@class="x-form-field-wrap x-form-field-trigger-wrap "])[1]')
    #查询日期_结束
    INPUTDT_ENDTIME = (By.XPATH,'(//div[@class="x-form-field-wrap x-form-field-trigger-wrap "])[2]')
    #查询按钮
    BTN_DATA_SEARCH = (By.XPATH,'(//div[@id="maintab"]//button[contains(text(),"查询")])[2]')

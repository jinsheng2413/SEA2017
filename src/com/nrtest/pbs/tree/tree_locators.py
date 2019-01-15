# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: tree_locators.py
@time: 2019-01-09 9:58
@desc:
"""
from selenium.webdriver.common.by import By


class TreeLocators:
    # class = "panel layout-panel layout-panel-west layout-split-west"
    TREE_DIV = (By.XPATH, '//div[ends-with(@class, "split-west"]')

    ROOT_NODE = (By.XPATH, '//ul[@id="treeDemo"]')
    # 计算公式：(By.XPATH, //div[@id = "treetab"]')'
    # 采集参数配置 (By.XPATH, '//ul[@id="tree"]//span[text()="{}"]')
    # 系统功能(By.XPATH, '//ul[@id="sysTree"]//span[text()="{}"]')
    # 费率列表 NORMAL_NODE = (By.XPATH, '//table[@class ="datagrid-btable"]//div[text()="{}"]')
    # 数据字典 (By.XPATH, '//ul[@id="dataDictionaryTree"]//span[text()="{}"]')

    NODE_LEVEL = (By.XPATH, '//li[@class="level{}"]/a[@title="{}"]/../span')
    # 保留，暂时不用
    LEEF_NODE = (By.XPATH, '//li[@class="level{}"]/a[@title="{}"]')

    # # 第一层
    # NODE_LEVEL0 = (By.XPATH, '//li[@class="level0"]/a[@title="{}"]/../span')
    # # span按钮打开状态：class="button level0 switch root_open"
    # # 	   关闭状态：class="button level0 switch root_close"
    #
    # # 第二层 局
    # NODE_LEVEL1 = (By.XPATH, '//li[@class="level1"]/a[@title="{}"]/../span')
    # # class="button level1 switch center_open"
    #
    # # 第三层 局下面的变电站
    # NODE_LEVEL2 = (By.XPATH, '//li[@class="level2"]/a[@title="{}"]/../span')
    # # NODE_LEVEL2 = (By.XPATH, '//li[@class="level2"]/a[@title="贵阳局.800kV黎平变电站"]/../span')
    #
    # # class="button level2 switch center_open"
    #
    # # 第四层
    # NODE_LEVEL3 = (By.XPATH, '//li[@class="level3"]/a[{}]/../span')
    # # class="button level3 switch center_close"
    #
    # # 第五层 设备
    # NODE_LEVEL4 = (By.XPATH, '//li[@class="level4"]/a[{}]/../span')
    # 			class="button level4 switch bottom_docu"   --只有一个节点或最后一个节点时是bottom  其他是center
    #
    # $x('//div[@id="treeDemo"]//li[@class="level3"]/a[@title="500kV"]/../span[@id="treeDemo_15_switch"]')
    # 		class="button level3 switch bottom_open"
    # 	设备
    # 	$x('//div[@id="treeDemo"]//li[@class="level4"]/a[@title="800kV.-高主表"]/../span[@id="treeDemo_19_switch"]')
    # 			class="button level4 switch center_docu"  --第一个、中间节点
    #
    # 	$x('//div[@id="treeDemo"]//li[@class="level4"]/a[@title="500kV.测试发电机组副表"]/../span[@id="treeDemo_22_switch"]')
    # 			class="button level4 switch bottom_docu"  --最后一个节点

    # 选择某变电站范围内搜索节点：如，某变电站下第n层的XXX节点: 省级用户level是2，市级用户level是1
    NODE_LEVEL_IN_SUB = (By.XPATH, '//li[@class="level{}"]/a[@title="{}"]/..//li[@class="level{}"]/a[@title="{}"]/../span')

    # 左边树: 全模型/搜索/收藏夹
    NODE_TAB = (By.XPATH, '//div[@class="tabs-wrap"]//span[text()="{}"]')

    # 【搜索TAB】
    # 向下箭头按钮（hover）
    DOWN_ARROW = (By.XPATH, '//span[@class="m-btn-downarrow"]')
    # 查询条件
    INPUT_SEARCH = (By.XPATH, '//span[@class="textbox searchbox"]//input[@placeholder="请输入关键字"]')

    # 查询按钮：
    BTN_SERCH = (By.XPATH, '//a[@class="textbox-icon searchbox-button"]')

    # 带复选框的树节点
    # 不选中'//span[@class="button chk checkbox_false_full"'
    # 选中'//span[@class="button chk checkbox_true_full"'
    NODE_CHK = (By.XPATH, '//li[@class="level{}"]/a[@title="{}"]/../span[starts-with(@class,"button chk checkbox")]')
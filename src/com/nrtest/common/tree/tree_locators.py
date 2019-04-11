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
    # 左边树不同Tab选择: 用户、终端、供电区域、行业、电网结构、群组
    NODE_TAB = (By.XPATH, '//li//span[@class ="x-tab-strip-text " and text()="{}"]')
    # 当前活动的TAB页内容

    # class =" x-panel x-panel-noborder  x-hide-display 隐藏
    # class =" x-panel x-panel-noborder  活动
    ACTIVE_TAB_PAGE = '//div[@class=" x-panel x-panel-noborder "]'

    TREE_DIV = '//div[@id="mainwest"]'

    # 省公司
    # 关：x-tree-ec-icon x-tree-elbow-end-plus
    # 开：class="x-tree-ec-icon x-tree-elbow-end-minus"
    NODE_PROVINCE = (By.XPATH,
                     '//div[@class="x-tree-root-node"]//li[@class="x-tree-node"]//span[text()="{}"]/../preceding-sibling::img[starts-with(@class,"x-tree-ec-icon")]')
    # 省公司下属局（市县所及用户均可）选择：
    # 【非叶子节点】
    # 关：class="x-tree-ec-icon x-tree-elbow-plus"
    # 开：class="x-tree-ec-icon x-tree-elbow-minus"
    # 【叶子节点】
    # class="x-tree-ec-icon x-tree-elbow"
    NODE_LEVEL = (By.XPATH,
                  '//div[@class="x-tree-root-node"]//ul[contains(@style, "visibility: visible; position: static;")]/li[@class="x-tree-node"]//span[text()="{}"]/../preceding-sibling::img[starts-with(@class,"x-tree-ec-icon")]')
    NODE_LEVEL_IN_PARENT = (By.XPATH,
                            '//div[@class="x-tree-root-node"]//ul[contains(@style, "visibility: visible; position: static;")]//li[@class="x-tree-node"]//span[text()="{}"]/ancestor::li[@class="x-tree-node"]/ul[contains(@style, "visibility: visible; position: static;")]/li[@class="x-tree-node"]//span[text()="{}"]/../preceding-sibling::img[starts-with(@class,"x-tree-ec-icon")]')

    LEEF_NODE = (By.XPATH,
                 '//div[@class="x-tree-root-node"]//ul[contains(@style, "visibility: visible; position: static;")]/li[@class="x-tree-node"]//span[text()="{}"]')
    LEEF_NODE_IN_PARENT = (By.XPATH,
                           '//div[@class="x-tree-root-node"]//ul[contains(@style, "visibility: visible; position: static;")]//li[@class="x-tree-node"]//span[text()="{}"]/ancestor::li[@class="x-tree-node"]/ul[contains(@style, "visibility: visible; position: static;")]/li[@class="x-tree-node"]//span[text()="{}"]')
    LEEF_PROVINCE = (By.XPATH,
                     '//div[@class="x-tree-root-node"]//li[@class="x-tree-node"]//span[text()="{}"]')

    # 选择节点范围内搜索节点：如，某供电局内搜索相关节点：
    # $x('//div[@id="mainwest"]//div[@id="areaTree"]//span[text()="唐山供电公司"]/../../..//span[text()="直属用户"]/../preceding-sibling::img[2]')
    # NODE_LEVEL_IN_PARENT = (By.XPATH, '//div[@id="mainwest"]//span[text()="{}"]/../../..//span[text()="{}"]/../preceding-sibling::img[2]')

    # 【搜索TAB】

    # 向下箭头按钮（hover）
    DOWN_ARROW = (By.XPATH, '//span[@class="m-btn-downarrow"]')
    # 查询条件
    INPUT_SEARCH = (By.XPATH, '//span[@class="textbox searchbox"]//input[@placeholder="请输入关键字"]')
    RREE_INPUT = (By.XPATH, '//label[normalize-space(text())="{}"]/..//input[@type!="hidden"]')



    # 带复选框的树节点
    # 不选中'//span[@class="button chk checkbox_false_full"'
    # 选中'//span[@class="button chk checkbox_true_full"'
    NODE_CHK = (By.XPATH, '//li[@class="level{}"]/a[@title="{}"]/../span[starts-with(@class,"button chk checkbox")]')

    # 【用户Tab页】
    USER_QRY_INPUT = {'02': (By.XPATH, '//div[@id="mainwest"]//div[@id="indexUserPanel"]//input[@name="consNo"]'),
                      '03': (By.XPATH, '//div[@id="mainwest"]//div[@id="indexUserPanel"]//input[@name="terminalAddr"]'),
                      '04': (By.XPATH, '//div[@id="mainwest"]//div[@id="indexUserPanel"]//input[@name="meterAssetNo"]')}
    # 查询按钮：
    USER_BTN_QUERY = (By.XPATH, '//div[@id="mainwest"]//div[@id="indexUserPanel"]//button[@class =" x-btn-text query" and text()="查询"]')

    NODE_USER_TAB_RSLT_DEFAULT = (By.XPATH, '//div[@id="mainwest"]//div[@id="leftUserGrid"]//div[@class="x-grid3-scroller"]//table[1]')
    NODE_USER_TAB_RSLT = (By.XPATH, '//div[@id="mainwest"]//div[@id="leftUserGrid"]//div[@class="x-grid3-scroller"]//table[%s]//td[1]/div/div')

    # 【群组Tab页】
    # 普通群组/重点用户群组/按单位展示/控制群组
    GROUP_NODE = {'05': (By.XPATH, '//div[@id="mainwest"]//div[@id="backTree"]'),
                  '06': (By.XPATH, '//div[@id="mainwest"]//div[@id="impoUserGroupTree"]'),
                  '07': (By.XPATH, '//div[@id="mainwest"]//div[@id="orgBackTree"]'),
                  '08': (By.XPATH, '//div[@id="mainwest"]//div[@id="controlTree"]')}


class TreeSingleUserLocators:
    """
    SEA2017单户综合查询
    """
    NODE_LEVEL = (By.XPATH, '//div[@class="x-tree-root-node"]//span[text()="{}"]/../../a/preceding-sibling::img[contains(@class, "elbow")]')
    LEEF_NODE = (By.XPATH, '//div[@class="x-tree-root-node"]//span[text()="{}"]')

    # 【搜索】
    # 查询条件
    QRY_INPUT = (By.XPATH, '//img[starts-with(@class,"x-form-trigger x-form-search-trigger")]/../../span/preceding-sibling::input')
    BTN_QUERY = (By.XPATH, '//img[starts-with(@class,"x-form-trigger x-form-search-trigger")]')
    # 查找到的终端节点
    TMNL_NODE = (By.XPATH, '//div[@class="x-grid-group-title" and contains(text(),"终端资产号:")]/ancestor::div[starts-with(@class, "x-grid-group ")]')
    # TMNL_NODE = (By.XPATH, '//div[@class="x-grid-group-title" and contains(text(),"终端资产号:")]')
    SPLIT_LINE = (By.XPATH, '//div[@class="x-layout-split x-layout-split-west x-splitbar-h"]')
    # 用户信息行
    USER_LINE = (By.XPATH, '//div[contains(@id, "gp-TMNL_ASSET_NO") and @class="x-grid-group-body"]//div[text()="{}"]')

    DROP_TARGET = (By.XPATH, '//div[text()="{}"]')

class TreePBSLocators:
    # class = "panel layout-panel layout-panel-west layout-split-west"
    TREE_DIV = (By.XPATH, '//div[ends-with(@class, "split-west"]')

    ROOT_NODE = (By.XPATH, '//ul[@id="treeDemo"]')
    # 计算公式：(By.XPATH, //div[@id = "treetab"]')'
    # 采集参数配置 (By.XPATH, '//ul[@id="tree"]//span[text()="{}"]')
    # 系统功能(By.XPATH, '//ul[@id="sysTree"]//span[text()="{}"]')
    # 费率列表 NORMAL_NODE = (By.XPATH, '//table[@class ="datagrid-btable"]//div[text()="{}"]')
    # 数据字典 (By.XPATH, '//ul[@id="dataDictionaryTree"]//span[text()="{}"]')

    NODE_LEVEL = (By.XPATH, '//li[@class="level{}"]/a[@title="{}"]/../span')
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
    NODE_LEVEL_IN_PARENT = (By.XPATH, '//li[@class="level{}"]/a[@title="{}"]/..//li[@class="level{}"]/a[@title="{}"]/../span')

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


class LeftTreeLocators:
    ID = 'myIframe'
    # 判断有没有展开
    TREE_ELEMENT_LOCATOR = (By.XPATH, '//*[@class="tabs-panels"]//*[text()="{}" and contains(@id,"tree")]')
    # 点击选中的目标
    TREE_ELEMENT_OPEN_LOCATOR = (By.XPATH, '//*[@class="tabs-panels"]//*[text()="{}" and contains(@id,"tree")]/../span[contains(@class,"open")]')

    CLOSE_LFET_TREE = (By.XPATH, '//*[contains(@class,"center_open") and contains(@id,"tr")]')
    CLOSE_LFET_ROOT_TREE = (By.XPATH, '//*[contains(@class,"root_open") and contains(@id,"tr")]')

    # 返回首页
    MAIN_PAGE = (By.XPATH, '//li[@class="nav_header"]')


class TreeQualityLocators:
    # 左边树不同Tab选择: 用户、终端、供电区域、行业、电网结构、群组
    NODE_TAB = (By.XPATH, '//li//span[@class ="x-tab-strip-text " and text()="{}"]')

    ROOT_IDS = {'指标类': "indexTreePanel", '采集质量类': 'collectionQualityTreePanel', '任务查询类': 'taskQueryTreePanel'}
    # 根节点
    # 关：class=" x-panel x-tree  x-panel-collapsed"
    # 开：class=" x-panel x-tree "
    NODE_ROOT = (By.XPATH, '//div[@id="{}"]')
    # 关：class="x-tree-ec-icon x-tree-elbow-end-plus"
    # 开：class="x-tree-ec-icon x-tree-elbow-end-minus"
    NODE_LEVEL = (By.XPATH, '//div[@id="{}"]//span[text()="{}"]/../../a/preceding-sibling::img[contains(@class, "elbow")]')

    LEEF_NODE = (By.XPATH, '//div[@id="{}"]//span[text()="{}"]')

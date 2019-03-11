# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_locators.py
@time: 2018/8/28 0028 13:45
@desc:
"""
from selenium.webdriver.common.by import By


class MenuLocators:
    """
    SEA2017标设的菜单元素
    """

    # 一级菜单
    # 通过菜单名定位，下同
    MENU_LEVEL1 = (By.XPATH, '//*[@id ="menu1"]/tbody/tr//img[@id="%s"]')

    # 二级菜单
    MENU_LEVEL2 = (By.XPATH, '//*[@id="smenu"]//*[@class="x-toolbar-left-row"]//*[@type="button" and text() = "%s"]')

    # 三级菜单
    MENU_LEVEL3 = (By.XPATH, '//ul[@class="x-menu-list"]/li/a/span[text() = "%s"]')

    # 四级菜单
    MENU_LEVEL4 = (By.XPATH, '//div[@class="x-menu x-menu-floating x-layer "][2]/ul/li//*[text()= "%s"]')

    # 五级菜单
    MENU_LEVEL5 = (By.XPATH, '//div[@class="x-menu x-menu-floating x-layer "][3]/ul/li//*[text()= "%s"]')

    # 上下滚动菜单按钮
    BTN_SCROLL_DOWN = (By.XPATH, '//div[starts-with(@class,"x-menu-scroller x-menu-scroller-bottom x-unselectable")]')
    BTN_SCROLL_UP = (By.XPATH, '//div[starts-with(@class,"x-menu-scroller x-menu-scroller-top x-unselectable")]')

    # 当前活动菜单页面
    ACTIVE_MENU_PAGE = (By.XPATH, '//li[@id="maintab__{}"]')

    # 当前菜单的关闭按钮
    CURR_MENU = (By.XPATH, '//li[@id="maintab__{}"]/a[@class="x-tab-strip-close"]')
    # 当前菜单或工作台外的其他菜单关闭按钮
    WORKBENCH = 'and @id != "maintab__工作台"'
    CLOSE_OTHERS_MENU = (By.XPATH, '//li[starts-with(@id,"maintab") {} and @id != "maintab__{}"]/a[@class="x-tab-strip-close"]')

    # 当前正在操作的菜单页面
    CURRENT_MENU = (By.XPATH, '//*[@class="x-tab-strip-inner"]//*[contains(text(),"%s")]')
    CURRENT_MENU1 = (By.XPATH, '//span[contains(@class,"x-tab-strip-text") and text() = "%s"]')
    # '//span[contains(@class,"x-tab-strip-text" and text() = "%s"]')
    # 右键菜单：关闭当前页/关闭其他所有页
    # '//*[@class="x-menu x-menu-floating x-layer "]//*[text()=\'关闭其他所有页\']'
    CLOSE_PAGES = (By.XPATH, '//*[@class="x-menu x-menu-floating x-layer "]//*[text()="%s"]')
    CLOSE_PAGES_SPE = (By.XPATH, '//*[@class ="x-menu x-menu-floating x-layer  x-hide-offsets"]//*[text()="%s"]')

    # 打开菜单超时对话框
    TIMEOUT_DLG = (By.XPATH, '//div[@class="x-window-bwrap"]//span[text()="请求无响应或超时！"]')

    # 打开菜单太多对话框
    OVER_15_DLG = (By.XPATH, '//span[text()="最多只允许打开15个菜单"]')
    # 关闭“超时”、“菜单太多”、“未找到对应模块名”等弹出对话框
    CLOSE_DLG = (By.XPATH, '//tbody[@class="x-btn-small x-btn-icon-small-left"]//button[text()="确定"]')

    # 长时间加载页面中:Loading
    LOADING = (By.XPATH, '//div[@class ="loading-indicator" and text()="Loading..."]')
    # 左边树查询超时等待
    LEFT_TREE_LOADING = (By.XPATH, '(//div[@id="indexUserPanel"]//div[@class="ext-el-mask-msg x-mask-loading"])[2]')

    # 【左边树】
    # 左边树按钮
    BTN_LEFT_MENU = (By.XPATH, '//div[@id="mainwest-xcollapsed"]/div')

    # 左边树省公司节点
    BTN_LEFT_MENU_ELETRIC = (By.XPATH, '//span[@unselectable="on"]')
    # 菜单下拉框选择
    BTN_MENU = (By.XPATH, '//*[@id="menuUseStat_menuCombo_1"]')
    # 左边加号
    BTN_LEFT_PLUS = (By.XPATH, '(//img[@class="x-tree-ec-icon x-tree-elbow-end-plus"])[%s]')
    # 公司加号
    BTN_COMPANY_PLUS = (By.XPATH, '(//img[@class="x-tree-ec-icon x-tree-elbow-plus"])[%s]')
    # 市
    BTN_COMPANY = (By.XPATH, '(//a[@class="x-tree-node-anchor"])[%s]')
    # 县
    BTN_COUNTY = (By.XPATH, "(//span[contains(text(),'直属用户')])[1]/../../../../li[%s]")
    # 县和用户
    BTN_COUNTY_AND_USER = (By.XPATH, "(//span[contains(text(),'直属用户')])[2]/../../../../li[%s]")

    LEFT_TREE_PANEL = '//div[@id="mainwest"]'

    # 【用户TAB页】
    NODE = {'02': (By.XPATH, '//*[@name="consNo"]'), '03': (By.XPATH, '//*[@name="terminalAddr"]'), '04': (By.XPATH, '//*[@name="meterAssetNo"]'),
            # 台区编号
            '12': (By.XPATH, '//input[@name="tgNo"]'),
            # 集中器地址
            '13': (By.XPATH, '//input[@name="terminalId"]'),
            # 集中器下电表资产号
            '14': (By.XPATH, '//*[@name="meterAssetNo"]'),
            # 【终端Tab页】
            #  采集点编号
            '22': (By.XPATH, '//input[@name="cp_no"]'),
            #  终端地址
            '23': (By.XPATH, '//input[@name="tmnl_addr"]')}

    # 不同用户类型下拉选择时点下拉操作
    SEL_USER_TYPE = (By.XPATH, '//div[text()="用户查询类型"]/../following-sibling::td//input')
    SEL_USER_CHECKBOX = (By.XPATH, '//div[@id="indexUserPanel"]//label[normalize-space(text())="{}"]/..//img')
    # 【终端Tab页】
    SEL_TMNL_CHECKBOX = (By.XPATH, '//div[@id="mainwest"]//label[normalize-space(text())="{}"]/..//img')
    USER_TMNL_BTN_QRY = (By.XPATH, '//div[@id="mainwest"]//button[text()="查询"]')


    # 【群组TAB页】
    GROUP_NODE = {'05': (By.XPATH, '//*[@id="mainPanel.operate"]//*[text()=\'普通群组\']'),
                  '06': (By.XPATH, '//*[@id="mainPanel.operate"]//*[text()=\'重点用户群组\']'),
                  '07': (By.XPATH, '//*[@id="mainPanel.operate"]//*[text()=\'控制群组\']')}
    # 用户TAB页的查询按钮
    # USER_TAB_BTN_QRY = (By.XPATH, '(//*[@id="indexUserPanel"]//*[text()="查询"])[5]')
    USER_TAB_BTN_QRY = (By.XPATH, '//div[@id="indexUserPanel"]//button[text()="查询"]')
    # 打开群组
    GROUP_PLUS = {'05': (By.XPATH, '//div[@id="backTree"]//span[text()="群组"]/../../*[@class="x-tree-ec-icon x-tree-elbow-end-plus"]'),
                  '06': (By.XPATH, '//div[@id="impoUserGroupTree"]//span[text()="群组"]/../../*[@class="x-tree-ec-icon x-tree-elbow-end-plus"]'),
                  '07': (By.XPATH, '//div[@id="controlTree"]//span[text()="群组"]/../../*[@class="x-tree-ec-icon x-tree-elbow-end-plus"]')}
    # 查询结果区
    NODE_USER_TAB_RSLT_DEFAULT = (By.XPATH, '//*[@id="leftUserGrid"]//div[@class="x-grid3-scroller"]//table[1]')
    # 2019-02-18
    # NODE_USER_TAB_RSLT = (By.XPATH, '//*[@id="leftUserGrid"]//div[@class="x-grid3-scroller"]//table[%s]//td[1]/div/div')
    NODE_USER_TAB_RSLT = (By.XPATH, '//*[@id="{}"]//div[@class="x-grid3-scroller"]//table//span[text()="{}"]')

    NODE_USER = (By.XPATH, '//*[@class="x-tab-strip-text " and text()=\'用户\']')
    NODE_GROUP = (By.XPATH, '//*[@class="x-tab-strip-text " and text()=\'群组\']')
    NODE_GROUP_RSLT = {'05': (By.XPATH, '//div[@id="backTree"]//span[text()="%s"]'),
                       '06': (By.XPATH, '//div[@id="impoUserGroupTree"]//span[text()="%s"]'),
                       '07': (By.XPATH, '//div[@id="controlTree"]//span[text()="%s"]')}


    # Tab页
    TAB_PAGE = (By.XPATH, '//span[@class="x-tab-strip-text " and text()="{}"]')

    # 【左边树显示区】
    TABLE_DATA = (By.XPATH, '(//*[@class="x-grid3-row-table"])[[1]]')
    TREE_MINUS = (By.XPATH, '//*[@class="x-tree-ec-icon x-tree-elbow-minus"]')
    TREE_END = (By.XPATH, '//*[@class="x-tree-ec-icon x-tree-elbow-end-minus"]')
    # # 【table显示区】
    # TAB_ONE = (By.XPATH, '(//table[@class="x-grid3-row-table"])[1]')
    # TAB_VALUE = (By.XPATH, "//*[@class="x-grid3-row-table"])[{0}]//td[1]")


class MenuPBSLocators:
    """
    D5000/PBS5000的菜单元素
    """
    # 首页窗口：
    # 选择一级菜单
    MENU_LEVEL1 = (By.XPATH, '//div[@id="project_head"]//p[@class="menu_p" and text()="{}"]')

    # 选择二级菜单	 @class="nav-item selectMenu active"
    MENU_LEVEL2 = (By.XPATH, '//div[@id="project_head"]//li[@class="nav-item selectMenu"]//p[text()="{}"]')

    # 当前活动菜单页面
    # ACTIVE_MENU_PAGE = (By.XPATH, '//div[@id="project_head"]//li[@class="nav-item selectMenu active"]//p[text()="{}"]')
    ACTIVE_MENU_PAGE = (By.XPATH, '//div[@id="project_head"]//li[@class="nav-item selectMenu active"]')

    # 返回首页:
    # //div[@id="project_head"]//li[@title="返回首页"]
    GOTO_MAINPAGE = (By.XPATH, '//div[@id="project_head"]//h2[@class="home_btn"]')

    # 当前页面选择的一级菜单
    # CONFORM_MENU = (By.XPATH, '//div[@id="project_head"]//h2[@class="home_btn" and text()="{}"]')


class MenuSEA20Locators:
    """
    SEA2.0的菜单元素
    """

    BTN_SCROLL_DOWN = (By.XPATH, '')


class MenuJLZDHLocators:
    """
    JLZDH的菜单元素
    """
    pass

if __name__ == '__main__':
    print(MenuLocators.GROUP_NODE['05'])

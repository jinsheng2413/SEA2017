# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_common_man_pageLocators.py
@time: 2018/6/4 0004 14:42
@desc:
"""
from selenium.webdriver.common.by import By


class SecurityCommonManPageLocators:
    # 【左边树】
    # 左边树按钮
    BTN_LEFT_MENU = (By.XPATH, '//*[@id="mainwest-xcollapsed"]/div')
    # 左边树国王冀北店里有限公司
    BTN_LEFT_MENU_ELETRIC = (By.XPATH, '//span[@unselectable="on"]')
    # 菜单下拉框选择
    BTN_MENU = (By.XPATH, '//*[@id="menuUseStat_menuCombo_1"]')
    # 左边加号
    BTN_LEFT_ADD = (By.XPATH, '//img[@class=\"x-tree-ec-icon x-tree-elbow-end-plus\"]')
    # 【操作区】
    BTN_SYS_MANAGE = (By.XPATH, '//*[@id="sysManIcon"]')
    # 公司
    BTN_COMPANY = (By.XPATH, '(//a[@class=\"x-tree-node-anchor\"])[%s]')

    # 菜单使用明细
    BTN_MENU_DETAIL = (By.XPATH, '//*[@id=\"menuUseStat_CenterTab\"]/div/div/ul/li[2]')

    # 系统使用情况统计
    BTN_SYS_USE_SITUATION_COUNT = (By.XPATH, "//button[contains(text(),'系统使用情况统计')]")
    # 系统配置管理
    BTN_SYS_CONFIG_MAN = (By.XPATH, "//button[contains(text(),'系统配置管理')]")
    # 数据字典管理
    BTN_DATA_DIC_MAN = (By.XPATH, "//ul[@class='x-menu-list']/li[1]")
    # 日志管理
    BTN_LOG_MAN = (By.XPATH, "//button[contains(text(),'日志管理')]")
    # 系统登陆日志
    BTN_SYS_LOGIN_LOG = (By.XPATH, "//*[contains(text(),'系统登录日志')]")
    # 系统操作日志
    BTN_SYS_OPERATION_LOG = (By.XPATH, "//*[contains(text(),'系统操作日志')]")
    # 系统升级日志
    BTN_SYS_UPGRADE_LOG = (By.XPATH, "//*[contains(text(),'系统升级日志')]")

    # 用户分布情况统计s
    BTN_SYS_USER_DISTRIBUTION_COUNT = (By.XPATH, "//span[contains(text(),'用户分布情况统计')]")
    # 菜单分布情况统计
    BTN_SYS_MENU_DISTRIBUTION_COUNT = (By.XPATH, "//span[contains(text(),'菜单使用情况统计')]")
    # 信息定制
    BTN_INFORMATION_CUSTOMIZATION = (By.XPATH, "//button[contains(.,'信息定制')]")
    # 推送信息定制
    BTN_PUSH_INFORMATION_CUSTOMIZATION = (By.XPATH, '(//span[@class="x-menu-item-text"])[1]')
    # 监控台定制
    BTN_MONITOR_CUSTOMIZATION = (By.XPATH, '(//span[@class="x-menu-item-text"])[2]')
    # 工作台定制
    BTN_WORK_CUSTOMIZATION = (By.XPATH, '(//span[@class="x-menu-item-text"])[3]')
    # 信息设置
    BTN_INFORMATION_MAKE = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[1]')
    # 重要信息推出
    BTN_IMPORTANT_INFORMATION_PUSH = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[2]')

    # 数据字典管理
    BTN_TAB_DATA_DIC = (By.XPATH, "//*[contains(text(),'数据字典管理')]")

    # 关闭其他所有页面
    BTN_CLOSE_OTHER_ALL_PAGE = (By.XPATH, "//*[contains(text(),'关闭其他所有页')]")
    # 关闭当前页面
    BTN_NOW_PAGE = (By.XPATH, "//*[contains(text(),'关闭当前页')]")
    # 确定
    BTN_CONFIRME = (By.XPATH, "//*[contains(text(),'确定')]")
    # 菜单使用统计
    BTN_MER_MENU_USE_COUNT = (By.XPATH, "//*[contains(text(),'菜单使用统计')]")
    # 左边树校验
    VAL = (By.XPATH, "//*[contains(text(),'电网结构')]")

    # 权限密码管理
    BTN_PWD_MANAGE = (By.XPATH, "//button[contains(text(),'权限密码管理')]")
    # 操作员管理
    BTN_OPERATOR_MANAGE = (By.XPATH, "//span[contains(text(),'操作员管理')]")
    # 角色管理
    BTN_ROLE_MANAGE = (By.XPATH, '//span[contains(text(),"角色管理")]')
    # 权限管理
    BTN_SEC_MANAGE = (By.XPATH, '//span[contains(text(),"权限管理")]')
    # 模板管理
    BTN_TEM_MANAGE = (By.XPATH, '//button[contains(text(),"模板管理")]')
    # 终端参数
    BTN_ZHONGDUAN = (By.XPATH, '//span[contains(text(),"终端参数")]')
    # 高级应用
    BTN_ADVAPP = (By.XPATH, '//*[@id="advAppIcon"]')
    # 费控管路
    BTN_FEI_MANGE = (By.XPATH, "//button[contains(text(),'费控管理')]")
    # 本地费控
    BTN_LOCAL_FEI_MANGE = (By.XPATH, '//div[@class=\"x-menu x-menu-floating x-layer \"]/ul/li[1]')
    # 【费控管理】
    # 专变用户费控管理
    BTN_SPE_USER_FEI_MANGE = (By.XPATH, "//*[@class=\"x-menu-list\"]//*[contains(text(),'专变用户费控管理')]")
    # 抵押用户余额查看
    BTN_LOW_USER_MONEY_CHECK = (By.XPATH, "(//div[@class=\"x-menu x-menu-floating x-layer \"])[2]/ul/li[3]")
    # 专变用户余额查看
    BTN_SPE_USER_MONEY_CHECK = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[5]')

    # 【一级菜单】

    # 统计查询
    BTN_STATREY = (By.XPATH, '//*[@id="qryStatIcon"]')

    # 【二级菜单】

    # 数据分析
    BTN_DATAANALYSE = (By.XPATH, '//button[contains(text(),"数据分析")]')

    # 工单查询
    BTN_WORKQUERY = (By.XPATH, '//button[contains(text(),"工单查询")]')

    # 【三级菜单-数据分析】
    # 负荷分析
    HOVER_LOADANALYSE = (By.XPATH, '//span[contains(text(),"负荷分析")]')

    # 【三级菜单-工单查询】
    # 工单查询2017
    BTN_WORKQUERY_2017 = (By.XPATH, '//span[contains(text(),"工单查询2017")]')

    # 【四级菜单-负荷分析】
    # 负荷排名分析
    BTN_LOADANALYSE_RANK = (By.XPATH, '//span[contains(text(),"负荷排名分析")]')

    # 【四级菜单--电价参数下发】
    BTN_ELE_PRICE_PARA = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[1]')
    # 低压用户购电参数下发
    BTN_LOW_USER_BUY_PARA_GIVEOUT = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[2]')
    # 本地费控执行统计
    BTN_LOCAL_FEI_MANAGE_EXECUTE_COUNT = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[6]')
    BTN_LOCAL_FEI_MANAGE_EXECUTE_COUNT_DISTRRIBUTIONC = (By.XPATH, "// *[contains(text(), '费控情况统计')]")
    BTN_LOCAL_FEI_MANAGE_EXECUTE_COUNT_DISTRRIBUTIOND = (By.XPATH, "// *[contains(text(), '费控情况明细')]")
    # 费控投入调试
    BTN_CUST_CONTROL_COMMISSIONING = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[7]')
    # 电费控
    BTN_ELE_CUST_MANAGE = (By.XPATH, '(//input[@name=\"d-rb-auto\"])[2]')

    # 专变用户余额查看
    BTN_SPECIAL_USER_BALANCE_CHECK = (By.XPATH, '(//div[@class="x-menu x-menu-floating x-layer "])[2]/ul/li[5]')

    # 负荷特性分析
    BTN_LOAD_SPECIALITY_ANALYSE = (By.XPATH, '//span[contains(text(),"负荷特性分析")]')
    # 负荷曲线分析
    BTN_LOAD_CURVE_ANALYSE = (By.XPATH, '//span[contains(text(),"负荷曲线分析")]')

    # 【一级菜单】
    # 统计查询
    BTN_STAT_REY = (By.XPATH, '//img[@id="qryStatIcon"]')

    # 【二级菜单】
    # 统计查询→综合查询
    BTN_SYNTHQUERY = (By.XPATH, '//button[contains(text(),"综合查询")]')

    # 【三级菜单】
    # 统计查询→综合查询→用户数据查询
    BTN_USERDATAQUERY = (By.XPATH, '//*[contains(text(),"用户数据查询")]')
    # 统计查询→综合查询→终端数据查询
    BTN_TERMINALDATAQUERY = (By.XPATH, '//span[contains(text(),"终端数据查询")]')
    # 统计查询→综合查询→配变数据查询
    BTN_PUBLICDATAQUERY = (By.XPATH, '//span[contains(text(),"配变数据查询")]')
    # 统计查询→综合查询→线路数据查询
    BTN_LINEDATAQUERY = (By.XPATH, '//span[contains(text(),"线路数据查询")]')

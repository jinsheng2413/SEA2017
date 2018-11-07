# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class TemplateManLocators():
    # 页面元素
    # 左子树按钮
    BTN_TREE = (By.XPATH, '//div[@id="mainwest-xcollapsed"]/div')
    # 供电单位
    BTN_UNIT = (By.XPATH, '//span[contains(text(),"国网冀北")]')
    # 终端类型
    BTN_TYPE = (By.XPATH, '(//div[@class="x-form-element"]/div/img)[1]')
    # 终端规约
    BTN_RULE = (By.XPATH, '(//div[@class="x-form-element"]/div/input)[2]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')
    # 新增按钮
    BTN_ADD = (By.XPATH, '//button[contains(text(),"新增")]')
    # 查看按钮
    BTN_LOOK = (By.XPATH, '//button[contains(text(),"查看")]')
    # 删除按钮
    BTN_DEL = (By.XPATH, '//button[contains(text(),"删除")]')
    # 第一个模板
    BTN_FIRST = (By.XPATH, '(//div[@class="x-grid3-row-checker"])[1]')
    # 终端类型
    # 全部
    BTN_TYPE_ALL = (By.XPATH, "//div[contains(text(),'巡检仪')]/../div[1]")
    # 负荷控制终端
    BTN_TYPE_FHKZ = (By.XPATH, "//div[contains(text(),'巡检仪')]/../div[2]")
    # 负荷监测终端
    BTN_TYPE_FHJC = (By.XPATH, "//div[contains(text(),'巡检仪')]/../div[3]")
    # 低压集中器
    BTN_TYPE_DYJZQ = (By.XPATH, "//div[contains(text(),'巡检仪')]/../div[4]")
    # 关口电能量终端
    BTN_TYPE_GKDNL = (By.XPATH, "//div[contains(text(),'巡检仪')]/../div[5]")
    # 巡检仪
    BTN_TYPE_XJY = (By.XPATH, "//div[contains(text(),'巡检仪')]/../div[6]")
    # 终端规约
    # 全部
    BTN_RULE_ALL = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[1]")
    # 05规约
    BTN_RULE_05 = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[2]")
    # 04规约
    BTN_RULE_04 = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[3]")
    # 面向对象规约
    BTN_RULE_MXDX = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[4]")
    # 国网96规约
    BTN_RULE_GW96 = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[5]")
    # 698规约
    BTN_RULE_698 = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[6]")
    # 698_13规约
    BTN_RULE_698_13 = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[7]")
    # 江西（浙江）规约
    BTN_RULE_JX = (By.XPATH, "//div[contains(text(),'698_13规约')]/../div[8]")
    # 新增页面
    # 供电单位
    BTN_ADD_UNIT = (By.XPATH, '//*[@name="orgName"]')
    # 供电单位菜单
    BTN_ADD_UNIT_MENU = (By.XPATH, '//img[@class="x-tree-node-icon"]/../img[1]')
    # 国网冀北电力有限公司
    BTN_ADD_JIBEI = (By.XPATH, '(//span[contains(text(),"国网冀北")])[2]')
    # 确定按钮
    BTN_UNIT_SURE = (By.XPATH,
                     '//div[@class=" x-window x-window-noborder x-window-plain x-resizable-pinned"]//button[contains(text(),"确定")]')
    # 终端类型
    BTN_ADD_TYPE = (By.XPATH, '//input[@name="tmnlTypeCode"]/../img')
    # 终端类型，负荷控制终端
    BTN_ADD_TYPE_FHKZ = (By.XPATH, "//div[@class=\"x-layer x-combo-list \"]/div/div[1]")

    # 终端规约
    BTN_ADD_RULE = (By.XPATH, '//input[@name="protocolCode"]/../img')
    # 终端规约，05规约
    BTN_ADD_RULE_05 = (By.XPATH, "//div[contains(text(),'04规约')]")
    # 数传延时
    QRY_DATATRANSDELAY = (By.XPATH, '//input[@name="dataTransDelay"]')
    # 主站传输延时
    QRY_STATTRANSDELAY = (By.XPATH, '//input[@name="statTransDelay"]')
    # 主站等待时间
    QRY_STATWAITTIME = (By.XPATH, '//input[@name="statWaitTime"]')
    # 重发次数
    QRY_RESENDTIMES = (By.XPATH, '//input[@name="resendTimes"]')
    # 心跳周期
    QRY_HEARTCYCLE = (By.XPATH, '//input[@name="heartCycle"]')
    # 通信流量门限
    QRY_COMMFLOWLIMIT = (By.XPATH, '//input[@name="commFlowLimit"]')
    # 短信中心号码
    QRY_MSGCENTERNO = (By.XPATH, '//input[@name="msgCenterNo"]')
    # 主站电话号码
    QRY_STSTPHONENO = (By.XPATH, '//input[@name="statPhoneNo"]')
    # 用户名
    QRY_USERNAME = (By.XPATH, '//input[@name="username"]')
    # 密码
    QRY_USERPWD = (By.XPATH, '//input[@name="userPwd"]')
    # 重拨次数
    QRY_REDIALTIMES = (By.XPATH, '//input[@name="redialTimes"]')
    # 在线重拨间断
    QRY_ONLINEREDIALINT = (By.XPATH, '//input[@name="onlineRedialInt"]')
    # 无通信断电时间
    QRY_POWEROFFTIME = (By.XPATH, '//input[@name="powerOffTime"]')
    # 密钥
    QRY_SECRETKEY = (By.XPATH, '//input[@name="secretKey"]')
    # 终端抄表间隔
    QRY_READMETERINT = (By.XPATH, '//input[@name="readMeterInt"]')
    # 电压上限
    QRY_VOLHIGHLIMIT = (By.XPATH, '//input[@name="volHighLimit"]')
    # 电压下限
    QRY_VOLLOWLIMIT = (By.XPATH, '//input[@name="volLowLimit"]')
    # 电压上上限
    QRY_VOLHHLIMIT = (By.XPATH, '//input[@name="volHhLimit"]')
    # 电压下下限
    QRY_VOLLLLIMIT = (By.XPATH, '//input[@name="volLlLimit"]')
    # 持续时间
    QRY_HIGHKEEPTIME = (By.XPATH, '//input[@name="highKeepTime"]')
    # 持续时间
    QRY_LOWKEEPTIME = (By.XPATH, '//input[@name="lowKeepTime"]')
    # 恢复系数
    QRY_HIGHRECOVERFAC = (By.XPATH, '//input[@name="highRecoverFac"]')
    # 恢复系数
    QRY_LOWRECOVERFAC = (By.XPATH, '//input[@name="lowRecoverFac"]')
    # 保存按钮
    BTN_SAVE = (By.XPATH, '//button[contains(text(),"保存")]')
    # 关闭保存成功窗口
    BTN_SAVE_CLOSE = (By.XPATH, '//span[contains(text(),"提示")]/../div')
    # 关闭终端参数模板维护窗口
    BTN_CLOSE = (By.XPATH, '//button[contains(text(),"关闭")]')
    BTN_TAB = (
        By.XPATH, '//div[@class=\" x-window x-window-noborder x-resizable-pinned\"]/div[1]/div/div/div[1]/div[1]')
    # 确定删除
    # “是”按钮
    BTN_DEL_YES = (By.XPATH, '//button[contains(text(),"是")]')

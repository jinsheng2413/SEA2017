# -*- coding:utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: base_locators.py
@time: 2018-12-03 14:37
@desc:
"""
from selenium.webdriver.common.by import By


class Locators:
    # 【日期等只读属性改变】
    # 去除查询条件只读属性，如：日期选择框
    JS_REMOVE_ATTR = 'document.getElementBy{}("{}").removeAttribute("{}");'

    JS_DT = '''var elements, el;
                elements= document.evaluate("%s", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                for (var i = 0; i < elements.snapshotLength; i++) {
                    el= elements.snapshotItem(i);
                    el.removeAttribute("readonly")
                }'''

    # 勿删
    # OBJ = '''function getDom(rege){
    #             var domAll = document.getElementsByTagName("arguments[0]"),domArr = new Array();
    #             for (var i = 0; i < domAll.length; i++) {
    #                 if (rege.test(domAll[i].text)) {
    #                     var obj = domAll[i]
    #                     var txt = obj.text.replace(new RegExp(/\s/,'g'), '');
    #                     if (txt == "arguments[1]" && obj.style.display=="block")
    #                         domArr.push(obj);
    #                 }
    #             }
    #             return domArr;
    #         }
    #         getDom(%s);'''

    # innerHTML  剔除空白字符，及中英文冒号，英文中杠（-）及中英文圆括号
    CLEAN_BLANK = r'''var elements, el, txt;
                    elements= document.evaluate("%s", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                    for (var i = 0; i < elements.snapshotLength; i++) {
                        el= elements.snapshotItem(i);
                        txt = el.innerText.replace(new RegExp(/[\s:：\-\(\)（）]/,'g'), '');
                        if (txt != el.innerText)
                            el.innerText = txt
                    }'''


class BaseLocators(Locators):
    """
    基类Page的元素定义
    """
    # document.getElementById()、getElementsByName()、getElementsByTagName()
    # presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
    # visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。

    # 框定菜单范围
    # '//div[@id="档案查询" and @class =" x-panel x-panel-noborder  x-hide-offsets"]'

    # 通用查询条件定位
    # 与工作台一起的已打开菜单ID  class=" x-panel x-panel-noborder  x-hide-offsets"
    MENU_PAGE_ID = '//div[@id="{}"]'

    # 多个TAB页情况下的元素定位附加内容: '//div[@class =" x-panel x-panel-noborder  x-hide-display"]'
    # 预留
    MULTI_TAB = ''

    # 【输入框】
    # 按标签定位input normalize-space:去除换行\空格 \r\n\t
    QRY_INPUT = (By.XPATH, '//div[@class="x-form-item "]/label[normalize-space(text())="{}"]/..//input[@type!="hidden"]')

    # 按id或name对input直接定位
    QRY_INPUT_BY = (By.XPATH, '//input[@{}="{}"]')  # 如：'//input[@name="{}"]'

    # 缺少标签或id、name情况下的日期元素定位
    QRY_DT_INPUT = (By.XPATH, '//img[starts-with(@class,"x-form-trigger x-form-date-trigger")]/../input')

    # $x('//label[not(text())]/../div/input') 标签值为空的input元素
    # $x('(//body//label[text()="抄读成功率:"]/ancestor::tr//input)[4]')




    # 【下拉框】
    # 下拉选择点击按钮
    SEL_CHECKBOX = (By.XPATH, '//label[normalize-space(text())="{}"]/..//img')

    SEL_CHECKBOX_CLEAN = (By.XPATH, '//label[normalize-space(text())="{}"]/..//input')
    SEL_CHECKBOX_BY = (By.XPATH, '//input[@{}="{}"]/../img')


    #【下拉复选框相关】
    # 取消所有已选项
    # SEL_UNCHECK_ALL = (By.XPATH, '//div[@class ="x-combo-list-inner"]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img')
    SEL_UNCHECK_ALL = (By.XPATH,
                       '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img[contains(@src, "/checked.gif")]')
    # 选择指定复选项@class="ux-lovcombo-item-text" and
    # SEL_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]//div[contains(text(),"{}")]/../div/img')
    SEL_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/..//img')


    # 【下拉单选框相关】
    # 下拉单选项选择@class="x-combo-list-item" and
    # DROPDOWN_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[contains(text(),"{}")]')
    DROPDOWN_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]')
    # $x('//div[@class="x-layer x-combo-list  x-resizable-pinned" and contains(@style,"visible;")]//div[contains(text(),"巡检仪")]')

    # 【单选框】
    # 根据标签找input
    RADIOBOX_LABEL2INPUT = (By.XPATH, '//label[@class="x-form-cb-label"and text()="{}"]/preceding-sibling::input')

    RADIOBOX_INPUT2LABEL = (By.XPATH, '//input[@type="radio" and @{}="{}"]/../label[@text()="{}"')

    # 【复选框】
    # 单个复选框
    SINGLE_CHECK_BOX = (By.XPATH, '//label[text()="{}"]/..//input[@type="checkbox"]')

    # 被选择的复选框
    CHKBOX_UNCHECK_ALL = (By.XPATH, '//input[@type="checkbox" and @{}="{}" and @checked=""]')

    # 根据INPUT的name找标签 checkbox/radio
    CHKBOX_INPUT2LABEL = (By.XPATH, '//input[@type="checkbox" and @{}="{}"]/../label[text()="{}"]')

    # 【按钮类元素】，如：查询按钮
    # BTN_QRY = (By.XPATH, '//button[@class =" x-btn-text" and contains(text(),"{}")]')
    BTN_QRY = (By.XPATH, '//button[normalize-space(text())="{}"]')
    BTN_QRY_BLANK = (By.XPATH, '//button[contains(normalize-space(text()),"{}")]')

    # 确定
    BTN_CONFIRM = (By.XPATH, "//*[text()='确定']")

    # 定位一个菜单页面内的某一Tab页
    TAB_PAGE = (By.XPATH, '//span[@class="x-tab-strip-text " and text()="{}"]')

    # 登录后弹出窗口：账号异常
    # BTN_ACCOUNT_EXCEPT = (By.XPATH, '//div[@class="x-window-header x-unselectable x-window-draggable"]/span[@class="x-window-header-text"]/../div[contains(@class,"x-tool-close")]')

    # 登录后弹出窗口：推出重要信息
    # BTN_IMPORTANT_INFO = (By.XPATH, '//button[@class=" x-btn-text cancel" and text()="不再提醒"]')


class BasePbsLocators(Locators):
    # 多个TAB页情况下的元素定位附加内容: '//div[@class =" x-panel x-panel-noborder  x-hide-display"]'
    # 预留
    MULTI_TAB = ''

    # 【输入框】
    # 按标签定位input normalize-space:去除换行\空格 \r\n\t
    QRY_INPUT = (By.XPATH, '//div[@class="x-form-item "]/label[normalize-space(text())="{}"]/..//input[@type!="hidden"]')

    # 按id或name对input直接定位
    QRY_INPUT_BY = (By.XPATH, '//input[@{}="{}"]')  # 如：'//input[@name="{}"]'

    # 缺少标签或id、name情况下的日期元素定位
    QRY_DT_INPUT = (By.XPATH, '//img[starts-with(@class,"x-form-trigger x-form-date-trigger")]/../input')

    # 【下拉框】
    # 下拉选择点击按钮
    SEL_CHECKBOX = (By.XPATH, '//label[normalize-space(text())="{}"]/..//img')

    # 【下拉复选框相关】
    # 取消所有已选项
    SEL_UNCHECK_ALL = (By.XPATH,
                       '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img[contains(@src, "/checked.gif")]')
    # 选择指定复选项
    SEL_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/..//img')

    # 【下拉单选框相关】
    # 下拉单选项选择
    DROPDOWN_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]')

    # 【单选框】
    # 根据标签找input
    RADIOBOX_LABEL2INPUT = (By.XPATH, '//label[@class="x-form-cb-label"and text()="{}"]/preceding-sibling::input')

    RADIOBOX_INPUT2LABEL = (By.XPATH, '//input[@type="radio" and @{}="{}"]/../label[@text()="{}"')

    # 【复选框】
    # 单个复选框
    SINGLE_CHECK_BOX = (By.XPATH, '//label[text()="{}"]/..//input[@type="checkbox"]')

    # 被选择的复选框
    CHKBOX_UNCHECK_ALL = (By.XPATH, '//input[@type="checkbox" and @{}="{}" and @checked=""]')

    # 根据INPUT的name找标签 checkbox/radio
    CHKBOX_INPUT2LABEL = (By.XPATH, '//input[@type="checkbox" and @{}="{}"]/../label[text()="{}"]')

    # 【按钮类元素】，如：查询按钮
    BTN_QRY = (By.XPATH, '//button[normalize-space(text())="{}"]')
    BTN_QRY_BLANK = (By.XPATH, '//button[contains(normalize-space(text()),"{}")]')

    # 确定
    BTN_CONFIRM = (By.XPATH, "//*[text()='确定']")

    # 定位一个菜单页面内的某一Tab页
    TAB_PAGE = (By.XPATH, '//span[@class="x-tab-strip-text " and text()="{}"]')

if __name__ == '__main__':
    # print(BaseLocators.OBJ % '/查\s{1,}询/')
    print(BaseLocators.CLEAN_BLANK)

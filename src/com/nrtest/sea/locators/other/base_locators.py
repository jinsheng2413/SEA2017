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

    # 输入框边上LABEL标签文本为空的定位处理:菜单编号/第n个元素
    QRY_INPUT_NOLABEL = (By.XPATH, '//label[not(text())]/..//input')




    # 【下拉框】
    # 下拉选择点击按钮
    SEL_CHECKBOX = (By.XPATH, '//label[normalize-space(text())="{}"]/..//img')

    SEL_CHECKBOX_CLEAN = (By.XPATH, '//label[normalize-space(text())="{}"]/..//input')
    SEL_CHECKBOX_BY = (By.XPATH, '//input[@{}="{}"]/../img')


    #【下拉复选框相关】
    # 取消所有已选项
    # 统计查询→综合查询→抄表成功率查询（河北）
    SEL_UNCHECK_ALL = (By.XPATH,
                       '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img[contains(@src, "/checked.gif")]')
    # 基本应用→数据采集管理→采集质量分析→采集成功率:按时间统计
    SEL_UNCHECK_ALL_CLS = (By.XPATH,
                           '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/../..//img[contains(@class,"-checked")]')
    # 选择指定复选项@class="ux-lovcombo-item-text" and
    # SEL_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]//div[contains(text(),"{}")]/../div/img')
    SEL_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/..//img')
    SEL_OPTION_EQUAL = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[text()="{}"]/..//img')


    # 【下拉单选框相关】
    # 下拉单选项选择@class="x-combo-list-item" and
    # DROPDOWN_OPTION = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[contains(text(),"{}")]')
    DROPDOWN_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]')
    DROPDOWN_OPTION_EQUAL = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[text()="{}"]')
    # $x('//div[@class="x-layer x-combo-list  x-resizable-pinned" and contains(@style,"visible;")]//div[contains(text(),"巡检仪")]')

    # 【单选框】
    # 根据标签找input
    RADIOBOX_LABEL2INPUT = (By.XPATH, '//label[@class="x-form-cb-label"and text()="{}"]/preceding-sibling::input')

    RADIOBOX_INPUT2LABEL = (By.XPATH, '//input[@type="radio" and @{}="{}"]/../label[@text()="{}"')

    # 【复选框】
    # 单个复选框
    SINGLE_CHECK_BOX = (By.XPATH, '//label[text()="{}"]/..//input[@type="checkbox"]')

    # 根据复选框顺序定位
    CHECK_BOX_BY_ORDER = (By.XPATH, '//label[text()="{}"]/..//input[{}]')

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

    # 数据加载中
    # DATA_LOADING = (By.XPATH, '//div[@class="ext-el-mask-msg x-mask-loading"]')
    DATA_LOADING = (By.XPATH, '//div[starts-with(@class, "ext-el-mask-msg")]//div[contains(text(),"...")]')

    # 弹框处理
    # POPUP_DLG = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]')
    # POPUP_DLG_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')
    # 弹窗对话框
    # 不同弹窗对话框的class属性
    # class=" x-window x-window-plain"
    # class=" x-window" and contains(@style, "visibility: visible;")
    # class=" x-window x-resizable-pinned"
    # class=" x-window x-window-plain x-window-dlg"
    #
    # 弹窗对话框的title属性
    # //span[@class="x-window-header-text" and text()="{}"]
    POPUP_DLG = (By.XPATH, '//div[starts-with(@class," x-window") and contains(@style, "visibility: visible;")]')
    # 弹窗确定按钮[待作废]
    POPUP_DLG_CONFIRM = (By.XPATH, '//div[starts-with(@class," x-window") and contains(@style, "visibility: visible;")]//button[text()="确定"]')
    # 弹窗 X 按钮  div[@class="x-tool x-tool-close"]
    POPUP_DLG_PLUS = (By.XPATH,
                      '//div[starts-with(@class," x-window") and contains(@style, "visibility: visible;")]//span[@class="x-window-header-text"]/../div[@class="x-tool x-tool-close"]')

    # 【登录后清屏处理】
    # 登录异常弹窗确认
    DLG_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')

    # 账号异常信息弹窗确认
    DLG_EXCEPT = (By.XPATH, '//div[@id="index.loginExceptionWin"]//div[contains(@class, "x-tool-close")]')
    # 重要信息推出窗口关闭
    DLG_IMPORT = (By.XPATH, '//button[contains(text(), "不再提醒")]')

    # 【查询结果显示区】
    # 显示区显示表头
    TABLE_HEAD = (By.XPATH,
                  '//div[text()="{}"]/ancestor::div[contains(@class,"x-grid-with-col-lines") and not(contains(@class, "x-hide-display"))]//div[@class="x-grid3-viewport"]//tr[@class="x-grid3-hd-row"]')
    #  选择查询结果的指定行  范例菜单： menu_no = '99941704'
    SELECT_ROW = (
        By.XPATH,
        '//div[text() ="{}"]/ancestor::div[contains(@class,"x-grid-with-col-lines") and not(contains(@class, "x-hide-display"))]//div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr/td[{}]//*[text()="{}"]')
    # 选查询结果第一行，且text长度大于2的列
    SELECT_FIRST_ROW = (By.XPATH,
                        '//div[contains(@class,"x-grid-with-col-lines") and not(contains(@class, "x-hide-display"))]//div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr/td//div[string-length(text())>2]')

    # 【跳转校验用】
    # 被选中的单选框
    QRY_RADIO_CHECKED = (By.XPATH, '//label[@class="x-form-cb-label"and text()="{}"]/preceding-sibling::input[@type="radio" and @checked=""]')
    # 被选中的复选框
    QRY_CHK_CHECKED = (By.XPATH, '//label[text()="{}"]/..//input[@type="checkbox" and @checked=""]')


class BasePbsLocators(Locators):
    # 多个TAB页情况下的元素定位附加内容: '//div[@class =" x-panel x-panel-noborder  x-hide-display"]'
    MENU_PAGE_ID = ''
    # 预留
    MULTI_TAB = ''

    # 【输入框】
    # 按标签定位input normalize-space:去除换行\空格 \r\n\t
    QRY_INPUT = (By.XPATH, '//*[text()="{}"]/..//input')

    # 按id或name对input直接定位
    QRY_INPUT_BY = (By.XPATH, '//input[@{}="{}"]')  # 如：'//input[@name="{}"]'

    # 缺少标签或id、name情况下的日期元素定位
    QRY_DT_INPUT = (By.XPATH, '//*[text()="{}"]/..//input')
    # 数据加载中
    # DATA_LOADING = (By.XPATH, '//div[@class="ext-el-mask-msg x-mask-loading"]')
    DATA_LOADING = (By.XPATH, '//div[starts-with(@class, "ext-el-mask-msg")]//div[contains(text(),"...")]')

    # 【下拉框】
    # 下拉选择点击按钮
    SEL_CHECKBOX = (By.XPATH, '//*[text()="{}"]/..//a[1]')

    # 【下拉复选框相关】
    # 取消所有已选项
    SEL_UNCHECK_ALL = (By.XPATH,
                       '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img[contains(@src, "/checked.gif")]')
    # 选择指定复选项
    SEL_OPTION = (By.XPATH, '//div[contains(@class,"x-layer x-combo-list ") and contains(@style,"visible;")]//div[contains(text(),"{}")]/..//img')

    # 【下拉单选框相关】
    # 下拉单选项选择
    DROPDOWN_OPTION = (By.XPATH, '//*[@class="panel combo-p" and contains(@style,"block")]//div[text()="{}"]')

    # 【单选框】
    # 根据标签找input
    RADIOBOX_LABEL2INPUT = (By.XPATH, '//label[text()="{}"]/preceding-sibling::input[1]')
    RADIOBOX_INPUT2LABEL_NUM = (By.XPATH, '//input[{}]')

    RADIOBOX_INPUT2LABEL = (By.XPATH, '//input[@type="radio" and @{}="{}"]/../label[@text()="{}"')

    # 【复选框】
    # 单个复选框
    SINGLE_CHECK_BOX = (By.XPATH, '//label[text()="{}"]/..//input[@type="checkbox"]')

    # 根据复选框顺序定位
    CHECK_BOX_BY_ORDER = (By.XPATH, '//label[text()="{}"]/..//input[{}]')

    # 被选择的复选框
    CHKBOX_UNCHECK_ALL = (By.XPATH, '//input[@type="checkbox" and @{}="{}" and @checked=""]')

    # 根据INPUT的name找标签 checkbox/radio
    CHKBOX_INPUT2LABEL = (By.XPATH, '//input[@type="checkbox" and @{}="{}"]/../label[text()="{}"]')

    # 【按钮类元素】，如：查询按钮
    # BTN_QRY = (By.XPATH, '//button[normalize-space(@title)="{}"]')
    # BTN_QRY_BLANK = (By.XPATH, '//button[contains(normalize-space(text()),"{}")]')
    BTN_QRY = (By.XPATH, '//*[contains(@id,"sear")] | //*[contains(@class,"sear")]|//*[contains(@title,"{}")]')
    # 确定
    BTN_CONFIRM = (By.XPATH, "//*[text()='确定']")

    # 定位一个菜单页面内的某一Tab页
    TAB_PAGE = (By.XPATH, '//span[@class="tabs-title" and text()="{}"]')

    # 弹框处理
    POPUP_DLG = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]')
    POPUP_DLG_CONFIRM = (By.XPATH, '//div[@class=" x-window x-window-plain x-window-dlg"]//button[text()="确定"]')
    # --------------------------------------
    # 输入框
    QRY_LOCATORS = (By.XPATH, '//*[text()="{}"]/..//input')
    QRY_LINE_LOCATORS = (By.XPATH, '//*[text()="{}"]/following-sibling::td[1]//input')
    # 按钮
    QRY_BUTTON = (By.XPATH, '//*[text()="{}"]')
    # 打开下拉框图标
    QRY_SELECT_DROP_DOWN = (By.XPATH, '//*[text()="{}"]/..//a[1]')
    QRY_LINE_SELECT_DROP_DOWD = (By.XPATH, '//*[text()="{}"]//following-sibling::td[1]//a')
    # 选中下拉框
    QRY_SELECT_DROP_DOWN_ELE = (By.XPATH, '//*[@class="panel combo-p" and contains(@style,"block")]//div[text()="{}"]')
    # 选中复选框
    CHECK_BOX = (By.XPATH, '//label[text()="{}"]')
    # 清楚复选框
    UNCHECK_BOX = (By.XPATH, '//input[@type="checkbox"]')



class BaseSEA20Locators(Locators):
    pass


class BaseJLZDHLocators(Locators):
    pass



if __name__ == '__main__':
    # print(BaseLocators.OBJ % '/查\s{1,}询/')
    print(BaseLocators.CLEAN_BLANK)

# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: base_page.py
@time: 2018-05-25 0:32
@desc:
"""
import os
import time
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.dictionary import Dict
from com.nrtest.common.logger import Logger
from com.nrtest.common.setting import Setting
from com.nrtest.sea.locators.other.base_locators import BaseLocators
from com.nrtest.sea.locators.other.common_locators import CommonLocators
from com.nrtest.sea.locators.other.menu_locators import MenuLocators

# create a logger instance
logger = Logger(logger='Page').getlog()


# def func_info():
#     info = inspect.stack()[1]
#     clean_info = '{}.{}::{}'.format(info[1].split('src/')[1].split('.')[0], cls.__class__.__name__, info[3])
#     print(clean_info)

class MustGetUrl():
    """
    必须到达的URL
       参数：
       url    - 必须到达的地址
    """

    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        driver.get(self.url)
        return self.url == driver.current_url


class Page():
    """
    本项目所有页面菜单的基类
    """

    def __init__(self, driver, menu_page=None):
        self.driver = driver
        self.base_url = Setting.TEST_URL
        self.main_page_title = Setting.PAGE_TILE
        self.project_no = Setting.PROJECT_NO
        self.menuPage = menu_page
        if bool(menu_page):
            self.menu_no = menu_page.menu_no
            self.menu_name = menu_page.menu_name
            self.menu_path = menu_page.menu_path
        else:
            self.menu_no = ''
            self.menu_name = ''
            self.menu_path = ''
        self.tst_case_id = None
        self.class_name = ''

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        # 调自己封装类com.nrtest.common下的BeautifulReport.py
        path = Setting.IMG_PATH
        # 调LIB下类D:\Python\Python36-32\Lib\BeautifulReport.py
        # path = os.path.abspath(self.img_path)

        self.driver.get_screenshot_as_file('{}/{}.png'.format(path, img_name))

    def error_window_process(func):
        """
        出现弹出框异常，抛出页面报错
        使用信息：

        例如：
        @ERROR_WINDOW_PROCESS
        def btn_query(self, is_multi_tab=False):
        """

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            tag = False
            try:

                el = args[0].driver.find_element(*CommonLocators.ERROR_WINDOW_PROCESS)
                if el:
                    tag = True
                    print('弹窗错误信息：%s' % el.text)

                    if tag:
                        raise RuntimeError('PageError')

                    return res

            except:
                if tag:
                    raise RuntimeError('page error--弹出框错误异常')
                    try:
                        args[0].driver.find_element(*CommonLocators.BTN_CONFIRM_LOCATORS).click()
                    except:
                        pass

        return wrapper
    def fail_on_screenshot(self, func):
        """
        函数/方法报错截图处理
        :param func:
        :return:
        """

        def get_snapshot_directory():
            """
            获取截图存放路径
            :return:
            """
            if not os.path.exists(Setting.IMG_PATH):
                os.mkdir(Setting.IMG_PATH)
            return Setting.IMG_PATH

        def get_current_time_str():
            """
            格式化时间
            :return:
            """
            # return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f")
            return time.strftime(time.time(), '%Y%m%d%H%M%S%f')

        def wrapper(*args, **kwargs):
            instance, selector = args[0], args[1]
            try:
                return func(*args, **kwargs)
            except (TimeoutException, NoSuchElementException, InvalidElementStateException) as ex:
                logger.error('Could not find the locator: %s .', selector)
                filename = '{}.png'.format(get_current_time_str())
                screenshot_path = os.path.join(
                    get_snapshot_directory(), filename)
                logger.debug(instance.selenium.page_source)
                instance.selenium.save_screenshot(screenshot_path)
                raise ex

        return wrapper

    def _element_ec_mode(self, locator, seconds=5, ec_mode=0):
        """
        不同元素等待模式
        :param locator:
        :param seconds:
        :param ec_mode:
        :return:
        """
        if ec_mode == 0:
            # 判断元素是否可点击
            WebDriverWait(self.driver, seconds).until(EC.element_to_be_clickable(locator))
        elif ec_mode == 1:
            # 判断元素是否已加载出来
            WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(locator))
        elif ec_mode == 2:
            # 判断元素是否可见
            WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(locator))

    def _find_element(self, locator, seconds=5, ec_mode=0):
        """
        方法名：_element
        功能：定位元素的具体某个元素WEBelement
            presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
            visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
        *注释：_代表类的私有属性或方法
        :param locator: 元素的位置
        :param seconds:
        :param ec_mode: 0:判断元素是否可点击;1:判断元素是否已加载;2:判断元素是否可见
        :return: 返回定位的元素
        """
        element = None
        try:
            self._element_ec_mode(locator, seconds, ec_mode)
            # 定位元素
            element = self.driver.find_element(*locator)
            except_type = ''
            except_info = ''
        except TimeoutException as te:
            except_type = '等待超时'
            except_info = te
            if locator[1].find('请求无响应或超时！') == -1:
                logger.error(u'等待元素超时--> {}\n{}'.format(locator, te))
        except NoSuchElementException as nse:
            except_type = '找不到元素'
            except_info = nse
            logger.error(u'未找到元素-->  {}\n{}'.format(locator, nse))
        except Exception as ex:  # 无法确定是哪类异常时用基类异常来捕获
            except_type = '其他错误'
            except_info = ex
            logger.error(u'其他查找元素错误-->  {}\n{}'.format(locator, ex))
        if except_type != '':
            DataAccess.el_operate_log(self.menu_no, self.tst_case_id, locator, self.class_name, except_type, except_info)
        return element

    def start_case(self, para, class_path=''):
        """
        开始执行测试用例
        :param para:
        """
        # print(class_path)
        self.class_name = class_path.split('src')[1][1:]
        self.tst_case_id = para['TST_CASE_ID']
        # print('开始执行... \n用例ID：{}；菜单编号：{}；菜单路径：{}；Tab页名称：{}。'.format(*list(para.values())[:4]))
        print('开始执行... \n')
        print('用例ID：{}；菜单编号：{}；菜单路径：{}；Tab页名称：{}'.format(self.tst_case_id, self.menu_no,
                                                         self.menu_path, para['TAB_NAME']))

    def end_case(self):
        """
        测试用例执行结束
        :param para:
        """
        # print('结束... \n用例ID：{}'.format(para['TST_CASE_ID']))
        print('结束... \n用例ID：{}'.format(self.tst_case_id))

    def _direct_find_element(self, locator):
        """
        直接查找元素，不存在时不需要抛出异常处理，如：登录成功判断、左边树是否已打开、菜单是否已存在等
        :return:
        """
        element = None
        try:
            element = self.driver.find_element(*locator)
        except:
            pass
        return element

    def _find_displayed_element(self, locators, idx=1):
        """
        当定位到多个元素时，返回第一个显示的元素
        :param locators:
        :return:定位到的元素
        """
        # print('{}\n{}'.format(locators, idx))
        elements = self._find_elements(locators)
        pos = 1
        element = None
        for el in elements:
            if el.is_displayed():
                if pos == idx:
                    element = el
                    break
                else:
                    pos += 1
        return element

    def format_xpath_multi(self, xpath, format_val='', is_multi_tab=True):
        """
        应用于多Tab页情况下的xpath格式化
        :param xpath:
        :param format_val:可以是字符串、元组
        :return:
        """
        loc = xpath
        if is_multi_tab:
            loc = (xpath[0], BaseLocators.MENU_PAGE_ID.format(self.menu_name) + \
                   BaseLocators.MULTI_TAB + xpath[1])
        return self.format_xpath(loc, format_val)

    def curr_input(self, values, is_multi_tab=False, is_multi_elements=False):
        """
        新版输入查询条件操作
        :param values:要输入的值
        :param is_multi_tab:菜单面内是否有多个TAB页
        :param is_multi_elements:菜单面内是否有多个重复元素
        """
        try:
            ls_values = values.split(';')
            loc = self.format_xpath_multi(BaseLocators.QRY_INPUT, ls_values[0], is_multi_tab)
            if is_multi_elements:
                el = self._find_displayed_element(loc)
            else:
                el = self._find_element(loc)
            el.clear()
            el.send_keys(ls_values[1])
            # logger.info('list index out of range文本框输入:{}'.format(values))
        except AttributeError as ex:
            logger.error('输入错误:{}\n{}'.format(values, ex))

    def inputDate(self, value, is_multi_tab=False, new_idx=0):
        """
        新版日期输入框操作：没标签、没定义name或id时对可见日期选择框进行定位
        :param value:要输入的值:自定义标签名;第n个日期选择框;日期值【该值不填默认为1】：开始日期;1;2018-12-24
        :param is_multi_tab:菜单面内是否有多个TAB页
        :param new_idx:配置的idx因页面查询条件有变化时，替换为当前参数值
        """
        try:
            ls_values = value.split(';')
            # print(ls_values)
            loc = self.format_xpath_multi(BaseLocators.QRY_DT_INPUT, ls_values[0], is_multi_tab)
            tmp = ls_values[1].strip()
            idx = new_idx
            if new_idx == 0:
                idx = 1 if len(tmp) == 0 else int(tmp)
            if idx <= 0:
                raise Exception('日期选择框调整顺序【{}】不对，请确认'.format(idx))

            el = self._find_displayed_element(loc, idx)
            self.driver.execute_script("arguments[0].value=arguments[1]", el, ls_values[2])
            # el.clear()
            # el.send_keys(ls_values[2])
            logger.info('日期选择框填写:{}'.format(value))
        except Exception as ex:
            logger.error('输入错误:{}\n{}'.format(value, ex))

    def curr_click(self, is_multi_tab=False, btn_name='', idx=1):
        """
        新版点击方法
        :param btn_name:按钮元素文本值
        :param is_multi_tab:菜单面内是否有多个TAB页
        """
        try:
            btn_name = btn_name if bool(btn_name) else '查询'
            loc = self.format_xpath_multi(BaseLocators.BTN_QRY, btn_name, is_multi_tab)
            if is_multi_tab:
                el = self._find_displayed_element(loc, idx)
            else:
                el = self._find_element(loc)
            el.click()

            logger.info('点击元素：{}'.format(loc))
        except BaseException as e:
            logger.error('点击元素失败:{}\n{}'.format(loc, e))

    @error_window_process
    def btn_query(self, is_multi_tab=False, idx=1):
        """
        通用页面查询按钮
        :param is_multi_tab: 多Tab页时，如果查询按钮名有重复，则该值填True
        """
        self.curr_click(is_multi_tab, idx=idx)

    def selectDropDown(self, option, is_multi_tab=False, sleep_sec=0, is_multi_elements=False, is_equalText=False):
        """
        下拉单选框选择
        :param option: 参数格式：查询条件标签名;查询条件
        :param is_multi_tab: 多Tab页时，如果查询条件有重复，则该值填True
        :param sleep_sec:休眠n秒
        :param is_multi_elements:是否存在重复元素
        :param is_equalText: True-下拉选择值需完全匹配，Fase-部分匹配
        """
        if (option.find(';') == -1):
            print('............请配置查询条件的标签值............')
        else:
            ls_option = option.split(';')
            item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]
            if bool(item):
                # 打开下拉框
                xpath = self.format_xpath_multi(BaseLocators.SEL_CHECKBOX, ls_option[0], is_multi_tab)
                if is_multi_elements:
                    el = self._find_displayed_element(xpath)
                    el.click()
                else:
                    self.click(xpath)

                if bool(sleep_sec):
                    sleep(sleep_sec)

                # 根据名称选择下拉框
                if is_equalText:
                    loc = self.format_xpath(BaseLocators.DROPDOWN_OPTION_EQUAL, item)
                else:
                    loc = self.format_xpath(BaseLocators.DROPDOWN_OPTION, item)
                self.click(loc)
            else:  # 选择值为空时，表示选择全部
                xpath = self.format_xpath_multi(BaseLocators.SEL_CHECKBOX_CLEAN, ls_option[0], is_multi_tab)
                el = self._find_displayed_element(xpath)
                self.driver.execute_script("arguments[0].value=arguments[1]", el, '')

    def specialDropdown(self, option, locator, idx=1, locator_clean=None):
        """
        无法通过通用定位方法定位元素时，通过特殊locator定位选择
        :param option: 要选择的选项
        :param locator: 要定位的元素
        :param idx:选择定位到的第idx个元素
        :param locator_clean:全选时的清空处理
        """
        ls_option = option.split(';')
        item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]

        el = self._find_displayed_element(locator, idx)
        el.click()
        # 根据名称选择下拉框
        if bool(item):
            loc = self.format_xpath(BaseLocators.DROPDOWN_OPTION_EQUAL, item)
            self.click(loc)
        else:  # 选择值为空时，表示选择全部
            if bool(locator_clean):
                loc = locator_clean
            else:
                loc = (locator[0], locator[1] + '/preceding-sibling::input')
            el = self._find_displayed_element(loc, idx)
            self.driver.execute_script("arguments[0].value=arguments[1]", el, '')

    def specialInput(self, locator, value, idx=1):
        # 页面元素位置变动时，会存在定位错误问题，需人工调整
        loc = self.format_xpath_multi(locator, idx, True)
        el = self._find_displayed_element(loc, idx)
        el.send_keys(value.split(';')[1])

    def noLabelInput(self, value, idx=1):
        """
        输入框左边有label但没text值的定位
        :param value: 输入值
        :param idx: 第idx个此类可见输入框
        """
        # 页面元素位置变动时，会存在定位错误问题，需人工调整
        locator = self.format_xpath_multi(BaseLocators.QRY_INPUT_NOLABEL, idx, True)
        el = self._find_displayed_element(locator, idx)
        el.send_keys(value.split(';')[1])

    def _uncheck_all(self, option_name):
        """
        判断元素是否被选中
        :param option_name:下拉复选中选项，其中一个中文名称
        :return:
        """
        unchek_all_path = self.format_xpath(BaseLocators.SEL_UNCHECK_ALL, option_name)
        elements = self._find_elements(unchek_all_path)
        for el in elements:
            # if el.get_attribute('src').find('/checked.gif') > -1:
            #     el.click()
            el.click()

    def selectCheckBox(self, options, is_multi_tab=False, sleep_sec=0, is_multi_elements=False, is_equalText=False):
        """
        下拉复选框选择
        :param options: 参数格式：查询条件标签名;下拉选择项定位值;一组以,隔开的查询条件
        :param is_multi_tab: 多Tab页时，如果查询条件有重复，则该值填True
        :param sleep_sec:休眠n秒
        :param is_multi_elements:同一菜单是否存在重复元素
        :param is_equalText: True-下拉选择值需完全匹配，Fase-部分匹配
        """
        # print ('selectCheckBox', options, is_multi_tab)
        if (options.find(';') == -1):
            print('请配置查询条件的标签值。')
        else:
            ls_option = options.split(';')
            xpath = self.format_xpath_multi(BaseLocators.SEL_CHECKBOX, ls_option[0], is_multi_tab)
            # print('selectCheckBox', 'qry_path', xpath)
            if is_multi_elements:
                el = self._find_displayed_element(xpath)
                el.click()
            else:
                self.click(xpath)

            if bool(sleep_sec):
                sleep(sleep_sec)

            # 清除已选项
            self._uncheck_all(ls_option[1])

            if len(ls_option[2]) > 0 and ls_option[2] != '全部':
                for option in ls_option[2].split(','):
                    if is_equalText:
                        img_chk_xpath = self.format_xpath(BaseLocators.SEL_OPTION_EQUAL, option)
                    else:
                        img_chk_xpath = self.format_xpath(BaseLocators.SEL_OPTION, option)
                    self.click(img_chk_xpath)

            # 回收下拉框
            # self.click(BasePageContainsXpage.RECOVERY_DROP_DOWN)
            el.click() if is_multi_elements else self.click(xpath)

    def remove_attr(self, attr, obj_attr='readOnly'):
        """
        去除查询条件等对象的属性
        :param attr: 对象名 (By.ID/NAME, xxx)
        :param obj_attr: 对象属性
        """
        self.driver.execute_script(BaseLocators.JS_REMOVE_ATTR.format(attr[0].capitalize(), attr[1], obj_attr))

    def remove_readonly(self, attr):
        """
        通过元素的id或name定位并去除元素的readonly属性
        :param attr: attr: 对象名 (By.ID/NAME, xxx)
        """
        self.remove_attr(self, attr)

    def remove_dt_readonly(self, is_multi_tab=True):
        """
        新版日期输入框操作：没标签、没定义name或id时对可见日期选择框进行定位
        :param attr: 对象名 (By.ID/NAME, xxx)
        :param obj_attr: 对象属性
        """

        if is_multi_tab:
            xpath = BaseLocators.MENU_PAGE_ID.format(self.menu_name) + BaseLocators.QRY_DT_INPUT[1]
        else:
            xpath = BaseLocators.QRY_DT_INPUT[1]
        # 把xpath对象中的 “ 替换为 '
        js_attr = BaseLocators.JS_DT % xpath.replace('"', '\'')
        # print('*************js_attr', js_attr)
        self.driver.execute_script(js_attr)

    def _clean_blank(self, tag_text, tag_name='label'):
        """
        剔除标签中的空白字符及冒号：:
        :param tag_text: 标签中第一个连续中英文
        :param tag_name: 要剔除的tag
        """
        clean_obj = {'button': "//button[contains(text(), '{}')]",
                     'label': "//label[contains(text(), '{}')]",
                     'span': "//span[contains(text(), '{}')]"}
        clean_me = BaseLocators.MENU_PAGE_ID.format(self.menu_name).replace('"', '\'') + clean_obj[tag_name].format(tag_text[0])
        script = BaseLocators.CLEAN_BLANK % clean_me
        # print(script)
        self.exec_script(script)

    def clean_btn(self, tag_text):
        """
        请按钮名上的空格
        :param tag_text: 按钮名的部分内容
        """
        self._clean_blank(tag_text, 'button')

    def clean_label(self, tag_text):
        """
        清查询条件标签上的空格
        :param tag_text: 标签名的部分内容
        """
        self._clean_blank(tag_text)

    def clean_span(self, tag_text):
        """
        清日期选择标签上的空格
        :param tag_text: 标签名的部分内容
        """
        self._clean_blank(tag_text, 'span')

    def scrollToElement(self, locator):
        """
        滚动元素到指定位置
        :param locator:
        :return:
        """
        el = self._find_element(locator)
        logger.info('scroll view element')
        # // roll down and keep the element to the center of browser：scrollIntoView
        self.driver.execute_script('arguments[0].scrollIntoView();', el)

    def clickRadioBox(self, option, is_multi_tab=False, is_multi_elements=False):
        """
        选择单选框
        :param option: 被选择项名称
        :param is_multi_tab:
        :param is_multi_elements:
        """
        try:
            if (option.find(';') == -1):
                item = option
            else:
                ls_option = option.split(';')
                item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]

            if len(item) == 0:
                raise '单选框必须指定选择项：{}'.format(option)
            xpath = self.format_xpath_multi(BaseLocators.RADIOBOX_LABEL2INPUT, item, is_multi_tab)
            if is_multi_elements:
                el = self._find_displayed_element(xpath)
                el.click()
            else:
                self.click(xpath)
        except BaseException as ex:
            print('点击单选框失败：{}'.format(ex))

    def clickSingleCheckBox(self, options, is_multi_tab=False, is_multi_elements=False, locator=None):
        """
         选择单个复选框
         :param options: 被选择项
         :param is_multi_tab:
         """
        try:
            ls_option = options.split(';')
            item = ls_option[1]
            # 赋值选中，不赋值不选中
            is_select = bool(item)
            loc = locator if bool(locator) else BaseLocators.SINGLE_CHECK_BOX
            xpath = self.format_xpath_multi(loc, ls_option[0], is_multi_tab)
            if is_multi_elements:
                el = self._find_displayed_element(xpath)
            else:
                el = self._find_element(xpath)
            if is_select != el.is_selected():
                el.click()
            return el.is_selected()
        except BaseException as ex:
            print('点击失败：{}'.format(ex))
            return False

    def clickCheckBox(self, items, attr, is_multi_tab=False):
        """
        选择多个复选框【checkBox的name或id一致时调用此方法】
        :param items: 以逗号隔开，来实现点击多个复选框，eg:CheckBoxName='选中,未选中'
        :param attr: 属性值
        :param is_multi_tab: 页面是否有多Tab页
        """
        try:
            # 撤销已选项
            xpath = self.format_xpath_multi(BaseLocators.CHKBOX_UNCHECK_ALL, attr, is_multi_tab)
            elements = self._find_elements(xpath)
            for el in elements:
                el.click()

            if items.find(';') >= 0:
                ls_items = (items.split(';')[1]).split(',')
            else:
                ls_items = items.split(',')

            if ls_items[0] != '':
                for item in ls_items:
                    by_attr = (attr[0], attr[1], item)
                    xpath = self.format_xpath_multi(BaseLocators.CHKBOX_INPUT2LABEL, by_attr, is_multi_tab)
                    self.click(xpath)
        except BaseException as ex:
            print('点击复选框失败：{}'.format(ex))

    def clickCheckBox_new(self, options, is_multi_tab=False):
        """
        选择多个复选框【checkBox的name或id不一致时调用此方法】
        :param options: 以逗号隔开，来实现点击多个复选框，eg:CheckBoxName='选中,未选中'
        :param is_multi_tab: 页面是否有多Tab页
        """
        try:
            ls_option = options.split(';')
            ls_items = ls_option[2].split(',')
            data_dict = DataAccess.get_data_dictionary(ls_option[1])
            for data in data_dict:
                xpath = self.format_xpath_multi(BaseLocators.SINGLE_CHECK_BOX, data, is_multi_tab=is_multi_tab)
                el = self._find_displayed_element(xpath)
                is_select = data in ls_items
                if is_select != el.is_selected():
                    el.click()
        except BaseException as ex:
            print('点击复选框失败：{}'.format(ex))

    def clickTabPage(self, tab_name, is_multi_tab=False, is_multi_elements=False):
        """
        打开Tab页
        :param tab_name:
        """
        if tab_name.find(';') >= 0:
            ls_items = tab_name.split(';')
            tab = ls_items[1]
        else:
            tab = tab_name

        xpath = self.format_xpath_multi(BaseLocators.TAB_PAGE, tab, is_multi_tab)
        if is_multi_elements:
            el = self._find_displayed_element(xpath)
            el.click()
        else:
            self.click(xpath)

    def clickDt_Tab(self, tab_name, is_multi_tab=False, is_multi_elements=False):
        """
        按Tab选择不同日期区间，样例详见：系统管理→系统配置管理→后台服务监测
        :param tab_name:Tab页名称
        :param is_multi_tab:
        :param is_multi_elements:
        """
        if tab_name.find(';') >= 0:
            ls_items = tab_name.split(';')
            tab = ls_items[2]
            tab = tab if len(tab) > 0 else ls_items[1]
        else:
            tab = tab_name
        self.clickTabPage(tab, is_multi_tab, is_multi_elements)
        sleep(0.2)

    def get_para_value(self, para):
        """
        提取页面元素配置值，目前只针对单选框及输入框（包括日期型）
        :param para:
        :return:
        """
        if para.find(';') >= 0:
            ls_items = para.split(';')
            if len(ls_items) == 2:
                value = ls_items[1]
            else:
                value = ls_items[2]
                value = value if len(value) > 0 else ls_items[1]
        else:
            value = para
        return value

    def openLeftTree(self, treeNo, is_closed=False):
        """
        打开左边树
        :param treeNo:
        :param is_closed:Flase-左边树已处于打开状态，不需要再次点开；True-左边树处于关闭状态，需先点开
        """
        # 打开左边树
        if is_closed:
            self.menuPage.displayTreeMenu()
        try:
            node = Dict(eval(treeNo))
            print(node)
            node_flag = node['NODE_FLAG']
            node_vale = node['NODE_VALE']
        except:
            # 不是数组时的默认处理
            node_flag = '01'
            node_vale = treeNo

        if node_flag == '01':  # 选择供电单位
            self.menuPage.btn_left_tree(node_vale)
        else:  # 选择其他节点
            self.menuPage.btn_user_nodes(node_flag, node_vale)  # 该方法细节待实现

    # def exists_menu(self, active_page_loc):
    #     """
    #     判断菜单是否已打开，
    #     :return: True-已打开
    #     """
    #     locator = self.format_xpath(active_page_loc, self.menu_name)
    #     return bool(self._find_element(locator, seconds=0.5, ec_mode=1))

    def input(self, values, *locators):
        """
        方法名：input
        功能：文本框输入内容

        :param values: 文本框要输入的内容
        :param locators: 元素的位置
        :return: None
        """
        try:
            if values.find(';') > -1:
                self.curr_input(values)
            else:
                element = self._find_element(locators)
                # 输入前清空文本框
                element.clear()
                element.send_keys(values)
                logger.info('文本框输入:%s', values)
        except AttributeError as e:
            logger.error('输入错误:%s', values)

    def on_page(self, page_title):
        """
        通过title断言进入的页面是否正确。
        使用title获取当前窗口title，检查输入的title是否在当前title中。
        :param page_title:
        :return: 返回比较结果（True 或 False）
        """
        return page_title in self.driver.title

    def _open(self, url, page_title):
        """
        打开页面，并校验页面链接是否加载正确
        以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
        :param url: 要访问的链接地址
        :param page_title: 被访问页面的标题
        """
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        assert self.on_page(page_title), u'打开开页面失败 %s' % url

    def open_title_url(self, is_trust=False):
        """
        定义open方法，调用_open()进行打开链接
        :param is_trust:  是否一直等待到页面真正打开
        """
        if is_trust:
            WebDriverWait(self.driver, Setting.WAIT_TIME).until(MustGetUrl(self.base_url))
        else:
            self._open(self.base_url, self.main_page_title)

    def click(self, locator):
        """
        点击(click)元素,如图标、按钮等
        :param locator: 元素的位置
        """
        # locator参数值为None或带None的元组或元组长度为0
        if locator is None or locator[0] is None or len(locator) == 0:
            # print ('curr_click')
            self.curr_click(is_multi_tab=True)
        else:
            try:
                element = self._find_element(locator)
                # print(locator, '的状态', element.get_attribute('class'))
                element.click()
                logger.info('点击元素：{}'.format(locator))
            except BaseException as e:
                logger.error('点击元素失败:{}\n{}'.format(locator, e))

    def goto_window(self, switch_mode=True):
        """
        切换到新窗口
        :param switch_mode: True-关闭其他窗口，False-保留其他窗口
        """
        # 获取所有窗口句柄
        all_handles = self.driver.window_handles
        if switch_mode:
            for handle in all_handles[:-1]:
                self.driver.switch_to.window(handle)
                print(self.driver.title)
                self.driver.close()  # 关闭窗口
        self.driver.switch_to.window(all_handles[-1])

        # # 获取当前窗口句柄
        # now_handle = self.driver.current_window_handle

    def closeBrowser(self):
        """
        方法名：closeBrowser
        说明：关闭浏览器
        """
        logger.info('关闭浏览器')
        self.driver.quit()

    def hover(self, locator):
        """
        方法名：hover
        说明：鼠标移动到某个元素上
        :param locator: 元素的xpath
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            above = self._find_element(locator)
            ActionChains(self.driver).move_to_element(above).perform()
        except NameError as ex:
            logger.error('悬停失败：{}'.format(ex))

    def goto_frame(self, frame_obj=0):
        """
        进入iframe层
        :param frame_obj:frame序号，name， id or (By.TAG_NAME, '')
        """
        logger.info('进入 %s 的iframe层', frame_obj)
        object = frame_obj
        if isinstance(frame_obj, tuple):
            object = self._find_element(frame_obj)
        return self.driver.switch_to.frame(object)

    def goto_parent_iframe(self):
        """
        回到iframe上一层
        """
        logger.info('回到iframe上一层')
        self.driver.switch_to.parent_frame()

    def goto_home_iframe(self):
        """
        回到ifrmae开始的地方
        """
        logger.info('回到ifrmae开始的地方')
        self.driver.switch_to.default_content()

    def exec_script(self, src):
        """
        方法名：exec_script
        执行js脚本
        :param src:js脚本
        """
        self.driver.execute_script(src)

    # def invisible_element(self,wait_time =Setting.WAIT_TIME, *locator):
    #     """
    #     方法名：invisible_element
    #     确认元素是否可见
    #     :param locator:
    #     :param wait_time:
    #     :return:返回布尔值
    #     """
    #     return WebDriverWait(self.driver, wait_time).until(EC.invisibility_of_element_located(*locator))

    def get_titile(self):
        """
        方法名：get_titile
        获取当前页面标题
        :return:返回当前页面标题
        """
        return self.driver.title

    def get_current_url(self):
        """
        方法名：get_current_url
        获取当前页面URL
        :return:返回页面当前url地址
        """
        return self.driver.current_url()

    # def exists_element(self, locator, ec_mode=0):
    #     """
    #     方法名：exists_element
    #     判断元素是否存在,
    #     :param locator:元祖形式的xpath
    #     :return:布尔返回值
    #     """
    #     return bool(self._find_element(locator, ec_mode))

    # def checkbox_is_selected(self, locator):
    #     """
    #     方法名：checkbox_is_selected
    #     判断checkBox元素是否被选择
    #     :param locator:元祖形式的xpath
    #     :return:布尔返回值
    #     """
    #     return True if (self._find_element(locator).is_selected()) else False

    def open_url(self):
        """
        方法名：open_url
        打开被测服务地址
        :return:
        """
        try:
            self.driver.maximize_window()
            self.driver.get(self.base_url)
            logger.info('打开被测试服务地址：%s', self.base_url)
            return self.driver
        except NameError as e:
            logger.error('%s打开网址失败', self.base_url)

    def sleep_time(self, times):
        """
        休眠
        :param times: 休眠时间
        :return: 无
        """
        logger.info('休眠 %s 秒', times)
        sleep(times)

    def select(self, idx_or_text, locators):
        """
        选择下拉框
        :param locators: 元祖存放元素的xpath
        :param idx_or_text: 内容或下标
        :return:
        """
        try:
            # if type(idx_or_text) == int:
            if isinstance(idx_or_text, int):  # 数据类型判断新方法：isinstance
                Select(self._find_element(locators)).select_by_index(idx_or_text)
                logger.info('按下标选择下拉框,选中第:%s', idx_or_text)
            else:
                Select(self._find_element(locators)).select_by_visible_text(idx_or_text)
                logger.info('按内容选择元素，选中内容为:%s', idx_or_text)

        except NameError as e:
            logger.error('选择下拉框失败')

        # 保存图片

    def get_windows_img(self, name):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹Screenshots下
        """
        file_path = Setting.SHOT_PATH
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + name + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(
                'Had take screenshot and save to folder : /screenshots')
        except NameError as e:
            logger.error('Failed to take screenshot! %s', e)
            self.get_windows_img(screen_name)

    def _find_elements(self, locator):
        """
        校验一组元素
        :param locator:
        :return: 查找元素个数
        """
        elements = None
        try:
            except_type = ''
            elements = self.driver.find_elements(*locator)
        except NoSuchElementException as nse:
            except_type = '找不到元素'
            except_info = nse
            logger.info('显示区未查询到结果')
        except Exception as ex:  # 无法确定是哪类异常时用基类异常来捕获
            except_type = '其他错误'
            except_info = ex
        if except_type != '':
            DataAccess.el_operate_log(self.menu_no, self.tst_case_id, locator, self.class_name, except_type, except_info)
        return elements

    def wait(self):
        """
        等待页面加载完成
        :return:
        """
        self.driver.implicitly_wait(Setting.WAIT_TIME)

    def clean_screen(self, locators=None):
        """
        登录成功失败判断与清屏处理（如，告警提示框等）
        """
        if bool(locators):
            # 重要信息推出窗口关闭 LoginLocators
            el = self._find_displayed_element(locators.DLG_IMPORT)
            if bool(el):
                el.click()

            # 账号异常信息弹窗确认
            el = self._find_displayed_element(locators.DLG_EXCEPT)
            if bool(el):
                el.click()

    def refreshPage(self, is_clean_screen=True, locators=None):
        """
        刷新页面
        """
        self.driver.refresh()
        sleep(2)
        if is_clean_screen:
            self.clean_screen(locators)

    def clear(self, locator):
        """

        :param locator:
        :return:
        """
        self._find_element(locator).clear()

    def assert_body(self, value):
        txt = self._find_element((By.TAG_NAME, 'body')).text
        return value in txt

    def clear_values(self, cv):
        """
        inputSel_XXX    下拉选择框 --
        inputDt_XXX     日期输入框
        inputStr_XXX    文本输入框 --
        inputRSel_XXX   必选下拉选择：已定义/未定义,必须用下标
        inputCSel_XXX
        """
        for item in tuple(cv.__dict__.items()):
            temp = item[0]
            obj = getattr(self, temp)
            if ((temp.startswith('inputSel_')) and callable(obj)):
                obj('全部')
            elif ((temp.startswith('inputStr') or temp.startswith('inputDt'))
                  and callable(obj)):
                obj('')
            elif (temp.startswith('inputCStr') and callable(obj)):
                obj('c')
            elif (temp.startswith('inputRSel')) and callable(obj):
                obj(1)

    def get_select_locator(self, locator, num):
        """
        用于下拉菜单选择元素定位
        :param locator:xpath变量
        :param num:带定位下拉序号
        :return: 返回locator
        """

        return (locator[0], locator[1] % num)

    def bock_wait(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))

    def find_element_by_tag_name(self, value):
        """
        通过tag_name定位元素
        :param value:
        :return:
        """
        element = self.driver.find_element_by_tag_name(value)
        # print(len(element))
        return element

    def recoverLeftTree(self):
        self.menuPage.recoverLeftTree()

        # num = self._find_elements(MenuLocators.TREE_MINUS)
        # if self.assert_context(MenuLocators.TREE_END) is False:
        #     pass
        #
        # else:
        #     counter = len(num) - 1
        #     while counter >= 0:
        #         if num[counter] is MenuLocators.TREE_END:
        #             self.click(MenuLocators.TREE_END)
        #         else:
        #             num[counter].click()
        #         counter = counter - 1
        #     self.click(MenuLocators.TREE_END)

    def assertTableOne(self):
        try:
            return self.assert_context((By.XPATH, '(//*[@class="x-grid3-row-table"])[1]'))
        except NameError as e:
            print('获取显示区第一个列数据失败')
            return False

    def btn_confirm(self):
        """
        点击确认按钮
        """
        try:
            self.commonWait(BaseLocators.BTN_CONFIRM)
            self.driver.find_element(*BaseLocators.BTN_CONFIRM).click()
        except Exception as e:
            print('')

    def closePages(self, page_name='工作台', isCurPage=True):
        """
        通过工作台或定位菜单页面，关闭当前页面或除当前页面外其他页面
        :param page_name: 当“工作台”时相当于清屏操作：即关闭所有窗口
        :param isCurPage:True-关闭其他所有页；False-关闭当前页
        """
        self.menuPage.closePages(page_name, isCurPage)

        # # ****定位到要右击的元素**
        #
        # loc = self.format_xpath(MenuLocators.CURRENT_MENU, page_name)
        #
        # right_click = self.driver.find_element(*loc)
        # # 鼠标右键操作
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
        # sleep(2)
        # ActionChains(self.driver).context_click(right_click).perform()
        #
        # # 待定位右键菜单
        # forMenu = '关闭其他所有页' if isCurPage or page_name == '工作台' else '关闭当前页'
        # loc = self.format_xpath(MenuLocators.CLOSE_PAGES, forMenu)
        # pe = self.format_xpath(MenuLocators.CLOSE_PAGES_SPE, forMenu)
        #
        # try:
        #     WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
        # except:
        #     loc = pe
        #     print(loc)
        # self.driver.find_element(*loc).click()

    @staticmethod
    def format_xpath(xpath, format_val):
        """
        格式化xpath：(By.XPATH,'//*[@id=abc]//*[contains(text(),"%s"])
        按%s：只支持字符串
        按{}：支持字符串或元组
        :param xpath: 待格式化的xpath
        :param format_val: 格式化值，可以是单个字符串，元组
        :return:
        """
        if xpath[1].find('%s') > -1:  # 'abc%s' 格式
            # print('xpath:', xpath, 'format val', format_val)
            return (xpath[0], xpath[1] % format_val)
        if isinstance(format_val, tuple):
            return (xpath[0], xpath[1].format(*format_val))
        else:  # 'abc{}' 格式
            return (xpath[0], xpath[1].format(format_val))

    def displayTreeMenu(self):
        """
        打开左边树菜单栏
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MenuLocators.BTN_LEFT_MENU))
            el = self.driver.find_element(*MenuLocators.BTN_LEFT_MENU)
            if el.is_displayed():  # 左边树没显示时打开
                el.click()
        except:
            print('左边树菜单栏已经打开')

    def delDropdownBoxHtml(self):
        """
        删除下拉框的html标签
        :return:
        """
        try:
            js = "var elem = document.getElementsByClassName('xst')[0];" + \
                 'elem.parentNode.removeChild(elem);'
            self.exec_script(js)
            js2 = "var elem = document.getElementsByClassName('x-combo-list-inner')[0];" + \
                  'elem.parentNode.removeChild(elem);'
            self.exec_script(js2)
        except NoSuchElementException:
            print('删除下拉框的html标签失败')

    def clickAlert(self):
        self.driver.switch_to.alert.accept()

    def clickCancel(self):
        self.driver.switch_to.alert.dismiss()

    def commonWait(self, locator):
        """
        显示等待
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))


    def checkBoxAssertLine(self, value):
        xp = '// *[text() =\'{}\']/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]/ancestor::div[@class="x-grid3-viewport"]//*[@class="x-grid3-header"]//td'.format(
            value)
        el = self._find_elements((By.XPATH, xp))
        dl = 0
        l = 0
        for i in el:
            l += 1
            if value in i.text:
                dl = l - 1
                break
        return dl

    def rightClick(self, locators):
        """
        右键点击元素
        :param locators: 传入xpath即可
        :return:
        """
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locators))
        right_click = self.driver.find_element(*locators)
        ActionChains(self.driver).context_click(right_click).perform()

    def assert_context(self, locators, Num=0):
        """
        断言
        :param locators: 校验的值
        :return: 布尔返回值
        """
        try:

            if Num == 0:

                try:

                    el = WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'程序异常')]")))
                    res = self.driver.find_element(*(By.XPATH, "//span[contains(text(),'程序异常')]")).is_displayed()
                    if res:
                        print('弹出程序异常错误')
                        self.btn_confirm()
                        return False
                except:
                    print('')
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(locators))
            return self.driver.find_element(*locators).is_displayed()
        except:
            return False

    def assertValue(self, assertValues):
        """
        assertValues ='手机,外包队伍名称,test'
        :param assert_values:以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
        """
        print('-------------------')
        try:
            # 显示区是否有值
            xpath_table = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(assertValues[0])
            self.commonWait((By.XPATH, xpath_table))
            # 显示区查询出多少结果数量
            displayNum = len(self._find_elements((By.XPATH, xpath_table)))
            try:
                xpath_checker = '//*[@class="x-grid3-row-checker"]'
                displayCheck = self.assert_context((By.XPATH, xpath_checker))
            except:
                print('没有弹出确定按钮')
            diplayName = self.checkBoxAssertLine(assertValues[1])  # 判断具体是哪一行
            ringhtNum = 0
            displayLineElement = '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]//*[contains(text(),"{3}")]'
            if displayNum > 0:
                if displayCheck:

                    for i in range(1, displayNum + 1):
                        # 显示区结果的每一行对应列的数据的xpath
                        displayLineElement_index = displayLineElement.format(assertValues[0], i, diplayName + 1,
                                                                             assertValues[2])
                        try:
                            assert_rslt = self.assert_context((By.XPATH, displayLineElement_index), Num=1)
                            if assert_rslt:
                                ringhtNum += 1
                            else:
                                print('第{0}行，{1}列显示的值与{2}不一致'.format(i, assertValues[1], assertValues[2]))
                                break
                        except:
                            print('校验失败')
                    return ringhtNum == displayNum

                elif not displayCheck:  # 非带有复选框显示区
                    for i in range(1, displayNum + 1):
                        # 显示区结果的每一行对应列的数据的xpath
                        displayLineElement_index = displayLineElement.format(assertValues[0], i, diplayName + 1,
                                                                             assertValues[2])
                        try:
                            assert_rslt = self.assert_context((By.XPATH, displayLineElement_index))
                            if assert_rslt:
                                ringhtNum += 1
                            else:
                                print('第{0}行，{1}列显示的值与{2}不一致'.format(i, assertValues[1], assertValues[2]))
                                break
                        except:
                            print('校验失败')

                    return ringhtNum == displayNum
        except:
            print('显示区结果值校验失败')

    def clickSkip(self, assertValues):
        """
        AssertValues ='手机,外包队伍名称,test'
        :param assertValues:
        以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
       """
        try:
            displayElement = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(
                assertValues[0])
            self.commonWait((By.XPATH, displayElement))
            display_num = len(self._find_elements((By.XPATH, displayElement)))
            if display_num > 0:
                # try:
                #     sel = '//*[@class="x-grid3-row-checker"]'
                #
                #     displayCheckbox = self.assert_context((By.XPATH, sel))  # 判断显示区是有复选框的还是没有复选框的
                #     print('显示区有复选框')
                # except:
                #     print('显示区没有复选框')
                if 1:
                    lineName = self.checkBoxAssertLine(assertValues[1])  # 判断是那一列
                    displayLine = '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]'.format(
                        assertValues[0], 1, lineName + 1)
                    try:
                        self.click((By.XPATH, displayLine))
                        # 把弹出的确定框点掉

                        self.btn_confirm()

                        try:
                            skipMenuName = "//span[@class=\"x-tab-strip-inner\"]/span[contains(text(),'{}')]".format(
                                assertValues[2])
                            result = self.assert_context((By.XPATH, skipMenuName))  # 判断跳转菜单页是否存在
                            if 1:
                                self.closePages(page_name=assertValues[2], isCurPage=False)  # 关闭跳转菜单页
                            return result
                        except BaseException:
                            pass
                    except:
                        print('跳转验证失败')

                # elif displayCheckbox == False:
                #     gl = self.checkBoxAssertLine(va[1])
                #     for i in range(1, num + 1):
                #         val2 = "(//*[text()=\'{0}\']/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]//*[contains(text(),'{3}')]".format(
                #             va[0], i, gl + 1, va[2])
                #         try:
                #             hl = self.assert_context((By.XPATH, val2))
                #             if hl == True:
                #                 num2 += 1
                #             else:
                #                 print('第{0}行，{1}列显示的值与{2}不一致'.format(i, va[1], va[2]))
                #                 break
                #         except:
                #             print('校验失败')
                #
                #     if num2 == num:
                #         return True
                #     else:
                #         return False

        except:
            print('验证失败')

    def check_query_result(self, para):
        """
        查询结果校验
        :param para:
        :return:item
        """
        esplain = {'11': '显示区未查询出结果', '12': '按条件查询出的结果与期望值不一致', '21': '跳转页面不正确'}
        rslt = DataAccess.get_case_result(para['TST_CASE_ID'])
        Display_tab = '// *[text() =\'{}\']/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'  # 根据XPATH判断显示区是否有值
        ls_check_rslt = {}
        for row in rslt:  # 根据rslt有几个值来判断要做几次校验
            assert_type = row[0]
            if assert_type == '11':
                assert_rslt = self.assert_context((By.XPATH, Display_tab.format(row[1])))  # 判断是否有值
            elif assert_type == '12':
                assert_rslt = self.assertValue(row[1:])  # 判断值是否准确,item截取字符串，在转换成列表
            elif assert_type == '21':
                assert_rslt = self.clickSkip(row[1:])  # 判断跳转的页面是否是指定页面,item截取字符串，在转换成列表
            ls_check_rslt.update({assert_type: assert_rslt})

        result = True
        # 处理判断结果，具体那一步出错
        for item in ls_check_rslt.items():
            if item[1] == False:
                print(esplain[item[0]])  # 出错具体原因
                result = item[1]
                break

        return result

    def check_query_criteria(self, para):
        """
        查询条件有效性校验（含安全）
        :param para:
        :return:
        """

        result = True
        return result

    def waitLeftTree(self):
        locators = (By.XPATH, '//*[@class="x-tree-ec-icon x-tree-elbow-plus"]')

        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locators))


if __name__ == '__main__':
    # dr = webdriver.Chrome()
    # el = dr.find_element(*(By.XPATH, '')).get_attribute('class')
    # el.is_selected()
    # #
    # # p = Page(dr)
    # # # jjjjjj
    # #
    # # p.clear_values(Page)
    # # p.base_url = 'hhhhhhhhhhh'
    #
    # print(loc1)
    page = Page(None)
    page._clean_blank('查询')
    # print(page.format_xpath_multi((By.XPATH, 'adad{}'), 'c', False))
    # pg = Page(None)
    # pg.clickSingleCheckBox('忽略历史版本;')

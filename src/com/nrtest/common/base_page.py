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
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.dictionary import Dict
from com.nrtest.common.logger import Logger
from com.nrtest.common.setting import Setting
from com.nrtest.common.user_except import AssertError
from com.nrtest.common.utils import Utils
from com.nrtest.sea.locators.other.base_locators import *

# create a logger instance
logger = Logger(logger='Page').getlog()


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
        self.province_no = DataAccess.get_province()
        if bool(menu_page):
            self.menu_no = menu_page.menu_no
            self.menu_name = menu_page.menu_name
            self.menu_path = menu_page.menu_path
            self.is_call_left_tree = False
            # 提取点查询按钮后报共性异常对话框信息
            self.except_dlgs = DataAccess.get_data_dictionary('EXCEPT_DLG')

            # 跳转时目标页面报错信息
            self.skip_except_dlg = []
        else:
            self.menu_no = ''
            self.menu_name = ''
            self.menu_path = ''
        self.tst_case_id = None
        self.class_name = ''

        if self.project_no == 'SEA':
            self.baseLocators = BaseLocators
        elif self.project_no == 'SEA2.0':
            self.baseLocators = BaseSEA20Locators
        elif self.project_no in (['PBS5000', 'D5000']):
            self.baseLocators = BasePbsLocators
        elif self.project_no.endswith('JLZDH'):
            self.baseLocators = BaseJLZDHLocators

    def save_img(self, img_path, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_path:
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file(img_path + img_name)

    def popup(self, img_path, img_name, dlg_title='', *args):
        """
        捕获弹窗信息，并判断处理
        :param img_path:截图存放路径
        :param img_name: 截图文件名
        :param *args: 测试用例外的其他途径弹窗判断：01-点击菜单直接弹窗报错；
        :return: 弹窗信息，弹窗按钮，辅助信息（有弹窗只截图，不抛异常）
        """

        def find_except_dlg(info):
            # 弹窗是共性报错弹窗
            is_find = False
            for dlg in self.except_dlgs:
                is_find = dlg in info
                if is_find:
                    break
            return is_find

        action = '00'
        info = ''
        # dlg_src:1-一般用例；2-查询条件有效性用例;3-点菜单时报错；4-add_test_img弹窗处理;5-左边树选择弹窗;6-查询结果跳转异常
        if len(args) > 0:  # 带参弹窗处理优先级高于用例优先级
            dlg_src = int(args[0])
        else:
            dlg_src = int(self.case_para['CASE_TYPE'])  # 用例类型：1-一般用例；2-查询条件有效性检查用例

        # 账号异常信息弹窗属正常临时弹窗，不许特殊处理，发现时关闭即可
        self.close_account_except_dlg()

        el = self._direct_find_element(self.baseLocators.POPUP_DLG)
        if bool(el) and el.is_displayed():  # 有对话框，且显示
            info = '\r'.join(el.text.replace(' ', '').split('\n')[:6])  # [:-2])  # 有些正常弹窗数据太多
            # if '账号异常信息' in info:  # 测试用例执行过程中的“账号异常信息”弹窗属正常情况，不予处理
            #     action = '03'
            # elif dlg_src in (1, 3, 4, 6):  # 对info信息解析处理，如，对查询条件有效性判断处理，有效时不需要抛异常
            if dlg_src in (1, 3, 4, 6):  # 对info信息解析处理，如，对查询条件有效性判断处理，有效时不需要抛异常
                # action：00-没弹窗,正确结果；01-截图，且抛异常；02-只截图，不抛异常；
                #         03-既不截图，也不抛异常; 04-没弹窗时，也截图，抛异常
                # 01-针对普通用例、不符合期望值的弹窗有效性判断、点击菜单异常；02-有弹窗，但不想抛异常；
                # 03-针对符合期望值的弹窗有效性判断；
                action = '01'
                if dlg_src == 1:
                    if not find_except_dlg(info):
                        popup_type = self.case_para['POPUP_TYPE']
                        if popup_type > '00':
                            dlg_info = self.case_para['EXPECTED_RST']
                            if dlg_info in info:
                                # POPUP_TYPE:01-报错弹窗；02-没查询结果的提示弹窗；09-其他普通弹窗
                                action = '01' if popup_type == '01' else '03'
                            else:
                                info = '期望提示框信息：' + dlg_info + '\r实际提示信息' + info
                elif dlg_src == 6:
                    action = '03' if bool(dlg_title) and dlg_title in info.split('\r')[0] else '02'  # 处理符合期望的正常弹窗不要截图
                    key = '01' if find_except_dlg(info) else '02'
                    self.skip_except_dlg.append([key, info])
            elif dlg_src == 5:
                action = '01'
                # case_type = int(self.case_para['CASE_TYPE'])
                if 'EXPECTED_VAL' in self.case_para and self.case_para['EXPECTED_VAL'] in info:  # 对话框信息与期望值一致
                    action = '03'

            elif dlg_src == 2:
                if 'EXPECTED_VAL' in self.case_para and self.case_para['EXPECTED_VAL'] in info:  # 对话框信息与期望值一致
                    action = '03'
                else:  # 有对话框，但与期望值不一致
                    action = '01'

            if action in ('01', '02'):
                self.save_img(img_path, img_name)

            # btn_el = self._direct_find_element(self.baseLocators.POPUP_DLG_CONFIRM)
            btn_el = self._direct_find_element(self.baseLocators.POPUP_DLG_PLUS)
            if bool(btn_el):
                btn_el.click()

        elif dlg_src == 1:
            popup_type = self.case_para['POPUP_TYPE']
            if popup_type > '00':  # 期望有弾窗
                action = '04'
                info = '期望有提示框，且提示信息为：' + self.case_para['EXPECTED_RST']
                self.save_img(img_path, img_name)

        elif dlg_src == 2:
            if 'EXPECTED_VAL' in self.case_para and bool(self.case_para['EXPECTED_VAL']):  # 期望异常对话框
                action = '04'
                info = '期望有提示框，且提示信息为：\r' + self.case_para['EXPECTED_VAL']
                self.save_img(img_path, img_name)

        return dlg_src, action, info

    def get_skip_except_info(self, info_format='00'):
        """
        获取skip跳转弹窗异常信息
        :return: None-没弹窗异常发生；否则有弹窗异常，返回数据是个字典，格式如下：
                key：01-明确为异常弹窗；02-其他未知弹窗
                value：弹窗信息
        """
        dlg_info = self.skip_except_dlg.pop() if bool(self.skip_except_dlg) else None
        info = dlg_info
        if bool(dlg_info):
            if info_format == '01':  # 只返回弹窗标题
                info = dlg_info[1].split('\r')[0]
        return info

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

    def _element_ec_mode(self, locator, seconds=5, ec_mode=1):
        """
        不同元素等待模式
        :param locator:
        :param seconds:超时秒数
        :param ec_mode:等待元素模式：0-不做任何等待；1-判断元素是否可点击；2-判断元素是否已加载出来；3-判断元素是否可见
        :return:
        """
        if ec_mode == 1:
            # 判断元素是否可点击
            WebDriverWait(self.driver, seconds).until(EC.element_to_be_clickable(locator))
        elif ec_mode == 2:
            # 判断元素是否已加载出来
            WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(locator))
        elif ec_mode == 3:
            # 判断元素是否可见
            WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(locator))

    def _find_element(self, locator, seconds=5, ec_mode=1):
        """
        功能：定位元素的具体某个元素WEBelement
            presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
            visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
        :param locator: 元素的位置
        :param seconds:
        :param ec_mode:等待元素模式：0-不做任何等待；1:判断元素是否可点击;2:判断元素是否已加载;3:判断元素是否可见
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
        # 江西现场存在整点web服务无反应情况 2019-03-11
        if self.province_no == 'JX':
            date_time = time.localtime()
            # print(date_time)
            if date_time.tm_min > 57:
                sleep(60 * 5)  # 休眠4分钟

        # 关闭用例执行过程中账号异常弹窗
        self.close_account_except_dlg()

        # print(class_path)
        self.class_name = class_path.split('src')[1][1:]
        self.case_para = para
        self.tst_case_id = para['TST_CASE_ID']
        self.timeout_seconds = int(para['TIMEOUT_SECONDS'])

        print('开始执行... </br>')
        info = '用例ID：{}；菜单编号：{}；菜单路径：{}；Tab页名称：{}'.format(self.tst_case_id, self.menu_no, self.menu_path, para['TAB_NAME'])
        print(info + '</br>')

        logger.info('开始执行...\r')
        logger.info(info + '\r')

    def end_case(self):
        """
        测试用例执行结束
        :param para:
        """
        print('结束... </br>')
        logger.info('结束... \r')

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

    def format_xpath_multi(self, xpath, format_val='', is_multi_tab=True, menu_name=''):
        """
        应用于多Tab页情况下的xpath格式化
        :param xpath:
        :param format_val:可以是字符串、元组
        :return:
        """
        loc = xpath
        if is_multi_tab:
            menu_name = menu_name if bool(menu_name) else self.menu_name
            xpath_str = self.baseLocators.MENU_PAGE_ID.format(menu_name) + self.baseLocators.MULTI_TAB
            if xpath[1].startswith('('):
                loc = (xpath[0], xpath[1][:1] + xpath_str + xpath[1][1:])
            else:
                loc = (xpath[0], xpath_str + xpath[1])
        return self.format_xpath(loc, format_val)

    def get_province(self):
        return DataAccess.get_province()

    def ignore_op(self, value):
        """
        用于判断处理是否忽略针对当前元素的操作
        :param value:
        :return:
        """
        return value == 'IGNORE_VAL'

    def curr_input(self, values, is_multi_tab=False, is_multi_elements=False):
        """
        新版输入查询条件操作
        :param values:要输入的值
        :param is_multi_tab:菜单面内是否有多个TAB页
        :param is_multi_elements:菜单面内是否有多个重复元素
        """
        if self.ignore_op(values):
            return
        try:
            ls_values = values.split(';')
            loc = self.format_xpath_multi(self.baseLocators.QRY_INPUT, ls_values[0], is_multi_tab)
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
        if self.ignore_op(value):
            return
        try:
            ls_values = value.split(';')
            # print(ls_values)
            loc = self.format_xpath_multi(self.baseLocators.QRY_DT_INPUT, ls_values[0], is_multi_tab)
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

    def click_by_js(self, obj, idx=1):
        """
        通过JavaScript单击（click）元素
        :param obj:
        :param idx:
        """
        if isinstance(obj, WebElement):
            el = obj
        else:
            el = self._find_displayed_element(obj, idx)

        js = '''var event1 = document.createEvent("HTMLEvents"); 
                              event1.initEvent("click", true, true); 
                              event1.eventType = "message"; /*这行代码可能能删除*/ 
                              arguments[0].dispatchEvent(event1);'''
        self.driver.execute_script(js, el)

    def curr_click(self, is_multi_tab=False, btn_name='', idx=1, is_by_js=False):
        """
        新版点击方法
        :param is_multi_tab:菜单面内是否有多个TAB页
        :param btn_name:按钮元素文本值
        :param idx:第idx个可见按钮
        :param is_by_js:True-通过js触发click操作；False-用传统方法click
        """
        try:
            btn_name = btn_name if bool(btn_name) else '查询'
            loc = self.format_xpath_multi(self.baseLocators.BTN_QRY, btn_name, is_multi_tab)
            if is_multi_tab:
                el = self._find_displayed_element(loc, idx)
            else:
                el = self._find_element(loc)

            if is_by_js:
                # js = '''var event1 = document.createEvent("HTMLEvents");
                #       event1.initEvent("click", true, true);
                #       event1.eventType = "message"; /*这行代码可能能删除*/
                #       arguments[0].dispatchEvent(event1);'''
                # self.driver.execute_script(js, el)
                self.click_by_js(el)
            else:
                el.click()

            logger.info('点击元素：{}'.format(loc))
        except BaseException as e:
            logger.error('点击元素失败:{}\n{}'.format(loc, e))
        return el

    def get_input_val(self, values, use_share_xpath='01', option_name='', menu_name='', idx=1):
        """
        获取查询条件值
        :param values:要输入的值
        :param use_share_xpath:
        :param option_name:
        :param menu_name: 填跳转后的菜单名
        """
        # print('SETUP-6-1', values, use_share_xpath, option_name, menu_name)
        if self.ignore_op(values):
            return None
        try:
            if use_share_xpath in ('04', '05', '07'):
                return self.get_chk_val(values, use_share_xpath, menu_name, idx)
            else:
                # print('SETUP-6-2 label_name:{}'.format(label_name))
                if use_share_xpath == '06':  # 日期
                    loc = self.format_xpath_multi(self.baseLocators.QRY_DT_INPUT, '', True, menu_name)
                    idx = int(option_name) if bool(option_name) else 1
                    # print('SETUP-6-3-1', loc)
                else:
                    label_name = values.split(';')[0]
                    loc = self.format_xpath_multi(self.baseLocators.QRY_INPUT, label_name, True, menu_name)
                    # print('SETUP-6-3-2', loc)
                # print('菜单', self._direct_find_element((By.XPATH, '//li[@id="maintab__报文分析工具"]')))
                el = self._find_displayed_element(loc, idx)
                # print('SETUP-6-4', el)
                value_of_el = self.driver.execute_script("return arguments[0].value", el)  # self.get_el_text(el)
                logger.info(
                    '******** 查询条件（values）：{}, use_share_xpath：{}, option_name：{}, idx：{}, 查询条件值：{}\r'.format(values, use_share_xpath, option_name,
                                                                                                              idx,
                                                                                                              value_of_el))
                return value_of_el
        except AttributeError as ex:
            logger.error('提取元素内容失败:{}\n{}'.format(values, ex))
            return None

    def get_chk_val(self, values, use_share_xpath='01', menu_name='', idx=1):
        """
        获取查询条件值
        :param values:要输入的值
        :param use_share_xpath:
        :param menu_name: 填跳转后的菜单名
        """
        # print('SETUP-6-1', values, use_share_xpath, option_name, menu_name)
        if self.ignore_op(values):
            return None
        try:
            if use_share_xpath == '04':  # 单选框              QRY_RADIO_CHECKED
                loc = self.format_xpath_multi(self.baseLocators.QRY_RADIO_CHECKED, values, True, menu_name)
                el = self._find_displayed_element(loc, idx)
                value_of_el = values if bool(el) else ''
            elif use_share_xpath in ('05', '07'):  # 复选框
                ls_values = values.split(',')
                value_of_el = ''
                for value in ls_values:
                    loc = self.format_xpath_multi(self.baseLocators.QRY_CHK_CHECKED, value, True, menu_name)
                    el = self._find_displayed_element(loc, idx)
                    value_of_el += ',' + (value if bool(el) else '')
                value_of_el = value_of_el[1:]
            # logger.info(
            #     '******** 查询条件（values）：{}, use_share_xpath：{}, option_name：{}, idx：{}, 查询条件值：{}\r'.format(values, use_share_xpath, option_name, idx,                                                                                    value_of_el))
            return value_of_el
        except AttributeError as ex:
            logger.error('提取元素内容失败:{}\n{}'.format(values, ex))
            return None

    def query_timeout(self, locator=None, timeout_seconds=0, is_from_btn=False):
        """
        查询超时判断,当用例不配置超时时间或值为0时，不做等待超时判断
        :return: 查询耗时时间（单位：秒）
        """
        if timeout_seconds == 0:
            timeout_seconds = self.timeout_seconds
        if timeout_seconds > 0:
            start_time = time.time()
            sec = 2
            sleep(sec)
            try:
                # 找到元素，并且该元素也可见
                loc = locator if bool(locator) else self.baseLocators.DATA_LOADING
                WebDriverWait(self.driver, timeout_seconds - sec).until_not(EC.visibility_of_element_located(loc))
                end_time = time.time()
                cost_seconds = round(end_time - start_time, 2)
                except_type = ''
            except TimeoutException as te:
                end_time = time.time()
                cost_seconds = timeout_seconds
                except_type = '用例超时'
                info = '用例要求<={}秒，实际耗时>{}秒。'.format(timeout_seconds, cost_seconds)
                raise te
            except Exception as ex:
                except_type = '用例异常'
                info = ex.__str__()
                raise ex
            finally:
                if bool(except_type):
                    DataAccess.el_operate_log(self.menu_no, self.tst_case_id, '', self.class_name, except_type, info)
                if is_from_btn and except_type != '用例异常':
                    DataAccess.case_exec_log(self.tst_case_id, Utils.now_str(start_time), Utils.now_str(end_time), timeout_seconds, cost_seconds)
            return cost_seconds

    @BeautifulReport.add_popup_img()
    def btn_query(self, is_multi_tab=False, btn_name='', idx=1, is_by_js=False):
        """
        通用页面查询按钮
        :param is_multi_tab: 多Tab页时，如果查询按钮名有重复，则该值填True
        :param btn_name:按钮元素文本值
        :param idx:第idx个可见按钮
        """
        self.curr_click(is_multi_tab, btn_name=btn_name, idx=idx, is_by_js=is_by_js)
        self.query_timeout(is_from_btn=True)

    def selectDropDown(self, option, is_multi_tab=False, sleep_sec=0, is_multi_elements=False, is_equalText=False, byImg=True):
        """
        下拉单选框选择
        :param option: 参数格式：查询条件标签名;查询条件
        :param is_multi_tab: 多Tab页时，如果查询条件有重复，则该值填True
        :param sleep_sec:休眠n秒
        :param is_multi_elements:是否存在重复元素
        :param is_equalText: True-下拉选择值需完全匹配，Fase-部分匹配
        :param byImg: 存在点下拉框下拉图标时，不能弹出下拉选择的问题，True-下拉框下拉图标，False-下拉框的INPUT
        """
        if self.ignore_op(option):
            return
        if (option.find(';') == -1):
            print('............请配置查询条件的标签值............')
        else:
            ls_option = option.split(';')
            if len(ls_option) == 2:
                item = ls_option[1]
            else:
                item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]

            if bool(item):
                # 打开下拉框
                if byImg:
                    xpath = self.format_xpath_multi(self.baseLocators.SEL_CHECKBOX, ls_option[0], is_multi_tab)
                else:
                    xpath = self.format_xpath_multi(self.baseLocators.SEL_CHECKBOX_CLEAN, ls_option[0], is_multi_tab)

                if is_multi_elements:
                    el = self._find_displayed_element(xpath)
                    el.click()
                else:
                    el = self.click(xpath)

                if bool(sleep_sec):
                    sleep(sleep_sec)

                # 根据名称选择下拉框
                if is_equalText:
                    loc = self.format_xpath(self.baseLocators.DROPDOWN_OPTION_EQUAL, item)
                else:
                    loc = self.format_xpath(self.baseLocators.DROPDOWN_OPTION, item)
                el_option = self.click(loc)
                if not bool(el_option):
                    el.click()

            else:  # 选择值为空时，表示选择全部
                loc_all = self.format_xpath_multi(self.baseLocators.SEL_CHECKBOX_CLEAN, ls_option[0], is_multi_tab)
                el_all = self._find_displayed_element(loc_all)
                self.driver.execute_script("arguments[0].value=arguments[1]", el_all, '')

    def specialDropdown(self, option, locator, idx=1, locator_clean=None):
        """
        无法通过通用定位方法定位元素时，通过特殊locator定位选择
        :param option: 要选择的选项
        :param locator: 要定位的元素
        :param idx:选择定位到的第idx个元素
        :param locator_clean:全选时的清空处理
        """
        if self.ignore_op(option):
            return
        ls_option = option.split(';')
        item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]

        el = self._find_displayed_element(locator, idx)
        el.click()
        # 根据名称选择下拉框
        if bool(item):
            loc = self.format_xpath(self.baseLocators.DROPDOWN_OPTION_EQUAL, item)
            el_option = self.click(loc)
            if not bool(el_option):
                el.click()
        else:  # 选择值为空时，表示选择全部
            if bool(locator_clean):
                loc = locator_clean
            else:
                loc = (locator[0], locator[1] + '/preceding-sibling::input')
            el_all = self._find_displayed_element(loc, idx)
            self.driver.execute_script("arguments[0].value=arguments[1]", el_all, '')
            el.click()

    def specialSelCheckBox(self, options, locator=None, sleep_sec=0, checked_loc=None, is_equalText=False):
        """
        下拉复选框选择
        :param options: 参数格式：查询条件标签名;下拉选择项定位值;一组以,隔开的查询条件
        :param locator: 点击下拉框特殊处理元素
        :param sleep_sec:休眠n秒
        :param checked_loc: 已选择项定位特殊处理
        :param is_equalText: True-下拉选择值需完全匹配，Fase-部分匹配
        """
        if self.ignore_op(options):
            return
        if (options.find(';') == -1):
            print('请配置查询条件的标签值。')
        else:
            ls_option = options.split(';')
            if bool(locator):
                xpath = locator
            else:
                xpath = self.format_xpath_multi(self.baseLocators.SEL_CHECKBOX, ls_option[0], True)
            el_sel = self._find_displayed_element(xpath)
            el_sel.click()

            if bool(sleep_sec):
                sleep(sleep_sec)

            # 清除已选项
            unchek_all_path = self.format_xpath(checked_loc, ls_option[1])
            elements = self._find_elements(unchek_all_path)
            for el in elements:
                el.click()

            if len(ls_option[2]) > 0 and ls_option[2] != '全部':
                if is_equalText:
                    img_chk_loc = self.baseLocators.SEL_OPTION_EQUAL
                else:
                    img_chk_loc = self.baseLocators.SEL_OPTION
                for option in ls_option[2].split(','):
                    img_chk_xpath = self.format_xpath(img_chk_loc, option)
                    self.click(img_chk_xpath)

            # 回收下拉框
            el_sel.click()

    def specialInput(self, locator, value, idx=1):
        """
        页面元素位置变动时，会存在定位错误问题，需人工调整
        :param locator:
        :param value:
        :param idx:
        :return:
        """
        if self.ignore_op(value):
            return
        loc = self.format_xpath_multi(locator, idx, True)
        el = self._find_displayed_element(loc, idx)
        el.clear()
        el.send_keys(value.split(';')[1])

    def noLabelInput(self, value, idx=1):
        """
        输入框左边有label但没text值的定位
        :param value: 输入值
        :param idx: 第idx个此类可见输入框
        """
        if self.ignore_op(value):
            return
        # 页面元素位置变动时，会存在定位错误问题，需人工调整
        locator = self.format_xpath_multi(self.baseLocators.QRY_INPUT_NOLABEL, idx, True)
        el = self._find_displayed_element(locator, idx)
        el.clear()
        el.send_keys(value.split(';')[1])

    def _uncheck_all(self, option_name, unchecked_cls):
        """
        判断元素是否被选中
        :param option_name:下拉复选中选项，其中一个中文名称
        :param unchecked_cls:True-通过class-->-checked；False-通过src-->/checked.png
        :return:
        """
        if unchecked_cls:
            unchek_all_path = self.format_xpath(self.baseLocators.SEL_UNCHECK_ALL_CLS, option_name)
        else:
            unchek_all_path = self.format_xpath(self.baseLocators.SEL_UNCHECK_ALL, option_name)
        # print('所有选中项', unchek_all_path)
        elements = self._find_elements(unchek_all_path)
        for el in elements:
            # if el.get_attribute('src').find('/checked.gif') > -1:
            #     el.click()
            el.click()

    def selectCheckBox(self, options, is_multi_tab=False, sleep_sec=0, is_multi_elements=False, is_equalText=False, unchecked_cls=False):
        """
        下拉复选框选择
        :param options: 参数格式：查询条件标签名;下拉选择项定位值;一组以,隔开的查询条件
        :param is_multi_tab: 多Tab页时，如果查询条件有重复，则该值填True
        :param sleep_sec:休眠n秒
        :param is_multi_elements:同一菜单是否存在重复元素
        :param is_equalText: True-下拉选择值需完全匹配，Fase-部分匹配
        :param unchecked_cls:True-通过class-->-checked；False-通过src-->/checked.png
        """
        if self.ignore_op(options):
            return
        if (options.find(';') == -1):
            print('请配置查询条件的标签值。')
        else:
            ls_option = options.split(';')
            xpath = self.format_xpath_multi(self.baseLocators.SEL_CHECKBOX, ls_option[0], is_multi_tab)
            # print('selectCheckBox', 'qry_path', xpath)
            if is_multi_elements:
                el = self._find_displayed_element(xpath)
                el.click()
            else:
                self.click(xpath)

            if bool(sleep_sec):
                sleep(sleep_sec)

            # 清除已选项
            self._uncheck_all(ls_option[1], unchecked_cls)

            if len(ls_option[2]) > 0 and ls_option[2] != '全部':
                for option in ls_option[2].split(','):
                    if is_equalText:
                        img_chk_xpath = self.format_xpath(self.baseLocators.SEL_OPTION_EQUAL, option)
                    else:
                        img_chk_xpath = self.format_xpath(self.baseLocators.SEL_OPTION, option)
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
        self.driver.execute_script(self.baseLocators.JS_REMOVE_ATTR.format(attr[0].capitalize(), attr[1], obj_attr))

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
            xpath = self.baseLocators.MENU_PAGE_ID.format(self.menu_name) + self.baseLocators.QRY_DT_INPUT[1]
        else:
            xpath = self.baseLocators.QRY_DT_INPUT[1]
        # 把xpath对象中的 “ 替换为 '
        js_attr = self.baseLocators.JS_DT % xpath.replace('"', '\'')
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
                     'span': "//span[contains(text(), '{}')]",
                     'dropdown': '//div[contains(@class,\'x-layer x-combo-list \') and contains(@style,\'visible;\')]'
                     }
        clean_me = self.baseLocators.MENU_PAGE_ID.format(self.menu_name).replace('"', '\'') + clean_obj[tag_name].format(tag_text[0])
        script = self.baseLocators.CLEAN_BLANK % clean_me
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

    def clean_dropdown(self, tag_text):
        """
        清下拉选择项的空格
        :param tag_text: 标签名的部分内容
        """
        self._clean_blank(tag_text, 'dropdown')

    def scrollTo(self, obj):
        if isinstance(obj, WebElement):
            el = obj
        else:
            el = self.driver.find_element(*obj)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)

    def get_el_text(self, obj):
        """
        提取元素的text值
        :param obj: xpath 或 元素实例（WebElement）
        :return:
        """
        if isinstance(obj, WebElement):
            el = obj
        else:
            el = self.driver.find_element(*obj)
        return self.driver.execute_script('return arguments[0].innerText;', el)

    def el_is_hided(self, obj):
        """
        判断元素是否隐藏不可见
        :param obj: xpath 或 元素实例（WebElement）
        :return:
        """
        if isinstance(obj, WebElement):
            el = obj
        else:
            el = self.driver.find_element(*obj)
        # display:none;
        return self.driver.execute_script('return arguments[0].style.display;', el) == 'none'

    def clickRadioBox(self, option, is_multi_tab=False, is_multi_elements=False):
        """
        选择单选框
        :param option: 被选择项名称
        :param is_multi_tab:
        :param is_multi_elements:
        """
        if self.ignore_op(option):
            return
        try:
            if (option.find(';') == -1):
                item = option
            else:
                ls_option = option.split(';')
                item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]

            if len(item) == 0:
                raise BaseException('单选框必须指定选择项：{}'.format(option))
            xpath = self.format_xpath_multi(self.baseLocators.RADIOBOX_LABEL2INPUT, item, is_multi_tab)
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
        if self.ignore_op(options):
            return
        try:
            ls_option = options.split(';')
            item = ls_option[1]
            # 赋值选中，不赋值不选中
            is_select = bool(item)
            loc = locator if bool(locator) else self.baseLocators.SINGLE_CHECK_BOX
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
        if self.ignore_op(items):
            return
        try:
            # 撤销已选项
            xpath = self.format_xpath_multi(self.baseLocators.CHKBOX_UNCHECK_ALL, attr, is_multi_tab)
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
                    xpath = self.format_xpath_multi(self.baseLocators.CHKBOX_INPUT2LABEL, by_attr, is_multi_tab)
                    self.click(xpath)
        except BaseException as ex:
            print('点击复选框失败：{}'.format(ex))

    def clickCheckBox_new(self, options, is_multi_tab=False, data_dict=None, by_order=False):
        """
        选择多个复选框【checkBox的name或id不一致时调用此方法】
        :param options: 以逗号隔开，来实现点击多个复选框，eg:CheckBoxName='选中,未选中'
        :param is_multi_tab: 页面是否有多Tab页
        :param data_dict:复选框的所有选项列表
        """
        if self.ignore_op(options):
            return
        try:
            ls_option = options.split(';')
            ls_items = ls_option[2].split(',')
            data_dict = data_dict if bool(data_dict) else DataAccess.get_data_dictionary(ls_option[1])
            for data in data_dict:
                if by_order:
                    xpath = self.format_xpath_multi(self.baseLocators.CHECK_BOX_BY_ORDER, (ls_option[0], int(data_dict[data])),
                                                    is_multi_tab=is_multi_tab)
                else:
                    xpath = self.format_xpath_multi(self.baseLocators.SINGLE_CHECK_BOX, data, is_multi_tab=is_multi_tab)
                el = self._find_displayed_element(xpath)
                is_select = data in ls_items
                if is_select != el.is_selected():
                    el.click()
        except BaseException as ex:
            print('点击复选框失败：{}'.format(ex))

    def clickTabPage(self, tab_name, is_multi_tab=False, is_multi_elements=False, is_by_js=False):
        """
        打开Tab页
        :param tab_name:
        """
        if tab_name.find(';') >= 0:
            ls_items = tab_name.split(';')
            if len(ls_items) == 2:
                tab = ls_items[1]
            else:
                tab = ls_items[2] if bool(ls_items[2]) else ls_items[1]
        else:
            tab = tab_name

        xpath = self.format_xpath_multi(self.baseLocators.TAB_PAGE, tab, is_multi_tab)
        if is_by_js:
            self.click_by_js(xpath)
        elif is_multi_elements:
            el = self._find_displayed_element(xpath)
            el.click()
        # elif double:
        #     self.double_click(xpath)
        else:
            self.click(xpath)

    def clickDt_Tab(self, tab_name, is_multi_tab=False, is_multi_elements=False):
        """
        按Tab选择不同日期区间，样例详见：系统管理→系统配置管理→后台服务监测
        :param tab_name:Tab页名称
        :param is_multi_tab:
        :param is_multi_elements:
        """
        if self.ignore_op(tab_name):
            return

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

    def is_tree_node_first(self):
        return bool(self.get_para_value(self.case_para['TREE_NODE']))

    @BeautifulReport.add_popup_img(5)
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
            # print(node)
            node_flag = node['NODE_FLAG']
            node_value = node['NODE_VALUE']
        except:
            # 不是数组时的默认处理
            node_flag = '01'
            node_value = treeNo
        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~node_flag', node_flag)
        if node_flag in ['01', '10']:  # 01-选择供电单位tst_org；10-选择节点（tst_tree_node)
            # self.menuPage.btn_left_tree(node_value)  # 2019-03-06
            self.is_call_left_tree = True
            self.menuPage.btn_left_tree(treeNo)
        else:  # 选择其他节点
            self.menuPage.btn_user_nodes(node_flag, node_value)

    def input(self, value, *locators):
        """
        方法名：input
        功能：文本框输入内容

        :param value: 文本框要输入的内容
        :param locators: 元素的位置
        :return: None
        """
        if self.ignore_op(value):
            return
        try:
            if value.find(';') > -1:
                self.curr_input(value, True, True)
            else:
                element = self._find_element(locators)
                # 输入前清空文本框
                element.clear()
                element.send_keys(value)
                logger.info('文本框输入:%s', value)
        except AttributeError as e:
            logger.error('输入错误:%s', value)

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

    def click(self, locator, is_by_js=False):
        """
        点击(click)元素,如图标、按钮等
        :param locator: 元素的位置
        """
        # locator参数值为None或带None的元组或元组长度为0
        if locator is None or locator[0] is None or len(locator) == 0:
            # print ('curr_click')
            element = self.curr_click(is_multi_tab=True, is_by_js=is_by_js)
        else:
            try:
                element = self._find_element(locator)
                # print(locator, '的状态', element.get_attribute('class'))
                element.click()
                logger.info('点击元素：{}'.format(locator))
            except BaseException as e:
                logger.error('点击元素失败:{}\n{}'.format(locator, e))
        return element

    def goto_window(self, switch_mode=True):
        """
        切换到新窗口
        :param switch_mode: True-关闭其他窗口，False-保留其他窗口
        """
        # 获取所有窗口句柄
        all_handles = self.driver.window_handles
        # self.driver.current_url
        if switch_mode:
            for handle in all_handles[:-1]:
                self.driver.switch_to.window(handle)
                # print(self.driver.title)
                self.driver.close()  # 关闭窗口
        self.driver.switch_to.window(all_handles[-1])

        # # 获取当前窗口句柄
        # now_handle = self.driver.current_window_handle

    def goto_main_window(self, close_others=True):
        """
        返回到首页过程中的操作处理
        :param close_others: True-关闭其他窗口，False-保留其他窗口
        """
        # 获取所有窗口句柄
        all_handles = self.driver.window_handles
        if close_others:
            for handle in all_handles[1:]:
                self.driver.switch_to.window(handle)
                # print(self.driver.title)
                self.driver.close()  # 关闭窗口
        else:
            for handle in all_handles[1:]:
                self.driver.switch_to.window(handle)
                self.driver.maximize_window()
        self.driver.switch_to.window(all_handles[0])
        # print(self.driver.current_url)

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
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            # hover_obj = self._find_element(locator)
            # ActionChains(self.driver).move_to_element(hover_obj).perform()

            js = 'var evObj = document.createEvent("MouseEvents"); \
            evObj.initMouseEvent("mouseover", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null); \
            arguments[0].dispatchEvent(evObj);'

            # 请保留下面被注释的代码
            # js = 'if(document.createEvent){ \
            #         var evObj = document.createEvent("MouseEvents""); \
            #         evObj.initEvent("mouseover", true, false); \
            #         arguments[0].dispatchEvent(evObj);} \
            #       else if(document.createEventObject) { \
            #         arguments[0].fireEvent("onmouseover");}'

            hover_obj = self._find_element(locator)
            self.driver.execute_script(js, hover_obj)
        except NameError as ex:
            logger.error('悬停失败：{}'.format(ex))

    def goto_frame(self, frame_obj=0):
        """
        进入iframe层
        当一个iframe层内有多个iframe时，通过配置para['IFRAME']确认进入
        :param frame_obj:frame序号，name， id or (By.TAG_NAME, '')
        """
        logger.info('进入 %s 的iframe层', frame_obj)
        # object = frame_obj
        # if isinstance(frame_obj, tuple):
        #     object = self._find_element(frame_obj)
        if isinstance(frame_obj, str) and frame_obj.find(';') > 0:

            try:
                object = frame_obj.split(';')[1]
                object = int(object)
            except:
                object = 0
        elif isinstance(frame_obj, tuple):
            object = self._find_element(frame_obj)
        else:
            object = frame_obj
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

    def close_account_except_dlg(self):
        """
         账号异常信息弹窗确认：处理用例执行过程中临时弹出
        """
        try:
            el = self._direct_find_element(self.baseLocators.DLG_EXCEPT)
            if bool(el):
                el.click()
        except:
            pass

    def clean_screen(self):
        """
        登录成功失败判断与清屏处理（如，告警提示框等）
        """
        sleep(0.5)
        # 关闭除首页外的其他出口
        self.goto_main_window()

        sleep(1.5)
        # 登录异常弹窗确认
        el = self._direct_find_element(self.baseLocators.BTN_CONFIRM)
        if bool(el):
            el.click()

        # 重要信息推出窗口关闭
        el = self._find_displayed_element(self.baseLocators.DLG_IMPORT)
        if bool(el):
            el.click()

        # 账号异常信息弹窗确认
        el = self._find_displayed_element(self.baseLocators.DLG_EXCEPT)
        if bool(el):
            el.click()

    def refreshPage(self):
        """
        刷新页面
        """
        self.driver.refresh()
        sleep(2)
        if Setting.CLEAN_SCREEN.lower().startswith('y'):
            self.clean_screen()

    def clear(self, locator):
        """

        :param locator:
        :return:
        """
        self._find_element(locator).clear()

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
        # print('~~~~~~~~~~~~~~~~is_call_left_tree', self.is_call_left_tree)
        # sleep(10)
        if self.is_call_left_tree:
            self.is_call_left_tree = False
            self.menuPage.recoverLeftTree()

    def btn_confirm(self):
        """
        点击确认按钮
        """
        try:
            self.commonWait(self.baseLocators.BTN_CONFIRM)
            self.driver.find_element(*self.baseLocators.BTN_CONFIRM).click()
        except Exception as e:
            pass

    def closePages(self, page_name='工作台', isCurPage=True):
        """
        通过工作台或定位菜单页面，关闭当前页面或除当前页面外其他页面
        :param page_name: 当“工作台”时相当于清屏操作：即关闭所有窗口
        :param isCurPage:True-关闭其他所有页；False-关闭当前页
        """
        self.menuPage.closePages(page_name, isCurPage)

    def goto_home_page(self, menu_name=''):
        """
        PBS5000专用，回退到一级菜单
        :param menu_name:
        :return:
        """
        self.goto_home_iframe(self)
        self.menuPage.goto_home_page(menu_name)

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

    # def displayTreeMenu(self):
    #     """
    #     打开左边树菜单栏
    #     :return:
    #     """
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MenuLocators.BTN_LEFT_MENU))
    #         el = self.driver.find_element(*MenuLocators.BTN_LEFT_MENU)
    #         if el.is_displayed():  # 左边树没显示时打开
    #             el.click()
    #     except:
    #         print('左边树菜单栏已经打开')

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

    def commonWait(self, locator, seconds=5):
        """
        显示等待
        :param locator:
        :return:
        """
        WebDriverWait(self.driver, seconds).until(EC.element_to_be_clickable(locator))

    def calc_col_idx(self, loc_col_name, col_name='', idx=1):
        """
        计算所给列名（col_name）在表格中的所处位置
        --------------------loc_col_name[0]-----------------|-col_name[1]-|----[2]-------|--要定位的行号[3]--|-----[4]-----
        nvl(tab_column_name, column_name) AS tab_column_name, column_name, expected_value, row_num,          is_special
        :param loc_col_name: 能唯一定位表头的关键列名
        :param col_name: 计算列位置的列名, 如果col_name值为'', 则用loc_col_name替代
        :param idx: 第idx个可见对象
        :return: 返回：列位置，列是否可见以及第一列带标签的列
        """
        loc = self.format_xpath_multi(self.baseLocators.TABLE_HEAD, loc_col_name, True)
        el_tr = self._find_displayed_element(loc, idx=idx)
        # 如果col_name值为'', 则用loc_col_name替代
        if col_name == '':
            col_name = loc_col_name
        col_pos_info = {'COL_IDX': 0, 'EL_COL': None, 'HIDE_COLS': 0, 'FIRST_COL_IDX': 0, 'EL_FIRST': None, 'COL_IS_HIDED': True, 'HIDE_ROWS': 0}
        # 查找表头所有列名元素
        el_tds = el_tr.find_elements_by_xpath('./td')
        if bool(el_tds):
            # 隐藏列个数
            hide_cols = 0
            for i, el in enumerate(el_tds):
                el_label = self.get_el_text(el)
                el_label = Utils.replace_chrs(el_label, ' \r\n\t')
                if self.el_is_hided(el):
                    hide_cols += 1
                else:
                    if col_pos_info['EL_FIRST'] is None and el.is_displayed():
                        # 第一个带标签，且显示的列
                        col_pos_info['EL_FIRST'] = el
                        col_pos_info['FIRST_COL_IDX'] = i + 1
                    if el_label == col_name:
                        col_pos_info['COL_IS_HIDED'] = not el.is_displayed()
                        col_pos_info['EL_COL'] = el
                        # 表头列名位置，xpath元素下表以1开始，故+1
                        col_pos_info['COL_IDX'] = i + 1
                        break
            col_pos_info['HIDE_COLS'] = hide_cols
            logger.info('\r“{}”在表格中计算结果：第{}列（其中隐藏列{}列），且{}。\r'.format(col_name, col_pos_info['COL_IDX'], hide_cols,
                                                                      ('不可见' if col_pos_info['COL_IS_HIDED'] else '可见')))
            return col_pos_info
        else:
            raise AssertError('定位列{}在表格中的位置时报错！'.format(col_name))

    def select_row(self, row_item, idx=1):
        """
        定位查询结果行, 不指定row_item，则默认为第一行
        :param row_item: 数据格式：能唯一定位表头的关键列名;要定位的列名;要定位的所在列值
        :return:
        """
        row_item = row_item.split(';')[1]
        if bool(row_item):  # 指定选择行内容
            ls_row_items = row_item.split('-')
            loc_col_name = ls_row_items[0]
            if len(ls_row_items) == 2:
                col_name = loc_col_name
                col_val = ls_row_items[1]
            else:
                col_name = ls_row_items[1]
                col_val = ls_row_items[2]

            col_idx = self.calc_col_idx(loc_col_name, col_name, idx)['COL_IDX']
            xpath = self.format_xpath_multi(self.baseLocators.SELECT_ROW, (loc_col_name, col_idx, col_val))
            el = self._find_displayed_element(xpath)
            if bool(el):
                el.click()
        else:
            xpath = self.format_xpath_multi(self.baseLocators.SELECT_FIRST_ROW)
            el = self._find_displayed_element(xpath)
            if bool(el):
                el.click()

        if el is None:
            raise RuntimeError('定位不到指定行：{}'.format(row_item if bool(row_item) else '第1行'))

    def rightClick(self, locator):
        """
        右键点击元素
        :param locator: 传入xpath即可
        :return:
        """
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))
        el = self.driver.find_element(*locator)
        ActionChains(self.driver).context_click(el).perform()

    def check_query_criteria(self, para):
        """
        查询条件有效性校验（含安全）
        :param para:
        :return:
        """

        result = True
        return result

    def double_click(self, locator):
        el = self._find_element(locator)
        ActionChains(self.driver).double_click(el).perform()

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

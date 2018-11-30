# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: base_page.py
@time: 2018-05-25 0:32
@desc:
类方法说明：
 1.方法名：_find_element
        功能：定位元素的具体某个元素WEBelement

        *注释：_代表类的私有属性或方法
        :param Locators: 元素的位置
        :return: 返回定位的元素
 2.方法名：input
        功能：文本框输入内容

        :param values: 文本框要输入的内容
        :param locators: 元素的位置
        :return: None
 3.方法名：click
        功能：点击元素

        :param locators:元素的位置
        :return:None
4.方法名：get_current_url
        功能：打开测试服务器地址
        :return: None
5. 方法名：closeOldBrowser
        说明：在打开新页面时关闭旧的页面
        参数：无
6.方法名：closeBrowser
        说明：关闭浏览器
7.方法名：hover
        说明：鼠标移动到某个元素上
        :param Locators: 元素的xpath
8.方法名：switch_frame
        进入iframe层
        :param locators:元祖形式存在的iframe的id
        :return:
9.方法名：back_parent_iframe
        回到iframe上一层
        :return:无
10.方法名：back_home_iframe
        回到ifrmae开始的地方
        :return: 无
11. 方法名：exec_script
        执行js脚本
        :param src:js脚本
12.方法名：invisible_element
        确认元素是否可见
        :param locator:
        :param wait_time:
        :return:返回布尔值
13.方法名：get_titile
        获取当前页面标题
        :return:返回当前页面标题
14. 方法名：get_url
        获取当前页面URL
        :return:返回页面当前url地址
15.方法名：on_page
        通过title断言进入的页面是否正确。
        使用title获取当前窗口title，检查输入的title是否在当前title中。
        :param page_title:
        :return: 返回比较结果（True 或 False）
16.方法名：check_element_exists
        判断元素是否存在
        :param locator:
        :return:布尔返回值
17.法名：checkbox_is_selected
        判断checkBox元素是否被选择
        :param locator:元祖形式的xpath
        :return:布尔返回值
18.方法名：open_url
        打开被测服务地址

"""
import os
import time
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, InvalidElementStateException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.logger import Logger
from com.nrtest.common.setting import Setting
from com.nrtest.sea.locators.other.login_page_locators import LoginPageLocators
# create a logger instance
from com.nrtest.sea.locators.other.menu_locators import MenuLocators

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

    def __init__(self, driver, base_url=Setting.TEST_URL, pagetitle=Setting.PAGE_TILE):
        self.driver = driver
        self.base_url = base_url
        self.page_title = pagetitle

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
            if not os.path.exists(Setting.IMG_PATH):  # SNAPSHOT_DIRECTORY  #ljf
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

    def _find_element(self, *locator):
        """
        方法名：_element
        功能：定位元素的具体某个元素WEBelement
            presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
            visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
        *注释：_代表类的私有属性或方法
        :param locator: 元素的位置
        :return: 返回定位的元素
        """
        element = None
        try:
            # 利用显示等待判断元素是否已经出现
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(locator))
            # 定位元素
            element = self.driver.find_element(*locator)
        except TimeoutException as te:
            if locator[1].find('请求无响应或超时！') == -1:
                logger.error(u'等待元素超时--> %s' % locator, te)
        except NoSuchElementException as nse:
            logger.error(u'未找到元素--> %s' % locator, nse)
        except Exception as e:  # 无法确定是哪类异常时用基类异常来捕获
            logger.error(u'其他查找元素错误--> %s' % locator, e)
        return element

    def input(self, values, *locators):
        """
        方法名：input
        功能：文本框输入内容

        :param values: 文本框要输入的内容
        :param locators: 元素的位置
        :return: None
        """
        try:
            element = self._find_element(*locators)
            # 输入前清空文本框
            element.clear()
            element.send_keys(values)
            logger.info('文本框输入:%s', values)
        except AttributeError as e:
            logger.error('输入错误:%s', values)
        # return None

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
            WebDriverWait(self.driver, Setting.WAIT_TIME).until(
                MustGetUrl(self.base_url))
        else:
            self._open(self.base_url, self.page_title)

    def click(self, *locators):
        """
        点击(click)元素,如图标、按钮等
        :param locators: 元素的位置
        """
        try:
            element = self._find_element(*locators)
            element.click()
            logger.info('点击元素：{}'.format(locators))
        except BaseException as e:
            logger.error('点击元素失败:%s' % e)

    def closeOldBrowser(self):
        """
        方法名：closeOldBrowser
        说明：在打开新页面时关闭旧的页面
        参数：无

        """
        # 获取当前打开的所有窗口的句柄
        handles = self.driver.window_handles

        # 切换到第二个窗口的句柄
        self.driver.switch_to.window(handles[1])

        # 切换回主页句柄
        self.driver.switch_to.window(handles[0])
        self.driver.close()
        logger.info('关闭浏览器错误')

    def closeBrowser(self):
        """
        方法名：closeBrowser
        说明：关闭浏览器
        """
        logger.info('关闭浏览器')
        self.driver.quit()

    def hover(self, *locator):
        """
        方法名：hover
        说明：鼠标移动到某个元素上
        :param locator: 元素的xpath
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator))
            above = self._find_element(*locator)
            ActionChains(self.driver).move_to_element(above).perform()
        except NameError as e:
            logger.error('悬停失败：%s', e)

    def switch_frame(self, *locators):
        """
        方法名：switch_frame
        进入iframe层
        :param locators:元祖形式存在的iframe的id
        :return:
        """
        logger.info('进入 %s 的iframe层', locators)
        return self.driver.switch_to_frame(locators[1])

    def back_parent_iframe(self):
        """
        方法名：back_parent_iframe
        回到iframe上一层
        :return:
        """
        logger.info('回到iframe上一层')
        self.driver.switch_to.parent_frame()
        # return None

    def back_home_iframe(self):
        """
        方法名：back_home_iframe
        回到ifrmae开始的地方
        :return:
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

    # def on_page(self, page_title):
    #     """
    #     方法名：on_page
    #     通过title断言进入的页面是否正确。
    #     使用title获取当前窗口title，检查输入的title是否在当前title中。
    #     :param page_title:
    #     :return: 返回比较结果（True 或 False）
    #     """
    #     return page_title in self.driver.title

    def check_element_exists(self, *locator):
        """
        方法名：check_element_exists
        判断元素是否存在
        :param locator:元祖形式的xpath
        :return:布尔返回值
        """
        try:
            return bool(self._find_element(*locator))
        except NoSuchElementException:
            return False

    def checkbox_is_selected(self, *locator):
        """
        方法名：checkbox_is_selected
        判断checkBox元素是否被选择
        :param locator:元祖形式的xpath
        :return:布尔返回值
        """
        return True if (self._find_element(*locator).is_selected()) else False

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

    def assert_context(self, *locators):
        """
        断言
        :param locators: 校验的值
        :return: 布尔返回值
        """
        try:
            return self.driver.find_element(*locators).is_displayed()
        except:
            return False

    def sleep_time(self, times):
        """
        休眠
        :param times: 休眠时间
        :return: 无
        """
        logger.info('休眠 %s 秒', times)
        sleep(times)

    def select(self, idx_or_text, *locators):
        """
        选择下拉框
        :param locators: 元祖存放元素的xpath
        :param idx_or_text: 内容或下标
        :return:
        """
        try:
            # if type(idx_or_text) == int:
            if isinstance(idx_or_text, int):  # 数据类型判断新方法：isinstance
                Select(self._find_element(*locators)
                       ).select_by_index(idx_or_text)
                logger.info('按下标选择下拉框,选中第:%s', idx_or_text)
            else:
                Select(self._find_element(*locators)
                       ).select_by_visible_text(idx_or_text)
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

    def find_elements(self, *locator):
        """
        #校验一组元素
        :param locator:
        :return: 查找元素个数
        """
        try:
            element = self.driver.find_elements(*locator)
            return element

        except NoSuchElementException:
            logger.info('显示区未查询到结果')

    def wait(self):
        """
        等待页面加载完成
        :return:
        """
        self.driver.implicitly_wait(Setting.WAIT_TIME)

    def refreshPage(self):
        """
        刷新页面
        :return:
        """

        self.driver.refresh()
        sleep(2)
        txt = self.driver.find_element_by_tag_name('body').text

        if '重要信息推出' in txt:
            if '登录异常' in txt:
                print('-----')
                self.driver.find_element(
                    *LoginPageLocators.BTN_CONFIRM).click()
            if '账号异常信息' in txt:
                print('-----')
                self.driver.find_element(*LoginPageLocators.BTN_ARROW).click()

    def clear(self, *locator):
        """

        :param locator:
        :return:
        """
        self._find_element(*locator).clear()

    def assert_body(self, value):
        txt = self._find_element(*(By.TAG_NAME, 'body')).text
        # if value in txt:
        #     return True
        # else:
        #     return False
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
            elif (temp.startswith('inputStr') and callable(obj)):
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
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator))

    def implic_wait(self):
        self.driver.implicitly_wait(10)

    def find_element_by_tag_name(self, value):
        """
        通过tag_name定位元素
        :param value:
        :return:
        """
        element = self.driver.find_element_by_tag_name(value)
        # print(len(element))
        return element

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

    # def closeTab(self):
    #     # ****定位到要右击的元素**
    #     right_click = self.driver.find_element(*(By.XPATH,'//*[@id=\"maintab__工作台\"]'))
    #     # ****对定位到的元素执行鼠标右键操作
    #     ActionChains(self.driver).context_click(right_click).perform()
    #     self.driver.find_element(*(By.XPATH,"//div[@class=\"x-menu x-menu-floating x-layer \"]//*[contains(text(),'关闭其他所有页')]")).click()

    def recoverLeftTree(self):
        num = self.find_elements(*MenuLocators.TREE_MINUS)
        if self.assert_context(*MenuLocators.TREE_END) is False:
            pass

        else:
            counter = len(num) - 1
            while counter >= 0:
                if num[counter] is MenuLocators.TREE_END:
                    self.click(*MenuLocators.TREE_END)
                else:
                    num[counter].click()
                counter = counter - 1
            self.click(*MenuLocators.TREE_END)

    # def clickTabPage(self, name):
    #     """
    #     输入tab页名称，选中tab页
    #     :param name: tab页的中文名称
    #     :return:
    #     """
    #     try:
    #         locators = (By.XPATH, "(//*[@class=\"x-tab-strip-text \"])[contains(text(),'{}')]".format(name))
    #         self.click(*locators)
    #     except NoSuchElementException  as e:
    #         print('点击{}tab页失败'.format(name))
    #
    # def tableLineValue(self, i, l):
    #     try:
    #         str_xpath = "(//*[@class=\"x-grid3-row-table\"])[{0}]//td[{1}]".format(i, l)
    #         changeStr = self._find_element(*(By.XPATH, str_xpath)).text
    #         return changeStr
    #     except NameError as e:
    #         print('获取显示区文字失败')

    def assertTableOne(self):
        try:
            return self.assert_context(*(By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]'))
        except NameError as e:
            print('获取显示区第一个列数据失败')
            return False

    def btn_confirm(self):
        """
        点击确认按钮
        """
        try:
            self.commonWait(MenuLocators.BTN_CONFIRM)
            self.driver.find_element(*MenuLocators.BTN_CONFIRM).click()
        except Exception as e:
            print('点击确认按钮失败')

    def closePages(self, page_name='工作台', isCurPage=True):
        """
        通过工作台或定位菜单页面，关闭当前页面或除当前页面外其他页面
        :param page_name: 当“工作台”时相当于清屏操作：即关闭所有窗口
        :param isCurPage:True-关闭其他所有页；False-关闭当前页
        """

        # ****定位到要右击的元素**

        loc = self.format_xpath(MenuLocators.CURRENT_MENU, page_name)

        right_click = self.driver.find_element(*loc)
        # 鼠标右键操作
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
        sleep(2)
        ActionChains(self.driver).context_click(right_click).perform()

        # 待定位右键菜单
        forMenu = '关闭其他所有页' if isCurPage or page_name == '工作台' else '关闭当前页'
        loc = self.format_xpath(MenuLocators.CLOSE_PAGES, forMenu)
        pe = self.format_xpath(MenuLocators.CLOSE_PAGES_SPE, forMenu)

        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
        except:
            loc = pe
            print(loc)
        self.driver.find_element(*loc).click()

    @staticmethod
    def format_xpath(xpath, format_val):
        """
        格式化xpath：(By.XPATH,'//*[@id=abc]//*[contains(text(),\"%s\"])
        :param xpath: 待格式化的xpath
        :param format_val: 格式化值
        :return:
        """

        # print('xpath:', xpath, 'format val', format_val)
        return (xpath[0], xpath[1] % format_val)

    def DisplayTreeMenu(self):
        """
        打开左边树菜单栏
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MenuLocators.BTN_LEFT_MENU))
            el = self.driver.find_element(*MenuLocators.BTN_LEFT_MENU)

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

    def clickCheckBox(self, items):
        """
        选中复选框

        :param items: 以逗号隔开，来实现点击多个复选框，eg:CheckBoxName='选中,未选中'
        :return:
        """
        try:
            lis = items.split(',')
            for i in lis:
                xp = '//label[@class="x-form-cb-label"and contains(text(),"{}")]/preceding-sibling::input'.format(i)
                self.commonWait((By.XPATH, xp))
                self.driver.find_element(*(By.XPATH, xp)).click()
        except BaseException as e:
            print('点击复选框失败')
            print(e)

    def clickAlert(self):
        self.driver.switch_to.alert.accept()

    def clickCancel(self):
        self.driver.switch_to.alert.dismiss()

    def commonWait(self, locator):
        '''
        显示等待
        :param locator:
        :return:
        '''
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def AssertLine(self, value):
        xp = '// *[text() =\'{}\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"]/ancestor::div[@class=\"x-grid3-viewport\"]//*[@class=\"x-grid3-header\"]//td'.format(
            value)
        el = self.find_elements(*(By.XPATH, xp))
        l = 0
        for i in el:
            l += 1
            if value in i.text:
                dl = l - 1
                break
        return dl

    def assertValue(self, assertValues):
        """
        AssertValues ='手机,外包队伍名称,test'
        :param assert_values:
        以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
        """
        print('-------------------')
        try:
            xpath_table = '// *[text() =\'{}\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"]'.format(
                assertValues[0])  # 显示区是否有值
            self.commonWait((By.XPATH, xpath_table))
            # 显示区查询出多少结果数量
            displayNum = len(self.find_elements(*(By.XPATH, xpath_table)))
            try:
                xpath_checker = '//*[@class=\"x-grid3-row-checker\"]'

                displayCheck = self.assert_context(*(By.XPATH, xpath_checker))
            except:
                displayCheck = False
            diplayName = self.AssertLine(assertValues[1])  # 判断具体是哪一行
            ringhtNum = 0
            if displayNum > 0:

                if displayCheck == True:

                    for i in range(1, displayNum + 1):
                        displayLineElement = "(//*[text()=\'{0}\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"]//tr)[{1}]/td[{2}]//*[contains(text(),'{3}')]".format(
                            assertValues[0], i, diplayName + 1, assertValues[2])
                        try:
                            assert_rslt = self.assert_context(*(By.XPATH, displayLineElement))
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
                        displayLineElement = "(//*[text()=\'{0}\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"]//tr)[{1}]/td[{2}]//*[contains(text(),'{3}')]".format(
                            assertValues[0], i, diplayName + 1, assertValues[2])
                        try:
                            assert_rslt = self.assert_context(*(By.XPATH, displayLineElement))
                            if assert_rslt == True:
                                ringhtNum += 1
                            else:
                                print('第{0}行，{1}列显示的值与{2}不一致'.format(i, assertValues[1], assertValues[2]))
                                break
                        except:
                            print('校验失败')

                    if ringhtNum == displayNum:
                        return True
                    else:
                        return False
        except:
            print('显示区结果值校验失败')

    def rightClick(self, *locators):
        """
        右键点击元素
        :param locators: 传入xpath即可
        :return:
        """
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locators))
        right_click = self.driver.find_element(*locators)
        ActionChains(self.driver).context_click(right_click).perform()

    def clearInput(self, *Locators):
        self._find_element(*Locators).clear()

    def _uncheck_all(self, option_name):
        """
        判断元素是否被选中
        :param option_name:下拉复选中选项，其中一个中文名称
        :return:
        """
        # img_check = '//div[@class ="x-combo-list-inner"]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]'.format(
        #     option_name)
        # elements = self.find_elements(*(By.XPATH, img_check))
        # for el in elements:
        #     child_el = el.find_element(*(By.XPATH, './img'))
        #     # print('child_element ing', el.text)
        #     if child_el.get_attribute('src').find('/checked.gif') > -1:
        #         child_el.click()
        img_check = '//div[@class ="x-combo-list-inner"]//div[contains(text(),"{}")]/../..//div[@class="ux-lovcombo-item-text"]/img'.format(
            option_name)
        elements = self.find_elements(*(By.XPATH, img_check))
        for el in elements:
            if el.get_attribute('src').find('/checked.gif') > -1:
                el.click()

    def selectCheckBox(self, options, option_name=''):
        """
            not all arguments converted during string formatting:原因是元素没法定位
        :param options:
        :param option_name:
        :return:
        """
        self._uncheck_all(option_name)
        if len(option_name) > 0 and option_name != '全部':
            ls_option = options.split(',')
            img_chk_xpath = '//div[@class ="x-combo-list-inner"]//div[contains(text(),"{}")]/../div/img'
            for option in ls_option:
                self.click(*(By.XPATH, img_chk_xpath.format(option)))

    def clickSkip(self, assertValues):
        """
               AssertValues ='手机,外包队伍名称,test'
               :param AssertValues:
               以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
               :return:
               """
        try:
            displayElement = '// *[text() =\'{}\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"]'.format(
                assertValues[0])
            self.commonWait((By.XPATH, displayElement))
            display_num = len(self.find_elements(*(By.XPATH, displayElement)))
            if display_num > 0:
                try:
                    sel = '//*[@class=\"x-grid3-row-checker\"]'

                    displayCheckbox = self.assert_context(*(By.XPATH, sel))  # 判断显示区是有复选框的还是没有复选框的
                except:
                    displayCheckbox = False
                if displayCheckbox == True:
                    lineName = self.AssertLine(assertValues[1])  # 判断是那一列
                    displayLine = "(//*[text()=\'{0}\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"]//tr)[{1}]/td[{2}]".format(
                        assertValues[0], 1, lineName + 1)
                    try:
                        self.click(*(By.XPATH, displayLine))
                        # 把弹出的确定框点掉
                        try:
                            self.btn_confirm()
                        except:
                            print('没有出现确定')
                        try:
                            skipMenuName = "//*[@class=\"x-tab-strip-text \"and contains(text(),'{}')]".format(
                                assertValues[2])
                            result = self.assert_context(*(By.XPATH, skipMenuName))  # 判断跳转菜单页是否存在
                            if result == True:
                                self.closePages(page_name=assertValues[2], isCurPage=False)  # 关闭跳转菜单页
                            return result
                        except BaseException:
                            pass
                    except:
                        print('跳转验证失败')

            #
            # elif displayCheckbox == False:
            #     gl = self.AssertLine(va[1])
            #     for i in range(1, num + 1):
            #         val2 = "(//*[text()=\'{0}\']/ancestor::div[@class=\"x-grid3-viewport\"]//table[@class=\"x-grid3-row-table\"]//tr)[{1}]/td[{2}]//*[contains(text(),'{3}')]".format(
            #             va[0], i, gl + 1, va[2])
            #         try:
            #             hl = self.assert_context(*(By.XPATH, val2))
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
            #
        except:
            print('验证失败')

    def commonAssertValue(self, tst_case_id):
        """

        :param tst_case_id:
        :return:item
        """
        rslt = DataAccess.get_case_result(tst_case_id)
        Display_tab = (By.XPATH, '//table[@class=\"x-grid3-row-table\"]')  # 根据XPATH判断显示区是否有值
        for item in self.assertTstCaseResult(rslt):  # 根据rslt有几个值来判断要做几次校验

            flag = item[0]
            if flag == '11':
                haveValue = self.assert_context(*Display_tab)  # 判断是否有值
                if len(rslt) == 1:
                    return haveValue
                    break

            elif flag == '12':

                valueRight = self.assertValue(item[1:len(item)])  # 判断值是否准确,item截取字符串，在转换成列表
                print(valueRight)
                if len(rslt) == 1:
                    return valueRight
                    break
                elif valueRight == False:
                    return False


            elif flag == '21':
                skipValue = self.clickSkip(item[1:len(item)])  # 判断跳转的页面是否是指定页面,item截取字符串，在转换成列表
                return skipValue

    def assertTstCaseResult(self, rslt):
        """
        对数组进行排序，来确保先对结果值校验，在进行跳转
        :param rslt:
        :return:
        """
        new_rslt = []  # 重新排序后的列表
        index = 0
        for item in rslt:
            index += 1
            if item[0] in ('12', '11'):  # 有值和值的准确性放第一位
                new_rslt.insert(0, item)
            if item[0] in ('21', '22', '23'):  # 跳转放第二位
                new_rslt.insert(1, item)
        return new_rslt


if __name__ == '__main__':
    dr = webdriver.Chrome()
    el = dr.find_element(*(By.XPATH, '')).get_attribute('class')
    el.is_selected()
    #
    # p = Page(dr)
    # # jjjjjj
    #
    # p.clear_values(Page)
    # p.base_url = 'hhhhhhhhhhh'

    menu_name = '关闭其他所有页' if False else '关闭当前页'
    loc1 = Page.format_xpath(MenuLocators.CLOSE_PAGES, menu_name)
    print(loc1)

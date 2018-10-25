# -*- coding:utf-8 -*-

'''
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
10.方法名：back_home_ifrme
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

'''
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  # 键盘按键包
from selenium.webdriver.common.alert import Alert
from com.nrtest.common.logger import Logger
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from com.nrtest.common.setting import Setting
from time import sleep
from selenium.webdriver.support.ui import Select
from com.nrtest.common.setting import Setting
from com.nrtest.sea.locators.other.login_page_locators import LoginPageLocators
import datetime
import time

# create a logger instance
from com.nrtest.sea.locators.other.menu_locators import MenuLocators

logger = Logger(logger="Page").getlog()


class must_get_url(object):
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


class Page(object):

    def __init__(self, driver, base_url=Setting.TEST_URL, pagetitle=Setting.PAGE_TILE):
        self.driver = driver
        self.base_url = base_url
        self.page_title = pagetitle

    def fail_on_screenshot(function):
        """
        函数/方法报错截图处理
        :param function:
        :return:
        """

        def get_snapshot_directory():
            """
            获取截图存放路径
            :return:
            """
            if not os.path.exists(Setting.SNAPSHOT_DIRECTORY):
                os.mkdir(Setting.SNAPSHOT_DIRECTORY)
            return Setting.SNAPSHOT_DIRECTORY

        def get_current_time_str():
            """
            格式化时间
            :return:
            """
            return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f")

        def wrapper(*args, **kwargs):
            instance, selector = args[0], args[1]
            try:
                return function(*args, **kwargs)
            except (TimeoutException, NoSuchElementException, InvalidElementStateException) as ex:
                logger.error("Could not find the locator: [{}].".format(selector))
                filename = "{}.png".format(get_current_time_str())
                screenshot_path = os.path.join(get_snapshot_directory(), filename)
                logger.debug(instance.selenium.page_source)
                instance.selenium.save_screenshot(screenshot_path)
                raise ex

        return wrapper

    def _find_element(self, *Locator):
        '''
        方法名：_element
        功能：定位元素的具体某个元素WEBelement

        *注释：_代表类的私有属性或方法
        :param Locators: 元素的位置
        :return: 返回定位的元素
        '''

        try:
            # 利用显示等待判断元素是否已经出现
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(Locator))
            # 定位元素
            el = self.driver.find_element(*Locator)

        except NameError as e:
            logger.error(u'未找到元素:{0}'.format(Locator))

        return el

    def input(self, values, *locators):
        '''
        方法名：input
        功能：文本框输入内容

        :param values: 文本框要输入的内容
        :param locators: 元素的位置
        :return: None
        '''
        try:
            el = self._find_element(*locators)
            # 输入前清空文本框
            el.clear()
            el.send_keys(values)
            logger.info('文本框输入：{0}'.format(values))
        except AttributeError as e:
            logger.error('输入错误{0}'.format(values))
        return None

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
        assert self.on_page(page_title), u"打开开页面失败 %s" % url

    def open_title_url(self, is_trust=False):
        """
        定义open方法，调用_open()进行打开链接
        :param is_trust:  是否一直等待到页面真正打开
        """
        if is_trust:
            WebDriverWait(self.driver, Setting.WAIT_TIME).until(must_get_url(self.base_url))
        else:
            self._open(self.base_url, self.page_title)

    def click(self, *locators):
        '''
        方法名：click
        功能：点击元素

        :param locators:元素的位置
        :return:None
        '''
        try:
            el = self._find_element(*locators)
            el.click()
            logger.info('点击元素：{0}'.format(locators))
        except AttributeError as e:
            logger.error('点击元素失败')
        return None

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
        logger.info("关闭浏览器")
        self.driver.quit()

    def hover(self, *locators):
        """
        方法名：hover
        说明：鼠标移动到某个元素上
        :param Locators: 元素的xpath
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locators))
            above = self._find_element(*locators)
            ActionChains(self.driver).move_to_element(above).perform()
        except NameError as e:
            logger.error("悬停失败")

    def switch_frame(self, *locators):
        """
        方法名：switch_frame
        进入iframe层
        :param locators:元祖形式存在的iframe的id
        :return:
        """
        logger.info('进入{0}的iframe层'.format(locators))
        return self.driver.switch_to_frame(locators[1])

    def back_parent_iframe(self):
        '''
        方法名：back_parent_iframe
        回到iframe上一层
        :return:
        '''
        logger.info('回到iframe上一层')
        self.driver.switch_to.parent_frame()
        return None

    def back_home_ifrme(self):
        '''
        方法名：back_home_ifrme
        回到ifrmae开始的地方
        :return:
        '''
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

    def on_page(self, page_title):
        """
        方法名：on_page
        通过title断言进入的页面是否正确。
        使用title获取当前窗口title，检查输入的title是否在当前title中。
        :param page_title:
        :return: 返回比较结果（True 或 False）
        """
        return page_title in self.driver.title

    def check_element_exists(self, *locator):
        """
        方法名：check_element_exists
        判断元素是否存在
        :param locator:元祖形式的xpath
        :return:布尔返回值
        """
        try:
            self._find_element(*locator)
            return True
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
        '''
        方法名：open_url
        打开被测服务地址
        :return:
        '''
        try:
            self.driver.maximize_window()
            self.driver.get(self.base_url)
            logger.info('打开被测试服务地址：{0}'.format(self.base_url))
            return self.driver
        except NameError as e:
            logger.error("{0}打开网址失败".format(self.base_url))

    def assert_context(self, *locators):
        '''
        断言
        :param asssert_values: 校验的值
        :return: 布尔返回值
        '''
        try:
            f = self._find_element(*locators).is_displayed()
            return f
        except:
            return False

    def sleep_time(self, time):

        '''
        休眠
        :param time: 休眠时间
        :return: 无
        '''
        logger.info('休眠：{0}s'.format(time))
        sleep(time)

    def select(self, idx_or_text, *locators):

        '''
        选择下拉框
        :param locators: 元祖存放元素的xpath
        :param idx_or_text: 内容或下标
        :return:
        '''
        try:
            if type(idx_or_text) == int:
                Select(self._find_element(*locators)).select_by_index(idx_or_text)
                logger.info('按下标选择下拉框,选中第:{0}'.format(idx_or_text))
            else:
                Select(self._find_element(*locators)).select_by_visible_text(idx_or_text)
                logger.info('按内容选择元素，选中内容为:{0}'.format(idx_or_text))

        except NameError as e:
            logger.error("选择下拉框失败")

        # 保存图片

    def get_windows_img(self, name):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = Setting.SHOT_PATH
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + name + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    def find_elements(self, *Locator):
        '''
        #校验一组元素
        :param Locator:
        :return: 查找元素个数
        '''
        try:
            el = self.driver.find_elements(*Locator)
            return el

        except NameError as e:
            logger.info("组员查找错误")

    def find_elements_num(self, *Locator):
        '''
        #校验一组元素
        :param Locator:
        :return: 查找元素个数
        '''
        try:
            el = self.driver.find_elements(*Locator)
            return el

        except NameError as e:
            logger.info("组员查找错误")

    def wait(self):
        '''
        等待页面加载完成
        :return:
        '''
        self.driver.implicitly_wait(Setting.WAIT_TIME)

    def refreshPage(self):
        '''
        刷新页面
        :return:
        '''

        self.driver.refresh()
        sleep(2)
        con = self.driver.find_element_by_tag_name('body').text

        if '重要信息推出' in con:
            bool = False
            if '登录异常' in con:
                print("-----")
                self.driver.find_element(*LoginPageLocators.BTN_CONFIRM).click()
            if '账号异常信息' in con:
                print("-----")
                self.driver.find_element(*LoginPageLocators.BTN_ARROW).click()

    def clear(self, *Locators):
        '''

        :param Locators:
        :return:
        '''
        self._find_element(*Locators).clear()

    def assert_body(self, value):
        t = self._find_element(*(By.TAG_NAME, 'body')).text
        if value in t:
            return True
        else:
            return False

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
                obj("")
            elif (temp.startswith('inputCStr') and callable(obj)):
                obj("c")
            elif (temp.startswith('inputRSel')) and callable(obj):
                obj(1)

    @classmethod
    def get_select_locator(self, locator, num):
        '''
        
        :param idx: 
        :return: 返回locators
        '''
        return (locator[0], locator[1] % num)

    def bock_wait(self, Locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(Locator))

    def implic_wait(self):
        self.driver.implicitly_wait(10)

    def Find_element_by_tag_name(self, value):
        f = self.driver.find_element_by_tag_name(value)
        print(len(f))
        return f

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
        num = self.find_elements_num(*MenuLocators.TREE_MINUS)
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

    def clickTabPage(self, name):
        '''
        输入tab页名称，选中tab页
        :param name: tab页的中文名称
        :return:
        '''
        try:
            locators = (By.XPATH, "(//*[@class=\"x-tab-strip-text \"])[contains(text(),'{}')]".format(name))
            self.click(*locators)
        except NoSuchElementException  as e:
            print('点击{}tab页失败'.format(name))

    @classmethod
    def TableLineValue(self, i, l):
        try:
            str = "(//*[@class=\"x-grid3-row-table\"])[{0}]//td[{1}]".format(i, l)
            changeStr = self._find_element(*(By.XPATH, str)).text
            return changeStr
        except NameError as e:
            print('获取显示区文字失败')

    @classmethod
    def assertTableOne(self):
        try:
            bo = self.assert_context(*(By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]'))
            if bo is True:
                return True
            else:
                return False

        except NameError as e:
            print('获取显示区第一个列数据失败')
    #点击确认
    def btn_confirm(self):

           try:
            va = self.assert_context(*MenuLocators.BTN_CONFIRM)
            if va is True:
             self.click(*MenuLocators.BTN_CONFIRM)
           except:
               print('点击确认按钮失败')

    #点击右键关闭其他按钮
    def rightCloseOtherPage(self):
     try:
        right_click = self._find_element(*(By.XPATH,'//*[@id="maintab__工作台"]'))
        ActionChains(self.driver).context_click(right_click).perform()
        self.click(*(By.XPATH,'//*[@class=\"x-menu x-menu-floating x-layer \"]//*[text()=\'关闭其他所有页\']'))
     except:
         print('error:关闭其他页失败')


if __name__ == '__main__':
    dr = webdriver.Chrome()

    p = Page(dr)
    # jjjjjj

    p.clear_values(Page)
    p.base_url = 'hhhhhhhhhhh'

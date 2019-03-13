# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: menu_page.py
@time: 2018/8/28 0028 13:45
@desc:
"""

from com.nrtest.common import global_drv
from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.login import Login
from com.nrtest.pbs.tree.tree_page import *
from com.nrtest.sea.locators.other.menu_locators import *


class MenuPage(Page):
    def __init__(self, driver):

        super().__init__(driver)

        # SEA--SEA2017标设
        # SEA2.0--新一代采集系统
        # SZ_JLZDH--计量自动化(SZ)
        # GX_JLZDH--计量自动化(GX)
        # D5000--电能量采集系统（D5000/PBS5000)
        if self.project_no == 'SEA':
            self.locator_class = MenuLocators
            self.leftTree = TreePage(self)
        elif self.project_no == 'SEA2.0':
            self.locator_class = MenuSEA20Locators
        elif self.project_no in (['PBS5000', 'D5000']):
            self.locator_class = MenuPBSLocators
            self.leftTree = TreePBSPage(self)
        elif self.project_no.endswith('JLZDH'):
            self.locator_class = MenuJLZDHLocators
        print('执行【{}】项目的菜单元素'.format(self.project_no))

    @staticmethod
    def openMenu(menuNo):
        """
        打开指定菜单页面
        :param menuNo: 菜单编号
        :return:
        """
        menuPage = MenuPage(global_drv.get_driver())
        menuPage.click_menu(menuNo)
        sleep(1)
        return menuPage

    @BeautifulReport.add_popup_img(3)
    def click_menu(self, menu_no, isPath=False):
        """
        定位级菜单element,并调用Base_Page类的click方法选择级菜单
        :param menu_no: 菜单编号
        :param isPath: True-menu_no是已确定的菜单路径，False-menu_no是菜单编码
        :return:各级菜单名，如：基本应用;档案管理;档案同步  一级菜单下第一个菜单下的第二个子菜单
        """
        menu_path = menu_no if isPath else DataAccess.getMenu(menu_no)
        ls_menu = menu_path.split(',')
        menu_path = ls_menu[0]
        # 菜单动作：01-点击；02-悬浮（HOVER)；03-新窗口；11-滚屏且点击；12-滚屏且悬浮；13-滚屏且新窗口
        action = ls_menu[1]
        # PBS5000，用于区分每个菜单用到的左边树类型
        self.tree_type = ls_menu[2] if bool(ls_menu[2]) else '20'
        self.is_refresh = ls_menu[3]  # 关闭菜单时是否需要刷新页面

        items = menu_path.split(';')

        # 菜单编号、菜单名
        self.menu_no = menu_no
        self.menu_name = items[-1]
        # 菜单路径
        self.menu_path = ls_menu[-1] + '-->' + '-->'.join(items[1:])
        print('开始执行：{} 相关用例....\r'.format(self.menu_path))

        # self.menu_para = DataAccess.get_menu_setup(self.project_no)
        if self.project_no == 'SEA':
            self._click_sea2017(items, action)
        else:
            self._click_common_menu(items, action)

    def driver_action(self, menu_level, menu_levels):
        #     {'ACTION': '02', 'FIRST_LEVEL': 'N', 'LEVELS': ['2', '3']}
        if self.menu_para['FIRST_LEVEL'] == 'Y':
            is_pass = menu_level < menu_levels and menu_level >= self.menu_para['LEVELS']
        else:
            is_pass = menu_level < menu_levels and str(menu_level) in self.menu_para['LEVELS']
        return self.menu_para['ACTION'] if is_pass else '01'

    def _click_sea2017(self, items, action='01'):
        """
        国网2017标设菜单处理
        :param items:
        :param action:
        :return:
        """
        # print('国网2017标设菜单处理', items, action)
        if items[-1] == '升级版本管理':
            abcd = 'a'
        item_cnt = len(items)
        for i, item in enumerate(items):
            # MenuLocators
            locators = getattr(self.locator_class, 'MENU_LEVEL' + str(i + 1))
            loc = (locators[0], locators[1] % item)
            if (item_cnt == 4 and i == 2) or (item_cnt == 5 and i in (2, 3)):
                # loc = (By.XPATH, '//ul[@class="x-menu-list"]/li/a/span[text() = "{}"]/ancestor::li[@class="x-menu-list-item "]'.format(item))
                self.hover(loc)
            else:
                # 菜单太多需要滚屏处理,如：统计查询→综合查询→巡检仪综合查询
                # action:11-滚屏且点击
                if i + 1 == item_cnt and action == '11':
                    self._scroll_menu(loc, action)
                else:
                    self.click(loc)

    def _click_common_menu(self, items, actions):
        """
        通用菜单打开操作
        :param items: 菜单路径
        :param actions:菜单操作动作
        """
        ls_action = actions.split('/')
        if ls_action[-1] == '':
            ls_action.pop()
        for idx, item in enumerate(items):
            next_action = self._speical_deal(items, idx)
            # next_action: True - 继续处理当前菜单；False - 跳过处理当前菜单
            if next_action:
                locators = getattr(self.locator_class, 'MENU_LEVEL' + str(idx + 1))
                loc = self.format_xpath(locators, item)
                try:
                    action = ls_action[idx]
                    if action == '':
                        action = '01'
                except:
                    action = '01'
                self._menu_action(loc, action)

    def _speical_deal(self, items, idx):
        """
        通用菜单处理中，针对不同项目及层级菜单的特殊处理
        :param items: 菜单列表
        :param idx: 第 idx + 1 层级菜单
        :return: True-继续处理当前菜单；False-跳过处理当前菜单
        """
        next_action = True
        ####################PBS5000的特殊判断处理############################
        if idx == 0 and self.project_no == 'PBS5000':
            # 判断是否为首页及当前一级菜单
            next_action = self.goto_home_page(items[idx])

        return next_action

    def _menu_action(self, object, action):
        """
        菜单操作动作
        :param object: 元素对象或xpath
        :param action: 菜单动作
        """
        flag = action[-1]
        if flag in ('1', '3'):  # 1-点击/3-新窗口
            if isinstance(object, tuple):
                self.click(object)
            else:
                object.click()
            if flag == '3':  # 新窗口
                sleep(2)  # 等待窗口打开
                self.goto_window()
        elif flag == '2':  # 悬浮
            self.hover(object)  # 参数必须是locator

    def _scroll_menu(self, locator, action):
        """
        菜单太多时需要滚屏
        :param locator: 菜单xpath
        """
        try:
            flag = action[-1]
            el_menu = self._find_element(locator, ec_mode=2)
            # 当菜单动作为hover时，_menu_action.object的值为xpath对象
            object = locator if flag == 2 else el_menu
            if el_menu.is_displayed():
                # el_menu.click()
                self._menu_action(object, action)
            else:
                # el = self._find_element(self.locator_class.BTN_SCROLL_DOWN)
                el = self._find_element(self.locator_class.BTN_SCROLL_DOWN)
                cnt = 0  # 避免菜单不存在
                while cnt < 15:
                    el.click()
                    sleep(0.5)
                    cnt += 1
                    if el_menu.is_displayed():
                        # el_menu.click()
                        self._menu_action(object, action)
                        break
        except Exception as ex:
            DataAccess.el_operate_log(self.menu_name, None, locator, None, '找不到元素', ex)

    def goto_home_page(self, menu_name=''):
        """
        PBS5000专用，当前菜单为
        :param menu_name: 目标一级菜单名
        :return: True-已退回到一级菜单，False-仍驻留在menu_name菜单
        """
        curr_page_title = self.get_titile()

        # 判断是否是首页
        is_home_page = curr_page_title == self.main_page_title  # Setting.PAGE_TILE
        if is_home_page:
            return is_home_page

        # 判断是否是当前页
        if curr_page_title == menu_name:
            return False
        else:  # 都不是，则退回首页
            el = self._find_element(self.locator_class.GOTO_MAINPAGE, 1.5)
            if bool(el):
                el.click()
                is_home_page = True
                sleep(2)
            else:
                raise ("疯了......")
        return is_home_page

    def recoverLeftTree(self):
        """
        从BasePage类转来 MenuLocators
        :return:
        """
        self.leftTree.colseLeftTree()
        # num = self._find_elements(self.locator_class.TREE_MINUS)
        #
        # el = self._direct_find_element(self.locator_class.TREE_END)
        # if len(num) == 0 and el == None:
        #     return 0
        # is_exists = el.is_displayed() if bool(el) else False
        # if is_exists:
        #     counter = len(num) - 1
        #     while counter >= 0:
        #         if num[counter] is self.locator_class.TREE_END:
        #             self.click(self.locator_class.TREE_END)
        #         else:
        #             num[counter].click()
        #         counter = counter - 1
        #     num_end = self._find_elements(self.locator_class.TREE_END)
        #     counter_end = len(num_end) - 1
        #     while counter_end >= 0:
        #         num_end[counter_end].click()
        #         counter_end -= 1

    def closePage(self, page_name=None):
        """

        :param page_name:
        :return:
        """
        menu_name = page_name if bool(page_name) else self.menu_name
        menu_loc = self.format_xpath(self.locator_class.CURR_MENU, menu_name)
        try:
            sleep(1.5)
            # print('closing menu window {}'.format(menu_loc[1]))
            self.driver.find_element(*menu_loc).click()
            # print('closed menu window {}'.format(menu_loc[1]))
        except Exception as ex:
            print('定位菜单：{} 报错，错误信息：{}\r'.format(menu_name, ex))

    def closePages(self, page_name='工作台', isCurPage=True):
        """
        通过工作台或定位菜单页面，关闭当前页面或除当前页面外其他页面
        :param page_name: 需关闭的菜单
        :param isCurPage:True-关闭当前页；False-关闭其他所有页
        """
        if isCurPage:
            page_name = None if page_name == '工作台' else page_name
            self.closePage(page_name)
        else:
            if page_name == '工作台':
                menus = ('', page_name)
            else:
                menus = (self.locator_class.WORKBENCH, page_name)
            loc = self.format_xpath(self.locator_class.CLOSE_OTHERS_MENU, menus)

            # # 定位到要右击的元素
            # loc = self.format_xpath(self.locator_class.CURRENT_MENU, page_name)
            # right_click = self.driver.find_element(*loc)
            # # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
            # # 鼠标右键操作
            # ActionChains(self.driver).context_click(right_click).perform()
            #
            # # 定位右键菜单,并点击
            # forMenu = '关闭其他所有页' if isCurPage or page_name == '工作台' else '关闭当前页'
            # loc = self.format_xpath(self.locator_class.CLOSE_PAGES, forMenu)
            # try:
            #     WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
            # except:
            #     loc = self.format_xpath(self.locator_class.CLOSE_PAGES_SPE, forMenu)
            #     print(loc)
            self.driver.find_element(*loc).click()

        if self.is_refresh == 'Y':
            self.refreshPage()

    def displayTreeMenu(self):
        """
        打开左边树菜单栏 从BasePage转来
        :return:
        """
        el = self._direct_find_element(self.locator_class.BTN_LEFT_MENU)
        if bool(el) and el.is_displayed():
            el.click()

        # try:
        #     # MenuLocators
        #     WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.locator_class.BTN_LEFT_MENU))
        #     el = self.driver.find_element(*self.locator_class.BTN_LEFT_MENU)
        #     if el.is_displayed():  # 左边树没显示时打开
        #         el.click()
        # except:
        #     # print('左边树菜单栏已经打开')
        #     pass

    # 左边树
    def btn_plus(self, index):
        locator = self.get_select_locator(self.locator_class.BTN_LEFT_PLUS, index)
        self.click(locator)

    def btn_company_plus(self, index):
        locator = self.get_select_locator(self.locator_class.BTN_COMPANY_PLUS, index)
        # print(locator)
        self.click(locator)

    def btn_select_province(self):
        """
        选择省份
        """
        self.click(self.locator_class.BTN_LEFT_MENU_ELETRIC)

    def btn_select_company(self, number):
        """
        选择公司
        :param number:
        """
        nb = number + 1
        lr = self.get_select_locator(self.locator_class.BTN_COMPANY, nb)
        self.click(lr)

    def btn_left_arrow(self):
        """
        点击双向箭头
        """
        self.click(self.locator_class.BTN_LEFT_MENU)

    def btn_select_county(self, index):
        """
        选择县
        :param index:
        """
        lr = self.get_select_locator(self.locator_class.BTN_COUNTY, index)
        self.click(lr)

    def btn_select_user(self, index):
        """
        选供电所
        :param index:
        """
        lr = self.get_select_locator(self.locator_class.BTN_COUNTY_AND_USER, index)
        self.click(lr)

    def btn_suitable_arrow(self):
        txt = self._find_element((By.TAG_NAME, 'body')).text
        hp = '电网结构' in txt
        if hp is False:
            self.btn_left_arrow()
        else:
            print('省份选择错误')

    def click_left_tree_tab(self, tab_name):
        xpath = self.format_xpath(self.locator_class.TAB_PAGE, tab_name)
        self.click(xpath)


    # 选择左边树
    # def btn_left_tree(self, tree_no):
    #     self.sleep_time(2)
    #     tree = DataAccess.getLeftTree(tree_no)
    #     self.click_left_tree_tab('供电区域')
    #     # self.click(BaseLocators.POWER_SUPPLY_AREA)
    #
    #     # self.btn_suitable_arrow()
    #     items = tree.split(';')
    #     l = len(items)
    #
    #     if l == 2: # 选市公司
    #         self.btn_plus(1)
    #         self.btn_select_company(int(items[1]))
    #         # print(int(items[1]))
    #     elif l in (3, 4): # 选县公司、供电所
    #         self.btn_plus(1)  # 点击省公司加号
    #         if int(items[1]) == 5:  # 承德供电公司的加号xpath与前4个有所区别需要做特殊处理
    #             self.btn_plus(1)
    #         else:
    #             self.waitLeftTree()
    #             self.btn_company_plus(items[1])
    #         if l == 3:
    #             self.waitLeftTree()
    #             # self.btn_select_county(int(items[2]) + 1)  # 点击公司加号 ljf 2019-03-06
    #             self.btn_select_county(int(items[2]))  # 点击公司加号
    #         else:
    #             self.waitLeftTree()
    #             # self.btn_company_plus(int(items[2]) + int(items[1]))  # 点击公司加号 ljf 2019-03-06
    #             self.btn_company_plus(int(items[2]))
    #             self.waitLeftTree()
    #             # self.btn_select_user(int(items[3]) + 1)  # ljf 2019-03-06
    #             self.btn_select_user(int(items[3]))
    #     elif l == 1:  # 选省公司
    #         self.btn_select_province()
    #
    #     return self.driver
    def btn_left_tree(self, node_no):
        # self.sleep_time(2)
        self.leftTree.openLeftTree(node_no)
        return self.driver

    def btn_user_nodes(self, node_flag, node_value, number=1):

        """
        选择左边树用户Tab页面，并根据节点类型，输入并查询相应结果
        :param node_flag: 节点分类
        :param node_value: 节点值
        :param number:查询结果显示的区域，number：代表第几个行，默认是1

        """
        # 根据node_flag选择相应的节点查询条件xpath，并输入查询条件
        # {02:代表用户编号，03：代表终端逻辑地址，04：电能表资产号}
        # {05:普通群组，06：重点用户群组，07：控制群组}

        if node_flag in (
                # 选用户Tab页的用户
                '02', '03', '04',
                #  选用户Tab页的台区
                '12', '13', '14',
                # 选终端Tab页的采集点编号/终端地址
                '22', '23'
        ):
            if node_flag.startswith('2'):  # 点终端Tab页
                self.click_left_tree_tab('终端')
                loc_org = self.format_xpath(self.locator_class.SEL_TMNL_CHECKBOX, '供电单位')
                loc_btn_qry = self.locator_class.USER_TMNL_BTN_QRY
                table_rslt_id = 'leftcollGrid'
            else:  # 点用户Tab页
                self.click_left_tree_tab('用户')
                loc_org = self.format_xpath(self.locator_class.SEL_USER_CHECKBOX, '供电单位')
                loc_btn_qry = self.locator_class.USER_TAB_BTN_QRY
                table_rslt_id = 'leftUserGrid'

                # self.click(self.locator_class.NODE_USER)
            # 选用户查询类型
            if node_flag in ('02', '03', '04'):
                self.specialDropdown('用户查询类型;;', self.locator_class.SEL_USER_TYPE, locator_clean=self.locator_class.SEL_USER_TYPE)
            elif node_flag in ('12', '13', '14'):
                self.specialDropdown('用户查询类型;;台区', self.locator_class.SEL_USER_TYPE)
            if node_value.find(';') > 0:
                ls = node_value.split(';')
                org_no = ls[0]
                usr_info = ls[1]
                self.scrollTo(loc_org)
                self.specialDropdown('供电单位;;{}'.format(org_no), loc_org)
            else:
                usr_info = node_value

            self.scrollTo(self.locator_class.NODE[node_flag])
            self.input(usr_info, *self.locator_class.NODE[node_flag])

            # 点击查询按钮
            el = self._find_displayed_element(loc_btn_qry)
            el.click()
            # 左边树查询60秒超时等待
            self.query_timeout(self.locator_class.LEFT_TREE_LOADING, 60)  # @TODO 60秒不建议写死，建议后续改为可配置

            # 等待查询结果，最好通过其他途径判断查询已返回 @TODO 需增加是否有查询结果判断处理
            # self.commonWait(self.locator_class.NODE_USER_TAB_RSLT_DEFAULT)
            self.clear(self.locator_class.NODE[node_flag])

            # 定位查询结果，默认选择第一行记录
            xpath = self.format_xpath(self.locator_class.NODE_USER_TAB_RSLT, (table_rslt_id, usr_info))
            # print(xpath)

            self.click(xpath)
            # print('------------')

        elif (node_flag in ('05', '06', '07')):
            # 点击群组标签页
            self.click_left_tree_tab('群组')
            # self.click(self.locator_class.NODE_GROUP)

            # 选择群组类型
            if (node_flag != '05'):
                self.click(self.locator_class.GROUP_NODE[node_flag])

            # 打开群组信息
            self.click(self.locator_class.GROUP_PLUS[node_flag])

            # 根据名称选择群组
            xpath = self.format_xpath(self.locator_class.NODE_GROUP_RSLT[node_flag], node_value)
            # print(xpath)

            self.click(xpath)
            # print('------------')

    def clickAllMenu(self):
        menus = DataAccess.getAllMenu()
        # menus = [('999246000', '台区线损监测', 'advAppIcon;线损分析;线损统计分析;台区线损监测')]
        l = len(menus)
        for i in range(len(menus)):
            try:
                menu = menus[i]
                print('即将定位该菜单：', menu)
                self.click_menu(menu[2], True)
                sleep(1)
                self.closePages(menu[1])
            except Exception as e:
                print('该菜单定位报错：', menu, e)


if __name__ == '__main__':
    login = Login()
    menuPage = MenuPage(login.login())
    #
    # # menuPage.click_menu('99913210', True) #'99913210')
    # # menuPage.clickTabPage('采集成功率统计')
    # menuPage.clickAllMenu()

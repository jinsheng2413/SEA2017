# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: tree_page.py
@time: 2019-01-09 9:31
@desc:
"""
import re
from time import sleep

from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.dictionary import Dict
from com.nrtest.pbs.tree.tree_locators import TreePBSLocators, TreeLocators


class BaseTreePage(Page):
    def __init__(self, driver, menu_page=None):
        """

        :param driver:
        :param menu_page:
        :param tree_type:
                20-含电压等级厂站树 11-并且带复选框
                30-厂站档案设备树   21-并且带复选框
                40-普通树         41-并且带复选框；采集运维-->手动对时
        """
        super().__init__(self, driver, menu_page)
        if bool(menu_page):
            self.tree_type = menu_page.tree_type
        else:
            self.tree_type = '20'

    def openLeftTree(self, node_no, op_mode=True):
        """
        打开左边树
        :param node_no:
        """
        try:
            node = Dict(eval(node_no))
            node_vale = node['NODE_VALE']
        except:
            # 不是数组时的默认处理
            node = {'NODE_FLAG': '01', 'NODE_VALUE': node_no}
            node_vale = node_no

        node['NODE_VALE'] = DataAccess.getTreeNode(node_vale).split(';')

        self._click_node_tab(node['NODE_FLAG'])
        self.node_list = []  # 用于左边树整体收起压栈
        # self.tree_node = node # 整体压栈时，gai
        self._operate_left_tree(node)

    def _click_node_tab(self, node_tab_idx):
        """
        左边树操作前的预处理，如选择左边树类型
        :param node_tab_idx:
        """
        pass

    def colseLeftTree(self):
        # node = deepcopy(self.tree_node)
        # node['NODE_VALE'].reverse()
        # self._operate_left_tree(node, False)
        if self.tree_type[-1] == 0:  # 非复选框节点，最后一个叶子节点不处理
            self.node_list.pop()

        self.node_list.reverse()
        for node in self.node_list:
            node.click()

    def _operate_left_tree(self, node_info):
        """
        根据左边树节点信息，打开或收起节点信息
        :param node_info: 左边树节点信息
        :return:
        """
        node_flag = node_info['NODE_FLAG']
        if node_flag == '01':  # 选择全模型
            items = node_info['NODE_VALE']
            levels = len(items) - 1  # 总层级数-1
            for idx, item in enumerate(items):
                # 厂站间有重复节点名，如电压等级、厂站设备等
                locator = self._find_in_parent(item, idx, items)
                if self.tree_type[-1] == '1':  # 带复选框的左边树
                    els = self._find_elements(locator)
                    if bool(els):
                        self._node_click(els[0], idx, levels)
                        if idx == levels:
                            self._node_click(els[1], idx, levels, True)
                else:
                    # if idx == levels:  # 叶子节点只点击文本元素，不点击文本元素边上的图标元素
                    #     locator = (locator[0], locator[1].replace('/../span', ''))  # 该替换操作只对PBS5000有效
                    # el = self._find_element(locator)
                    el = self._find_displayed_element(locator)
                    if bool(el):
                        self._node_click(el, idx, levels)
        else:  # 选择其他节点
            self._other_left_tree(node_info)

    def _other_left_tree(self, node_info):
        pass

    def _find_in_parent(self, item, idx, items):
        return None

    def _node_click(self, element, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        pass


class TreePBSPage(BaseTreePage):
    def _click_node_tab(self, node_tab_idx):
        if self.tree_type[0] != '4':
            node_tab = {'01': '全模型', '02': '搜索', '03': '收藏夹'}
            loc = self.format_xpath(TreePBSLocators.NODE_TAB, node_tab[node_tab_idx])
            self.click(loc)

    def _find_in_parent(self, item, idx, items):
        """
        在父节点范围内查找
        :param item:
        :return:
        """
        # 20-含电压等级厂站树； 11-并且带复选框
        # 30-厂站档案设备树；   31-并且带复选框
        # 40-普通树；         41-并且带复选框；采集运维-->手动对时
        is_step_into = False
        if self.tree_type[0] == '2':  # 20-含电压等级的厂站树
            is_step_into = bool(re.search(r'^\d{1,4}.[kK][vV]$', item))
        elif self.tree_type[0] == '3':  # 30-厂站档案设备
            is_step_into = item in ['线端', '刀闸', '发电机组', '电容器', '负荷', '开关']

        levels = len(items) - 1  # 总层级数-1
        if is_step_into:
            locator = self.format_xpath(TreePBSLocators.NODE_LEVEL_IN_PARENT, (idx - 1, items[idx - 1], idx, item))
        else:
            locator = self.format_xpath(TreePBSLocators.NODE_LEVEL, (idx, item))
            # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
            if idx == levels and self.tree_type[1] == '0':
                # locator = (locator[0], locator[1].replace('/../span', ''))
                locator = self.format_xpath(TreePBSLocators.LEEF_NODE, (idx, item))

        return locator

    def _node_click(self, element, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        self.node_list.append(element)
        attrs = element.get_attribute('class').strip()
        if is_chk_node:
            # 目前仅对pbs5000有效:判断当前节点是选中，不选中
            # 带复选框的左边树：不选中：class="button chk checkbox_false_full"  选中：class="button chk checkbox_false_part"
            is_click = attrs.endswith('full') or curr_idx == node_levels
        else:
            # 目前仅对pbs5000有效:判断当前节点是打开还是关闭
            is_click = attrs.endswith('close') or curr_idx == node_levels

        # 状态不一致时点击
        if is_click:
            element.click()
            sleep(0.3)


class TreePage(BaseTreePage):
    def _click_node_tab(self, node_tab_idx):
        if self.tree_type[0] != '4':
            node_tab = {'01': '供电区域', '02': '用户', '03': '终端', '04': '行业', '05': '电网结构', '06': '群组'}
            loc = self.format_xpath(TreeLocators.NODE_TAB, node_tab[node_tab_idx])
            self.click(loc)

    def _find_in_parent(self, item, idx, items):
        """
        在父节点范围内查找
        :param item:
        :param idx:
        :param items:
        :return:
        """
        # 20-供电区域； 11-并且带复选框
        # 30-行业；    31-并且带复选框
        # 40-普通树；   41-并且带复选框；
        # 50-群组
        is_step_into = False
        if self.tree_type[0] == '2':
            is_step_into = item == '直属用户'

        levels = len(items) - 1  # 总层级数-1
        if is_step_into:
            locator = self.format_xpath(TreeLocators.NODE_LEVEL_IN_PARENT, (items[idx - 1], item))
            # *********带复选框的叶子节点，除勾选外，是否还需再点击一下
        else:
            locator = self.format_xpath(TreeLocators.NODE_LEVEL, (item))
            # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
            if idx == levels and self.tree_type[1] == '0':
                locator = self.format_xpath(TreeLocators.LEEF_NODE, item)

        # 对群组类型元素定位做特殊处理
        if self.tree_type == '50':
            locator = (locator[0], locator[1].replace(TreeLocators.TREE_DIV, self.group_node[1]))

        return locator

    def _node_click(self, element, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        self.node_list.append(element)
        attrs = element.get_attribute('class').strip()

        if is_chk_node:
            # is_click = attrs.endswith(('full' if is_open else 'part')) or curr_idx == node_levels
            # @TODO 含复选框的树在此处理
            is_click = True
        else:
            # 关闭：class ="x-tree-ec-icon x-tree-elbow-end-plus"

            # 打开：class ="x-tree-ec-icon x-tree-elbow-end-minus"
            is_click = attrs.endswith('plus') or curr_idx == node_levels

        # 状态不一致时点击
        if is_click:
            element.click()
            sleep(0.3)

    def _other_left_tree(self, node_info):
        node_flag = node_info['NODE_FLAG']
        if node_flag in ('02', '03', '04'):
            self.user_tab_query(node_flag, node_info['NODE_VALE'])
        elif node_flag in ('05', '06', '07'):
            self.group_tab_query(node_flag, node_info['NODE_VALE'])

    def user_tab_query(self, node_flag, node_value, number=1):

        """
        选择左边树用户Tab页面，并根据节点类型，输入并查询相应结果
        :param node_flag: 节点分类
        :param node_value: 节点值
        :param number:查询结果显示的区域，number：代表第几个行，默认是1

        """
        # 根据node_flag选择相应的节点查询条件xpath，并输入查询条件
        # {02:代表用户编号，03：代表终端逻辑地址，04：电能表资产号}
        # {05:普通群组，06：重点用户群组，07：控制群组}
        # 点击用户标签页
        self._click_node_tab('02')

        self.input(node_value, *self.TreeLocators.USER_QRY_INPUT[node_flag])

        # 点击查询按钮
        self.click(self.TreeLocators.USER_BTN_QUERY)

        # 等待查询结果，最好通过其他途径判断查询已返回
        self.commonWait(self.TreeLocators.NODE_USER_TAB_RSLT_DEFAULT)
        self.clear(self.TreeLocators.USER_QRY_INPUT[node_flag])

        # 定位查询结果，默认选择第一行记录
        xpath = self.format_xpath(self.TreeLocators.NODE_USER_TAB_RSLT, node_value)
        print(xpath)

        self.click(xpath)
        print('------------')

    def group_tab_query(self, node_flag, node_value, number=1):
        # 点击群组标签页
        # @TODO 还需考虑“群组”标签页滚动后才能找到
        self._click_node_tab('06')

        # 选择群组类型
        self.group_node = self.TreeLocators.GROUP_NODE[node_flag]
        el = self._find_displayed_element(self.group_node)
        attrs = el.get_attribute('class').strip()
        if attrs.endswith('collapsed'):
            el.click()

        node_info = {'NODE_FLAG': '01'}
        node_info.setdefault('NODE_VALE', node_value.split(','))
        self.node_list = []
        self.tree_type = '50'
        self._operate_left_tree(node_info)


# class TreePBSPage(Page):
#     def __init__(self, driver, menu_page=None):
#         """
#
#         :param driver:
#         :param menu_page:
#         :param tree_type:
#                 20-含电压等级厂站树 11-并且带复选框
#                 30-厂站档案设备树   21-并且带复选框
#                 40-普通树         41-并且带复选框；采集运维-->手动对时
#         """
#         super().__init__(self, driver, menu_page)
#         if bool(menu_page):
#             self.tree_type = menu_page.tree_type
#         else:
#             self.tree_type = '20'
#
#     def openLeftTree(self, node_no, op_mode=True):
#         """
#         打开左边树
#         :param node_no:
#         """
#         try:
#             node = Dict(eval(node_no))
#             node_vale = node['NODE_VALE']
#         except:
#             # 不是数组时的默认处理
#             node = {'NODE_FLAG': '01', 'NODE_VALUE': node_no}
#             node_vale = node_no
#
#         node['NODE_VALE'] = DataAccess.getTreeNode(node_vale).split(';')
#         self._click_node_tab(node['NODE_FLAG'])
#
#         self._operate_left_tree(node)
#         self.tree_node = node
#
#     def _click_node_tab(self, node_tab_idx):
#         if self.tree_type[0] != '4':
#             node_tab = {'01': '全模型', '02': '搜索', '03': '收藏夹'}
#             loc = self.format_xpath(TreePBSLocators.NODE_TAB, node_tab[node_tab_idx])
#             self.click(loc)
#
#     def colseLeftTree(self):
#         node = deepcopy(self.tree_node)
#         node['NODE_VALE'].reverse()
#         self._operate_left_tree(node, False)
#
#     def _operate_left_tree(self, node_info, is_open=True):
#         """
#         根据左边树节点信息，打开或收起节点信息
#         :param node_info: 左边树节点信息
#         :param is_open: True-打开左边树；False-收起左边树
#         :return:
#         """
#         node_flag = node_info['NODE_FLAG']
#         if node_flag == '01':  # 选择全模型
#             items = node_info['NODE_VALE']
#             levels = len(items) - 1  # 总层级数-1
#             for idx, item in enumerate(items):
#                 new_idx = idx if is_open else levels - idx
#
#                 # 厂站间有重复节点名，如电压等级、厂站设备等
#                 is_find_in_sub = self._find_in_parent(item)
#                 if is_find_in_sub:
#                     # 需厂站范围内找节点
#                     parent_idx = idx - 1 if is_open else idx + 1
#                     locator = self.format_xpath(TreePBSLocators.NODE_LEVEL_IN_PARENT, (parent_idx, items[parent_idx], new_idx, item))
#                 else:
#                     locator = self.format_xpath(TreePBSLocators.NODE_LEVEL, (new_idx, item))
#
#                 if self.tree_type[-1] == '1':  # 带复选框的左边树
#                     els = self._find_elements(locator)
#                     if bool(els):
#                         self._node_click(els[0], is_open, idx, levels)
#                         if idx == levels:
#                             self._node_click(els[1], is_open, idx, levels, True)
#                 else:
#                     if idx == levels and is_open:  # 叶子节点只点击文本元素，不点击文本元素边上的图标元素
#                         locator = (locator[0], locator[1].replace('/../span', ''))  # 该替换操作只对PBS5000有效
#                     el = self._find_element(locator)
#                     if bool(el):
#                         self._node_click(el, is_open, idx, levels)
#         else:  # 选择其他节点
#             # self.menuPage.btn_user_nodes(node_flag, node_vale)  # 该方法细节待实现
#             pass
#
#     def _find_in_parent(self, item):
#         is_step_into = False
#         # 20-含电压等级厂站树； 11-并且带复选框
#         # 30-厂站档案设备树；   31-并且带复选框
#         # 40-普通树；         41-并且带复选框；采集运维-->手动对时
#         if self.tree_type[0] == '2':  # 20-含电压等级的厂站树
#             is_step_into = bool(re.search(r'^\d{1,4}.[kK][vV]$', item))
#         elif self.tree_type[0] == '3':  # 30-厂站档案设备
#             is_step_into = item in ['线端', '刀闸', '发电机组', '电容器', '负荷', '开关']
#
#         return is_step_into
#
#     def _node_click(self, element, is_open, curr_idx, node_levels, is_chk_node=False):
#         """
#
#         :param element:
#         :param is_open:当前操作是做打开还是收起操作
#         :param curr_idx:当前节点序号：0 开始
#         :param node_levels:当前节点层级数：n -1
#         :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
#         """
#         attrs = element.get_attribute('class').strip()
#         if is_chk_node:
#             # 目前仅对pbs5000有效:判断当前节点是选中，不选中
#             # 带复选框的左边树：不选中：class="button chk checkbox_false_full"  选中：class="button chk checkbox_false_part"
#             is_click = attrs.endswith(('full' if is_open else 'part')) or curr_idx == node_levels
#         else:
#             # 目前仅对pbs5000有效:判断当前节点是打开还是关闭
#             is_click = attrs.endswith(('close' if is_open else 'open')) or curr_idx == node_levels
#
#         # 状态不一致时点击
#         if is_click:
#             element.click()
#             sleep(0.3)

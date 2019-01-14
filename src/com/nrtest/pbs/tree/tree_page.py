# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: tree_page.py
@time: 2019-01-09 9:31
@desc:
"""
import re
from copy import deepcopy
from time import sleep

from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.dictionary import Dict
from com.nrtest.pbs.tree.tree_locators import TreeLocators


class TreePage(Page):
    def __init__(self, driver, menu_page=None, tree_type='20'):
        """

        :param driver:
        :param menu_page:
        :param tree_type:
                20-含电压等级厂站树 11-并且带复选框
                30-厂站档案设备树   21-并且带复选框
                40-普通树         41-并且带复选框；采集运维-->手动对时
        """
        super().__init__(self, driver, menu_page)
        self.tree_type = tree_type

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
        if self.tree_type[0] != '4':
            self._click_node_tab(node['NODE_FLAG'])

        self._operate_left_tree(node)
        self.tree_node = node

    def _click_node_tab(self, node_tab_idx):
        node_tab = {'01': '全模型', '02': '搜索', '03': '收藏夹'}
        loc = self.format_xpath(TreeLocators.NODE_TAB, node_tab[node_tab_idx])
        self.click(loc)

    def colseLeftTree(self):
        node = deepcopy(self.tree_node)
        node['NODE_VALE'].reverse()
        self._operate_left_tree(node, False)

    def _operate_left_tree(self, node_info, is_open=True):
        """
        根据左边树节点信息，打开或收起节点信息
        :param node_info: 左边树节点信息
        :param is_open: True-打开左边树；False-收起左边树
        :return:
        """
        node_flag = node_info['NODE_FLAG']
        if node_flag == '01':  # 选择全模型
            items = node_info['NODE_VALE']
            levels = len(items) - 1  # 总层级数-1
            for idx, item in enumerate(items):
                new_idx = idx if is_open else levels - idx

                # 厂站间有重复节点名，如电压等级、厂站设备等
                is_find_in_sub = self._find_in_sub(item)
                if is_find_in_sub:
                    # 需厂站范围内找节点
                    parent_idx = idx - 1 if is_open else idx + 1
                    locator = self.format_xpath(TreeLocators.NODE_LEVEL_IN_SUB,
                                                (parent_idx, items[parent_idx], new_idx, item))
                else:
                    locator = self.format_xpath(TreeLocators.NODE_LEVEL, (new_idx, item))

                if self.tree_type[-1] == '1':  # 带复选框的左边树
                    els = self._find_elements(locator)
                    if bool(els):
                        self._node_click(els[0], is_open, idx, levels)
                        if idx == levels:
                            self._node_click(els[1], is_open, idx, levels, True)
                else:
                    if idx == levels and is_open:  # 叶子节点只点击文本元素，不点击文本元素边上的图标元素
                        locator = (locator[0], locator[1].replace('/../span', ''))  # 该替换操作只对PBS5000有效
                    el = self._find_element(locator)
                    if bool(el):
                        self._node_click(el, is_open, idx, levels)
        else:  # 选择其他节点
            # self.menuPage.btn_user_nodes(node_flag, node_vale)  # 该方法细节待实现
            pass

    def _find_in_sub(self, item):
        is_step_into = False
        # 20-含电压等级厂站树； 11-并且带复选框
        # 30-厂站档案设备树；   31-并且带复选框
        # 40-普通树；         41-并且带复选框；采集运维-->手动对时
        if self.tree_type[0] == '2':  # 20-含电压等级的厂站树
            is_step_into = bool(re.search(r'^\d{1,4}.[kK][vV]$', item))
        elif self.tree_type[0] == '3':  # 30-厂站档案设备
            is_step_into = item in ['线端', '刀闸', '发电机组', '电容器', '负荷', '开关']

        return is_step_into

    def _node_click(self, element, is_open, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param is_open:当前操作是做打开还是收起操作
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        attrs = element.get_attribute('class').strip()
        if is_chk_node:
            # 目前仅对pbs5000有效:判断当前节点是选中，不选中
            # 带复选框的左边树：不选中：class="button chk checkbox_false_full"  选中：class="button chk checkbox_false_part"
            is_click = attrs.endswith(('full' if is_open else 'part')) or curr_idx == node_levels
        else:
            # 目前仅对pbs5000有效:判断当前节点是打开还是关闭
            is_click = attrs.endswith(('close' if is_open else 'open')) or curr_idx == node_levels

        # 状态不一致时点击
        if is_click:
            element.click()
            sleep(0.3)

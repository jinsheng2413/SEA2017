# -*- coding: utf-8 -*-"""@author: 郭春彪@license: (C) Copyright 2018, Nari.@file: collect_para_configurantion_page.py@time: 2019-07-02 15:56:44@desc:"""from com.nrtest.common.base_page import Page# 参数管理→采集参数配置class CollectParaConfigurantionPage(Page):    # 查询    def btn_qry(self):        self.btn_query()
# -*- coding: utf-8 -*-

"""
@author:郭春彪
@license: (C) Copyright 2019, Nari.
@file: eleQuantity_page.py
@time: 2019-03-15 11:05
@desc:
"""
from com.nrtest.pbs.tree.tree_page import TreePBSPage

#智能研判-->电量短信
class EleQuantity_page(TreePBSPage):

		#用户列表
		def inputSel_user_list(self,option):
		  self.selectDropDown(option)


		# 时      间
		def inputDt_query_date(self,value):
		   self.inputDate(value)



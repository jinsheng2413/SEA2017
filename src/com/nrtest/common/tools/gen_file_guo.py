from com.nrtest.common.db_driver import PyOracle
import time
author = '郭春彪'
#生成文件路径
filePath = 'D:/pythonworkspace/SEA2017/src/com/nrtest/common/tools/'
#文件名称
name = 'test_re'
#pageName
PageName = 'cdsc'
PagePath= 'D:/pythonworkspace/SEA2017/src/com/nrtest/common/tools/'

#tab页名称，默认是01
tabName = '01'
#菜单编号
menuNo= '0000304'
#菜单编号名称
data_para = 'sdfdsffdsfds'
PageName = name.split('_')[1]+'_page'



def  get_data(menuNo,tab='01'):
    sql = 'select l.tab_name,l.xpath,l.use_share_xpath,l.xpath_name from tst_menu_xpath_list l where l.menu_no = :menuNo and l.tab_name =:tab order by l.use_share_xpath'
    pyoracle = PyOracle.getInstance()
    dataSet = pyoracle.query(sql, [menuNo,tab])
    return dataSet
def head(autor=author,name="puiu",menNo=''):
    str = '# -*- coding: utf-8 -*-\n\n'+'"""\n'+ "@author:{}\n" \
           "@license: (C) Copyright 2019, Nari.\n" \
           "@file: {}.py\n" \
           "@time: {}\n" \
           "@desc:\n"\
           '"""\n'\
           "from com.nrtest.pbs.tree.tree_page import TreePBSPage\n\n"\
           + getPath(menNo)+'\n'+\
           "class {}(TreePBSPage):\n"



    str_new = str.format(autor,name,time.strftime("%Y-%m-%d %H:%M", time.localtime()),name)
    return str_new
def testHead(autor=author,name="puiu",menNo=''):
    str = '# -*- coding: utf-8 -*-\n\n'+'"""\n'+ "@author:{}\n" \
           "@license: (C) Copyright 2019, Nari.\n" \
           "@file: {}.py\n" \
           "@time: {}\n" \
           "@desc:\n"\
           '"""\n'\
           'from com.nrtest.common.BeautifulReport import BeautifulReport\n'\
           'from com.nrtest.common.data_access import DataAccess\n'\
           "from com.nrtest.sea.pages.other.menu_page import MenuPage\n"\
           'from unittest import TestCase\n'\
           'from ddt import ddt, data\n\n'\
           + getPath(menNo)+'\n'+\
           "class {}(TestCase):\n\n"



    str_new = str.format(autor,name,time.strftime("%Y-%m-%d %H:%M", time.localtime()),name.capitalize())
    return str_new
def PageHead(autor=author,name="puiu",menNo=''):
    str = '# -*- coding: utf-8 -*-\n\n'+'"""\n'+ "@author:{}\n" \
           "@license: (C) Copyright 2019, Nari.\n" \
           "@file: {}.py\n" \
           "@time: {}\n" \
           "@desc:\n"\
           '"""\n'\
           'from com.nrtest.pbs.tree.tree_page import TreePBSPage\n\n'\
           + getPath(menNo)+'\n'+\
           "class {}(TreePBSPage):\n\n"
    str_new = str.format(autor, name, time.strftime("%Y-%m-%d %H:%M", time.localtime()), name.capitalize())
    return str_new
def getPath(menuNo):
    sql = 'select o.level1,o.level2,o.level3,o.level4,o.level5 from tst_menu o where o.menu_no = :menuNo'
    pyoracle = PyOracle.getInstance()
    dataSet = pyoracle.query(sql, [menuNo])
    str = '#'
    l =0
    for i ,it  in enumerate(dataSet[0],1):
        if it !=None:
            l=i

    for i, item in enumerate(dataSet[0],1):
        p =len(dataSet[0])
        if i == l:
           str += item
        elif item !=None and i != len(dataSet[0]):
           str+=item+'-->'

    return str

def  getPage(menuNO,tab='01',path ='',name=''):
  dic = {
        '01': 'def inputStr_{}(self,value):\n\t  self.input(value)',
        '03': 'def inputSel_{}(self,option):\n\t  self.selectDropDown(option)',
        '04': 'def inputChk_{}(self,option):\n\t   self.selectCheckBox(option)',
        '06': 'def inputDt_{}(self,value):\n\t   self.inputDate(value)',
        '07': 'def inputChk_{}(self,value):\n\t   self.selectCheckBox(option)',
        '09': 'def inputBt_{}(self,value):\n\t   self.click_button(value)',
        '10': 'def inputXp_{}(self,value):\n\t   self.click_xpath(value)'
    }
  data = get_data(menuNO,tab=tab)
  lis = []
  lis.append(PageHead(menNo=menuNO))



  for a,b,c,d in data:

      str  = b.lower()
      lis.append('\t#'+d+'\n\t'+dic[c].format(str)+'\n\n\n')
  ph = path+'/'+name+'.py'
  with open(ph,'w',encoding='utf-8') as file:
      file.writelines(lis)
def getTesth(data='',tabName=''):
    str = '  @classmethod\n'\
    '  def setUpClass(cls):\n'\
    '\t# 打开菜单（需要传入对应的菜单编号）\n'\
    '\tmenuPage = MenuPage.openMenu({})\n'\
    '\tsuper(TestCase, cls).__init__(cls, menuPage.driver, menuPage)\n'\
    '\tmenuPage.intoPBSIframe()\n'\
    '\t# 菜单页面没多个Tab页时，请注释clickTabPage所在行代码\n'\
    '\tmenuPage.clickTabPage({})\n'\
    '\t# 菜单页面上如果没日期型的查询条件时，请注释下面代码\n\n'\
    '  @classmethod\n'\
    '  def tearDownClass(cls):\n'\
    '\tprint("执行结束")\n'\
    '\tcls.iframe_back(cls, num=1)\n'\
    '\t# 关闭菜单页面\n'\
    '\tcls.main_page(cls)\n\n'\
    '  def setUp(self):\n'\
    '\t"""\n'\
    '\t测试固件的setUp()的代码，主要是测试的前提准备工作\n'\
    '\t:return:\n'\
    '\t"""\n\n'\
    '  def tearDown(self):\n'\
    '\t"""\n'\
    '\t每个测试用例测试结束后的操作，在这里做相关清理工作\n'\
    '\t:return:\n'\
    '\t"""\n'\
    '\t# 回收左边树\n'\
    '\tself.closeLeftTree()\n\n'\
    '  def query(self, para):\n'\
    '\t"""\n'\
    '\t:param para: Dict类型的字典，不是dict\n'\
    '\tddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值\n'\
    '\tkey值要与tst_case_detail表中的XPATH_NAME的值保持一致\n'\
    '\t"""\n'
    str_new = str.format(data,tabName)
    return str_new
def testTail(para,menuPath):
    str ='  def assert_query_result(self, para):\n'\
    '\t"""\n'\
    '\t查询结果校验（包括跳转）\n'\
    '\t:param para:\n'\
    '\t"""\n'\
    '\t# self.assertTrue(AssertResult(self).check_query_result(para))\n'\
    '  def assert_query_criteria(self, para):\n'\
    '\t"""\n'\
    '\t查询条件校验\n'\
    '\t:param para:\n'\
    '\t"""\n'\
    '\t# self.assertTrue(self.check_query_criteria(para))\n\n'\
    '  @BeautifulReport.add_test_img()\n'\
    '  @data(*DataAccess.getCaseData({}))\n'\
    '  def test_query(self, para):\n'\
    '\t"""{}\n'\
    '\t"""\n'\
    '\tself.start_case(para, __file__)\n'\
    '\tself.query(para)\n'\
    '\tself.assert_query_result(para)\n'\
    '\tself.end_case()\n\n'\
    '  @BeautifulReport.add_test_img()\n'\
    '  @data(*DataAccess.getCaseData({}, valCheck=True))\n'\
    '  def _test_checkValue(self, para):\n'\
    '\tself.start_case(para, __file__)\n'\
    '\tself.query(para)\n'\
    '\tself.assert_query_criteria(para)\n'\
    '\tself.end_case()\n'
    str_new = str.format(para,menuPath,para,para)
    return str_new

def  getTestCase(menuNO,tab='01',path ='',name='',para=''):

  dic = {
      '01': 'self.inputStr_{}(para["{}"])',
      '03': 'self.inputSel_{}(para["{}"])',
      '04': 'self.inputChk_{}(para["{}"])',
      '06': 'self.inputDt_{}(para["{}"])',
      '07': 'self.inputChk_{}(para["{}"])',
      '09': 'self.inputBt_{}(para["{}"])',
      '10': 'self.inputXp_{}(para["{}"])'
  }
  data = get_data(menuNO,tab=tab)
  lis = []
  lis.append(testHead(menNo=menuNO,name=name))
  lis.append(getTesth(data=para))




  for a,b,c,d in data:

      str  = b.lower()
      lis.append('\t#'+d+'\n\t'+dic[c].format(str,b)+'\n\n')
  lis.append('\n\n'+testTail(para,getPath(menuNO)))
  ph = path+'/'+name+'.py'
  with open(ph,'w',encoding='utf-8') as file:
      file.writelines(lis)


if __name__=='__main__':
    getPage(menuNO=menuNo,tab=tabName,path=PagePath,name=PageName)
    getTestCase(menuNO=menuNo,tab=tabName,path=filePath,name=name,para=data_para)


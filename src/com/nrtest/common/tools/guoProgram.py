# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: guoProgram.py
@time: 2018/12/18 0018 19:37
@desc:
"""
from com.nrtest.common.setting import Setting
from com.nrtest.common.tools.fr import *

from com.nrtest.common.tools.mysaql import readData


path = 'D:/pythonworkspace/SEA2017/src/com/nrtest/sea/testcase/sys_mam/archivesVerficationMan'
class GuoProgram(object):
    def strEmpty(self,stree):
        for i,item in enumerate(stree,0):
            if item != ' ':
                return i

    def knowDataLine(self, fileName):
        lis = []
        with open(fileName, 'rt', encoding='utf-8') as data:
            gmax = 0
            for i, v in enumerate(data.readlines(), 1):
                gmax += 1
                if 'self.btn' in v:
                    lis.append(i)
            lis.append(gmax)
        return lis

    # 修改pages
    def modifyPages(self, pathName):
        fileList = []
        index_list = []
        with open(pathName, 'rt', encoding='utf-8') as rdata:
            for index, value in enumerate(rdata.readlines(), 1):

                if 'self.input(' in value and '*' in value:
                    new_value = value.replace('self', '#self')
                    va = value[int(value.index('input(')) + 6:int(value.index(','))]
                    fileList.append(new_value)
                    empty_index = value.index('self')
                    content = '\n' + value[0:int(empty_index)] + 'self.input({})'.format(va)
                    fileList.append(content)
                    fileList.append('\n')
                else:
                    fileList.append(value)
            li = []
            for i,item in enumerate(fileList,1):
                if item.find('Sel')>0  or item.find('*locator')>0:
                    li.append(i+1)
                    if len(li) == 2:
                      index_list.append(li)
                      li = []
            for i  in range(0,len(index_list)-1):
                index_list[i][1] = int(index_list[i][1])-1

            for it  in index_list:
                   for j in range(it[0],it[1]):
                           fileList[j] = fileList[j][0:self.strEmpty(fileList[j])] + '#'+fileList[j][self.strEmpty(fileList[j]):len(fileList[j])-1]+'\n'
                   fileList.insert(it[1]+1,fileList[it[0]+1][0:self.strEmpty(fileList[it[0]+1])]+'self.selectDropDown(options)'+'\n')


            with open(pathName, 'wt', encoding='utf-8') as wdata:
                for item in fileList:
                    wdata.write(item)

    def modifyTestcase(self, pathName=''):
        newModelList = []
        with open(Setting.BASE_PATH + '/src/com/nrtest/sea/testcase/demo_new/test_TmnlInstallDetai_debug.py', 'rt',
                  encoding='utf-8') as rdata:
            line = 0
            for index, nlVlaue in enumerate(rdata.readlines(), 1):
                if 'assert_query_result' in nlVlaue:
                    line = 1
                if line == 1:
                    newModelList.append(nlVlaue)
            indexL = []
            for i, it in enumerate(newModelList, 0):
                if '@data' in it:
                    indexL.append(i)

        fileList = []
        with open(pathName, 'rt', encoding='utf-8') as rdata:
            desvalue = ''
            stopRun = 0
            p = 0
            lp = self.knowDataLine(pathName)
            for index, value in enumerate(rdata.readlines(), 1):

                if '@data' in value:
                    stopRun = 1
                    desvalue = value
                    newModelList[indexL[0]] = desvalue
                    newModelList[indexL[1]] = desvalue
                else:
                    if int(lp[0]) < index < int(lp[1]) + 1:
                        continue
                    fileList.append(value)
            las_empty = fileList[len(fileList)-1][0:fileList[len(fileList)-1].index('self')]

            fileList.pop()
            fileList.append(las_empty+'self.btn_query()'+'\n')
        fileList.extend(newModelList)
        if 'from com.nrtest.common.BeautifulReport' not in fileList:
            fileList.insert(12, 'from com.nrtest.common.BeautifulReport import BeautifulReport' + '\n')
        op = []
        r = 0
        for j, k in enumerate(fileList, 0):

            if 'query(self' in k:
                   r = 1

            if r == 1 and '#' in  k:
                op.append(j)

        le = int(op[0])

        se = fileList[le][0:fileList[le].index('#')] + '# 注册菜单' + '\n'+ fileList[le][0:fileList[le].index('#')] + "self.menu_name = para['MENU_NAME']"+'\n'
        fileList.insert(le, se)


        with open(pathName, 'wt', encoding='utf-8') as wdata:
            for item in fileList:
                wdata.write(item)


if __name__ == '__main__':
    gu = GuoProgram()
    # lis =  list_dir(r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\base_app\dataGatherMan\gatherQualityAnalyze')
    # print(lis)
    # for item in lis:
    # gu.modifyTestcase(r'D:\PyWorkspace\SEA2017\src\com\nrtest\sea\testcase\sys_mam\sysConfigMan\test_sysDictMan.py')
    gu.modifyPages(r'D:\PyWorkspace\SEA2017\src\com\nrtest\sea\pages\sys_mam\sysConfigMan\sysDictMan_page.py')
    # readData('99913230', name='终端数')
    # 99913260
    # gu.modifyTestcase(
    #     r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\sys_mam\archivesVerficationMan\test_scriptResultDetail.py')
    # print(list_dir(path))
    # lis = ['D:/pythonworkspace/SEA2017/src/com/nrtest/sea/pages/sys_mam/archivesVerficationMan/dataCheckTaskSet_page.py', 'D:/pythonworkspace/SEA2017/src/com/nrtest/sea/pages/sys_mam/archivesVerficationMan/scriptCheckTaskSet_page.py', 'D:/pythonworkspace/SEA2017/src/com/nrtest/sea/pages/sys_mam/archivesVerficationMan/scriptResultDetail_page.py' ]
    # gu = GuoProgram()
    # for item in lis:
    #     gu.modifyPages(item)



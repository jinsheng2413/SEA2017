# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: guoProgram.py
@time: 2018/12/18 0018 19:37
@desc:
"""
from com.nrtest.common.setting import Setting
from com.nrtest.sea.exp.fr import *

# from com.nrtest.sea.exp.mysaql import readData


path = 'D:/pythonworkspace/SEA2017/src/com/nrtest/sea/testcase/sys_mam/archivesVerficationMan'


class GuoProgram(object):
    def readAsswert(self):
        ModelList = []
        with open(Setting.BASE_PATH + '/src/com/nrtest/sea/testcase/demo_new/test_TmnlInstallDetai_debug.py', 'rt',
                  encoding='utf-8') as rdata:
            line = 0
            for index, nlVlaue in enumerate(rdata.readlines(), 0):
                if 'assert_query_result' in nlVlaue:
                    line = 1
                if line == 1:
                    ModelList.append(nlVlaue)
                    # print(newModelList)
            return ModelList

    def readdemo(self):

        with open(Setting.BASE_PATH + '/src/com/nrtest/sea/testcase/demo_new/test_TmnlInstallDetai_debug.py', 'rt',
                  encoding='utf-8') as rdata:
            newList = []
            star = 0
            for k, v in enumerate(rdata, 0):
                if '# 打开菜单' in v:
                    star = 1
                if 'menuPage.remove_dt_readonly()' in v:
                    star = 2
                if star == 1:
                    newList.append(v)
                if star == 2:
                    newList.append(v)
                    return newList

    def strEmpty(self, stree):
        for i, item in enumerate(stree, 0):
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
            for i, item in enumerate(fileList, 1):
                if item.find('Sel') > 0 or item.find('*locator') > 0:
                    li.append(i + 1)
                    if len(li) == 2:
                        index_list.append(li)
                        li = []
            for i in range(0, len(index_list) - 1):
                index_list[i][1] = int(index_list[i][1]) - 1
            for j, v in enumerate(fileList, 0):
                if 'self.' in v:
                    fileList[j] = fileList[j][0:v.index('self.')] + '#' + fileList[j].strip() + '\n'

            # for it  in index_list:
            #        for j in range(it[0],it[1]):
            #                fileList[j] = fileList[j][0:self.strEmpty(fileList[j])] + '#'+fileList[j][self.strEmpty(fileList[j]):len(fileList[j])-1]+'\n'
            #        fileList.insert(it[1]+1,fileList[it[0]+1][0:self.strEmpty(fileList[it[0]+1])]+'self.selectDropDown(options)'+'\n')

            with open(pathName, 'wt', encoding='utf-8') as wdata:
                for item in fileList:
                    wdata.write(item)

    def modifyTestcase(self, pathName=''):
        list1 = self.readdemo()
        list2 = self.readAsswert()
        # --------------------
        fileList = []
        intoList = []
        with open(pathName, 'rt', encoding='utf-8') as rdata:
            desvalue = ''
            stopRun = 0
            p = 0
            lp = self.knowDataLine(pathName)
            # 获取菜单编号，加入到一个列表中
            for index, value in enumerate(rdata.readlines(), 1):
                if 'cls.driver' in value:
                    intoList.append(value[value.index('(') + 1:value.index(')')])
        list1[1] = list1[1].replace('DataGatherMan_data.tmnlInstallDetail_para', intoList[0])
        with open(pathName, 'rt', encoding='utf-8') as rdata2:
            #     #ddt 获取参数项加入列表
            stress = ''.join(rdata2.readlines())
            new_stree = stress[stress.index('@data'):stress.find('))', stress.index('@data')) + 2]
            intoList.append(new_stree)
        strr = '@data(*DataAccess.getCaseData(DataGatherMan_data.tmnlInstallDetail_para, DataGatherMan_data.tmnlInstallDetail_tabOne))'
        list2[16] = list2[16].replace(strr, intoList[1])
        strr2 = 'DataGatherMan_data.tmnlInstallDetail_para, DataGatherMan_data.tmnlInstallDetail_tabOne'
        list2[24] = list2[24].replace(strr2, intoList[1][intoList[1].index('Data(') + 5:intoList[1].index('))')])
        if strr in list2[16]:
            print('=================')
        # print(list2)
        # print(intoList[1])
        # 读取文件加入列表
        with open(pathName, 'rt', encoding='utf-8') as rdata3:
            l = 0
            for j, v in enumerate(rdata3.readlines(), 0):
                fileList.append(v)
                if 'btn' in v:
                    break
        fileList.extend(list2)
        # f,l = 0,0
        # for i,o in enumerate(fileList,0):
        #     if '打开菜单' in o:
        #         f = i
        #         print(f)
        #     if  '@classmethod' in o and i>f:
        #
        #         l = i
        #         print(l)

        k = 0
        for i, v in enumerate(fileList, 0):
            if '开始执行' in v:
                k = i
                break
        for i, g in enumerate(list1, 1):
            fileList.insert(k + i, g)
        n = 0
        for i, p in enumerate(fileList, 0):
            if 'from' in p:
                n = i
                # fileList.insert(i,'from com.nrtest.common.BeautifulReport import BeautifulReport'+'\n')
                fileList.insert(i, 'from unittest import TestCase\n')
                break
        p = 0
        for i, p in enumerate(fileList, 0):
            if 'common.BeautifulReport' not in p:
                p = 1
        if p == 1:
            fileList.insert(14, 'from com.nrtest.common.BeautifulReport import BeautifulReport' + '\n')

        with open(pathName, 'wt', encoding='utf-8') as wdata:
            for item in fileList:
                wdata.write(item)


if __name__ == '__main__':
    gu = GuoProgram()
    lis = list_dir(r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\adv_app\lineLossAnalysis')
    # lis = gu.readAsswert()
    # print(lis)

    # print(lis)
    # for item in lis:
    # gu.modifyTestcase(r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\adv_app\lineLossAnalysis\lineLossIndexEvaluation\test_aeeseementResultStatistics.py')
    gu.modifyPages(
        r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\pages\adv_app\lineLossAnalysis\lineLossStatisticsAnalysis\tgLineLossAnalysis_page.py')
    # readData('99913230', name='终端数')
    # 99913260
    # gu.modifyTestcase(
    #     r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\sys_mam\archivesVerficationMan\test_scriptResultDetail.py')
    # print(list_dir(path))
    # lis = ['D:/pythonworkspace/SEA2017/src/com/nrtest/sea/pages/sys_mam/archivesVerficationMan/dataCheckTaskSet_page.py', 'D:/pythonworkspace/SEA2017/src/com/nrtest/sea/pages/sys_mam/archivesVerficationMan/scriptCheckTaskSet_page.py', 'D:/pythonworkspace/SEA2017/src/com/nrtest/sea/pages/sys_mam/archivesVerficationMan/scriptResultDetail_page.py' ]
    # gu = GuoProgram()
    # for item in lis:
    #     gu.modifyTestcase(item)

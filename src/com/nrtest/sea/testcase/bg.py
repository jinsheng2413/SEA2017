# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: bg.py
@time: 2018/7/4 0004 17:15
@desc:
"""

import unittest

from com.nrtest.sea.testcase.adv_app.vipConsMan.unControlPlant.test_unControlPlantGatherMon_tab2 import \
    Test_UnControlPlantGatherMon_2

suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
    Test_UnControlPlantGatherMon_2))
# tests = [TestGatherSuccessRate('test_epp_task_type')]
# suite.addTests(tests)


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

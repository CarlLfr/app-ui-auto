#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/23
# @Author  : lfr

import unittest
import time
from common.base_log import log
from common.base_driver import BaseDriver
from b_page.my_set import MySet
from b_page.page_init import PageInit

class TestSet(unittest.TestCase):
    '''
    测试设置页其他功能（除修改密码）
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化进入App首页'''
        log.info("---开始执行用例：提交商品品牌信息---")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    def test_brandInfo_submit(self):
        '''验证商家品牌信息提交功能'''
        log.info("验证设置页商家品牌信息提交功能")
        ms = MySet(self.driver)
        # ->我的->设置
        ms.enter_to_my()
        ms.enter_to_set()
        # 提交商家品牌信息操作
        ms.brand_opera("自动化测试")
        # 断言是否提交成功
        result = ms.is_toast_exist("提交成功")
        # log.info("result: %s" % result)
        self.assertTrue(result)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(2)
        cls.driver.quit()
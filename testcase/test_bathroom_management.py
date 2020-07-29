#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/07/14
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.base_manage_bathroom_management import BathroomManagement
from b_page.page_init import PageInit

class TestBathroomManagement(unittest.TestCase):
    '''
    全部应用，浴室管理-新增、编辑、删除浴室
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、删除浴室-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    def test_01_add_bathroom(self):
        '''验证新增浴室'''
        log.info("验证新增浴室")
        # ->全部应用->浴室管理
        bm = BathroomManagement(self.driver)
        bm.enter_to_all_applications()
        bm.enter_to_bathroom_management()
        # 新增浴室操作
        bm.add_bathroom_opera()
        # 断言是否新增成功
        toast_text = bm.get_toast_text()
        self.assertEqual(toast_text, bm.add_success_toast)
        result = bm.is_exist_element(bm.bathroom_name)
        self.assertTrue(result)

    def test_02_edit_bathroom(self):
        '''验证编辑浴室'''
        log.info("验证编辑浴室")
        bm = BathroomManagement(self.driver)
        # 编辑浴室操作
        bm.edit_bathroom_opera()
        # 断言是否编辑成功
        toast_text = bm.get_toast_text()
        self.assertEqual(toast_text, bm.edit_success_toast)
        result = bm.is_exist_element(bm.edit_bathroom_name)
        self.assertTrue(result)

    def test_03_delete_bathroom(self):
        '''验证删除浴室'''
        log.info("验证删除浴室")
        bm = BathroomManagement(self.driver)
        # 删除浴室操作
        bm.delete_bathroom_opera()
        # 断言是否编辑成功
        result = bm.is_exist_element(bm.edit_bathroom_name)
        self.assertFalse(result)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
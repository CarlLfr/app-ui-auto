#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/18
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.base_manage_shop_management import ShopManagement
from b_page.page_init import PageInit

class TestShopManagement(unittest.TestCase):
    '''
    基础管理，店铺管理-新增、编辑、删除
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、删除店铺-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    # @unittest.skip("调试跳过")
    def test_01_add_shop(self):
        '''验证新增店铺'''
        log.info("验证新增店铺")
        # ->全部应用->店铺管理
        smg = ShopManagement(self.driver)
        smg.enter_to_all_applications()
        smg.enter_to_shop_management()
        # 新增店铺操作
        smg.add_shop_opera()
        # 断言是否新增成功
        r_1 = smg.is_exist_element(smg.shop_name)
        self.assertTrue(r_1)

    def test_02_edit_shop(self):
        '''验证编辑店铺'''
        log.info("验证编辑店铺")
        smg = ShopManagement(self.driver)
        # 编辑店铺操作
        smg.edit_shop_opera()
        # 断言是否编辑成功
        toast_text = smg.get_toast_text()
        r = smg.is_exist_element(smg.edit_shop_name)
        self.assertEqual(toast_text, smg.edit_success_toast)
        self.assertTrue(r)

    def test_03_delete_shop(self):
        '''验证删除店铺'''
        log.info("验证删除店铺")
        smg = ShopManagement(self.driver)
        # 编辑店铺操作
        smg.delete_shop_opera()
        # 断言是否删除成功
        toast_text = smg.get_toast_text()
        r = smg.is_exist_element(smg.edit_shop_name)
        self.assertEqual(toast_text, smg.delete_success_toast)
        self.assertFalse(r)


    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
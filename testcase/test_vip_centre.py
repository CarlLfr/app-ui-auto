#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/03
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.manage_marketing import ManageMarketing
from b_page.page_init import PageInit

class TestVipCentre(unittest.TestCase):
    '''
    营销管理-VIP中心，新增、编辑、删除
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、删除VIP-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    def test_01_add_vip(self):
        '''验证新增vip'''
        log.info("验证新增vip")
        # ->全部应用->VIP中心
        mm = ManageMarketing(self.driver)
        mm.enter_to_all_applications()
        mm.enter_to_vip_center()
        # 新增vip
        mm.add_vip_opera()
        # 断言是否新增成功
        r_1 = mm.is_toast_exist(mm.vip_add_success_toast)
        r_2 = mm.is_toast_exist(mm.belong_store_name)
        self.assertTrue(r_1)
        self.assertTrue(r_2)

    # @unittest.skip("调试 跳过")
    def test_02_edit_vip(self):
        '''验证编辑vip'''
        log.info("验证编辑vip")
        # 编辑vip
        mm = ManageMarketing(self.driver)
        mm.edit_vip_opera()
        # 断言编辑是否成功
        r_1 = mm.is_toast_exist(mm.vip_edit_success_toast)
        r_2 = mm.is_toast_exist(str(mm.modify_limit_time))
        self.assertTrue(r_1)
        self.assertTrue(r_2)

    # @unittest.skip("调试 跳过")
    def test_03_delete_vip(self):
        '''验证删除vip'''
        log.info("验证删除vip")
        # 删除vip
        mm = ManageMarketing(self.driver)
        mm.delete_vip_opera()
        # 断言删除是否成功
        r_1 = mm.is_exist_element(mm.vip_centre_title)
        r_2 = mm.is_exist_element(mm.belong_store_name)
        self.assertTrue(r_1)
        self.assertFalse(r_2)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
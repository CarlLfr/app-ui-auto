#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/05/26
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.manage_marketing import ManageMarketing
from b_page.page_init import PageInit

@pytest.mark.market_management
class TestLimitedTimeDiscount(unittest.TestCase):
    '''
    营销管理-限时优惠，新增、编辑、删除
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、删除限时优惠-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    # @unittest.skip("跳过")
    def test_01_add_limited_time_discount(self):
        '''验证新增限时优惠'''
        log.info("验证新增限时优惠")
        # ->全部应用->限时优惠
        mm = ManageMarketing(self.driver)
        mm.enter_to_all_applications()
        mm.enter_to_limited_time_discount()
        # 新增限时优惠
        mm.add_discount_opera()
        # 断言是否新增成功
        r_1 = mm.is_toast_exist(mm.add_success_toast)
        r_2 = mm.is_exist_element(mm.belong_store_name)
        self.assertTrue(r_1)
        self.assertTrue(r_2)

    # @unittest.skip("跳过")
    def test_02_add_currency_ticket(self):
        '''验证编辑限时优惠'''
        log.info("验证编辑限时优惠")
        # 编辑限时优惠
        mm = ManageMarketing(self.driver)
        mm.edit_discount_opera()
        # 断言是否编辑成功
        r_1 = mm.is_toast_exist(mm.edit_success_toast)
        r_2 = mm.is_exist_element(str(mm.edit_discount))
        self.assertTrue(r_1)
        self.assertTrue(r_2)
        # 开关
        # mm.switch_discount_opera()
        # r_3 = mm.is_exist_element(mm.discount_switch_state)
        # self.assertTrue(r_3)

    # @unittest.skip("跳过")
    def test_03_delete_currency_ticket(self):
        '''验证删除限时优惠'''
        log.info("验证删除限时优惠")
        # 删除限时优惠
        mm = ManageMarketing(self.driver)
        mm.delete_discount_opera()
        # 断言是否删除成功
        r_1 = mm.is_toast_exist(mm.delete_success_toast)
        r_2 = mm.is_exist_element(mm.belong_store_name)
        self.assertTrue(r_1)
        self.assertFalse(r_2)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/05/21
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.manage_marketing import ManageMarketing
from b_page.page_init import PageInit

@pytest.mark.market_management
class TestCurrencyTicketManage(unittest.TestCase):
    '''
    营销管理-通用小票管理，新增、编辑、删除
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、删除通用小票-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    def test_01_add_currency_ticket(self):
        '''验证新增通用小票'''
        log.info("验证新增通用小票")
        # ->首页->全部应用->通用小票管理
        mm = ManageMarketing(self.driver)
        mm.enter_to_all_applications()
        mm.enter_to_currency_ticket_manage()
        # 新增通用小票
        mm.add_currency_ticket_opera()
        # 断言是否新增成功
        r_1 = mm.is_exist_element(mm.currency_ticket_manage_page_title)
        r_2 = mm.is_exist_element(mm.currency_ticket_store_name)
        self.assertTrue(r_1)
        self.assertTrue(r_2)

    def test_02_add_currency_ticket(self):
        '''验证编辑通用小票'''
        log.info("验证编辑通用小票")
        # 编辑通用小票
        mm = ManageMarketing(self.driver)
        mm.edit_currency_ticket_opera()
        # 断言是否编辑成功
        r_1 = mm.is_exist_element(mm.switch_state_1)
        r_2 = mm.is_exist_element(str(mm.sell_coin))
        self.assertTrue(r_1)
        self.assertTrue(r_2)

    def test_03_delete_currency_ticket(self):
        '''验证删除通用小票'''
        log.info("验证删除通用小票")
        # 删除通用小票
        mm = ManageMarketing(self.driver)
        mm.delete_opera()
        # 断言是否删除成功
        r_1 = mm.is_exist_element(mm.currency_ticket_manage_page_title)
        r_2 = mm.is_exist_element(mm.currency_ticket_store_name)
        self.assertTrue(r_1)
        self.assertFalse(r_2)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

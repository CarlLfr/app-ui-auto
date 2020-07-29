#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/16
# @Author  : lfr

import pytest
import unittest
import datetime
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.manage_marketing import ManageMarketing
from b_page.page_init import PageInit

@pytest.mark.market_management
class TestCurrencyTicketManage(unittest.TestCase):
    '''
    营销管理-通用小票管理，充值通用小票、会员充值记录、小票回收
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：充值通用小票、会员充值记录、小票回收-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    # @unittest.skip("调试，跳过")
    def test_01_recharge_coin(self):
        '''验证充值通用小票'''
        log.info("验证充值通用小票")
        # ->全部应用->通用小票管理
        mm = ManageMarketing(self.driver)
        mm.enter_to_all_applications()
        mm.enter_to_currency_ticket_manage()
        # 充值通用小票操作
        mm.recharge_coin_opera()
        # 断言充值是否成功
        r_1 = mm.is_toast_exist(mm.recharge_success_toast)
        self.assertTrue(r_1)

    def test_02_query_recharge_record(self):
        '''验证查询会员充值记录'''
        log.info("验证查询会员充值记录")
        # 通用小票管理页-会员充值记录查询操作
        mm = ManageMarketing(self.driver)
        mm.recharge_record_opera()
        date = mm.the_first_recharge_record_time()
        date_time = datetime.datetime.now().strftime('%Y-%m-%d')
        type_text = mm.the_first_recharge_record_type()
        # 断言：1，搜索出来的第一条记录的日期=今天的日期；2，type=商户代充
        self.assertEqual(date, date_time)
        self.assertEqual(type_text, mm.recharge_type_1)

        # 返回至通用小票管理页面
        mm.back_to_manage_page_opera()

    def test_03_member_management(self):
        '''验证会员管理-回收通用小票'''
        log.info("验证会员管理-回收通用小票")
        # 通用小票管理页-回收小票操作
        mm = ManageMarketing(self.driver)
        mm.member_manage_recovery_coin_opera()
        # 断言回收小票是否成功
        r_1 = mm.is_toast_exist(mm.recovery_success_toast)
        self.assertTrue(r_1)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
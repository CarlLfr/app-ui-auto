#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/24
# @Author  : lfr

import time
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.my_wallet import MyWallet
from b_page.page_init import PageInit

class TestMyWallet(unittest.TestCase):
    '''
    验证我的钱包：收支明细页筛选，体现记录
    '''
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：消息中心-----")
        self.driver = BaseDriver().android_driver()
        PageInit(self.driver).init_to_home()

    def test_income_out_screen(self):
        '''验证我的钱包-收支明细页筛选并验证'''
        log.info("验证我的钱包-收支明细页筛选并验证")
        # 进入我的钱包页
        mw = MyWallet(self.driver)
        mw.enter_to_my()
        mw.enter_to_myWallet()
        # 筛选操作
        mw.screen_opera()
        # 选择第一条筛选结果进入详情页
        mw.enter_to_result_detail()

        # 断言详情页与筛选条件是否一致
        r_1 = mw.is_exist_element(mw.order_detail_name)
        self.assertTrue(r_1)
        r_2 = mw.is_exist_element(mw.order_detail_store)
        self.assertTrue(r_2)

    @unittest.skip("该用例未调试")
    def test_withdraw_recode(self):
        '''验证我的钱包-体现记录页展示是否正常'''
        log.info("验证我的钱包-体现记录页展示是否正常")
        # 进入我的钱包-体现记录页-第一条记录详情
        mw = MyWallet(self.driver)
        mw.enter_to_my()
        mw.enter_to_myWallet()
        mw.enter_to_withdraw_record()

        # 断言展示是否正常
        result = mw.is_exist_element(mw.record_detail_text)
        self.assertFalse(result)

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        pass
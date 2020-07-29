#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/26
# @Author  : lfr

import time
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from common.base_operate import get_yaml_value
from config.path_config import TEST_ACCOUNT_PATH
from b_page.home import HomePage
from b_page.page_init import PageInit

class TestHome(unittest.TestCase):
    '''
    首页，今日收益，当月收益，总收益
    '''
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：首页-----")
        self.driver = BaseDriver().android_driver()
        PageInit(self.driver).init_to_home()

        # 判断今日收益展示是否为零
        # today_revenue_text = HomePage(self.driver).today_revenue().text
        # global today_revenue_text

    # @unittest.skipIf(today_revenue_text=="0.00", "今日收益为零则跳过不执行该用例")
    # @unittest.skip("调试跳过")
    def test_today_revenue(self):
        '''验证首页-今日收益导出功能'''
        log.info("验证首页-今日收益导出功能")
        # 进入今日收益页面，点击导出
        hp = HomePage(self.driver)
        # 判断今日收益展示是否为零，为零则不执行导出操作
        today_revenue_text = hp.today_revenue().text
        if today_revenue_text == "0.00":
            log.info("今日收益：%s" % today_revenue_text)
            return
        else:
            hp.enter_to_today_revenue()
            email = get_yaml_value(TEST_ACCOUNT_PATH, 'email')
            hp.export_opera(email)

            # 断言导出是否成功
            result = hp.is_toast_exist(hp.export_success_toast)
            self.assertTrue(result)

    # @unittest.skip("调试跳过")
    def test_month_revenue(self):
        '''验证首页-当月收益导出功能'''
        log.info("验证首页-当月收益导出功能")
        # 进入当月收益页面，点击导出
        hp = HomePage(self.driver)
        hp.enter_to_month_revenue()
        email = get_yaml_value(TEST_ACCOUNT_PATH, 'email')
        hp.export_opera(email)

        # 断言导出是否成功
        result = hp.is_toast_exist(hp.export_success_toast)
        self.assertTrue(result)

    def test_total_revenue(self):
        '''验证首页-总收益导出功能'''
        log.info("验证首页-总收益导出功能")
        # 进入总收益页面，进入第一条收益记录，点击导出
        hp = HomePage(self.driver)
        hp.enter_to_total_revenue()
        hp.total_to_month()
        email = get_yaml_value(TEST_ACCOUNT_PATH, 'email')
        hp.export_opera(email)

        # 断言导出是否成功
        result = hp.is_toast_exist(hp.export_success_toast)
        self.assertTrue(result)

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        pass
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/27
# @Author  : lfr

import time
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from common.base_operate import get_yaml_value
from config.path_config import TEST_ACCOUNT_PATH
from b_page.report_form import ReportFormPage
from b_page.page_init import PageInit

class TestReportForm(unittest.TestCase):
    '''
    报告页，水流导出，流水筛选，订单筛选
    '''
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：报告页-----")
        self.driver = BaseDriver().android_driver()
        PageInit(self.driver).init_to_home()

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # @unittest.skip("调试跳过")
    def test_report_export(self):
        '''验证报表页流水导出功能'''
        log.info("验证报表页导出功能")
        # 进入报表页-流水，进行导出操作
        rfp = ReportFormPage(self.driver)
        rfp.enter_to_report()
        email = get_yaml_value(TEST_ACCOUNT_PATH, 'email')
        rfp.report_export_opera(email)

        # 断言导出是否成功
        result = rfp.is_toast_exist(rfp.export_success_toast)
        self.assertTrue(result)

    @unittest.skip("调试跳过，测试账号建好后需完善脚本")
    def test_report_screen(self):
        '''验证报表页流水筛选功能'''
        log.info("验证报表页流水筛选功能")
        # 进入报表页-流水，进行筛选操作
        rfp = ReportFormPage(self.driver)
        rfp.enter_to_report()
        rfp.report_screen_opera()

        # 断言筛选结果是否正确
        result = rfp.is_exist_element(rfp.store_text)
        self.assertTrue(result)

    def test_report_order(self):
        '''验证报表页订单筛选功能'''
        log.info("验证报表页订单筛选功能")
        # 进入报表页-订单，选择店铺
        rfp = ReportFormPage(self.driver)
        rfp.enter_to_report()
        rfp.report_order_opera()

        # 断言结果是否正确
        r_1 = rfp.is_exist_element(rfp.title_text)
        r_2 = rfp.is_exist_element(rfp.order_store_text)
        self.assertTrue(r_1)
        self.assertTrue(r_2)
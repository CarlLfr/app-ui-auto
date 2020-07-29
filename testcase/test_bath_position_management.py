#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/07/21
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.base_manage_bath_position_management import BathPositionManagement
from b_page.page_init import PageInit

class TestBathroomManagement(unittest.TestCase):
    '''
    全部应用，浴位管理-新增、编辑、高级设置、删除浴位设备
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、高级设置、删除浴位设备-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    # @unittest.skip("调试，跳过")
    def test_01_add_bath_position(self):
        '''验证新增浴位'''
        log.info("验证新增浴位")
        bm = BathPositionManagement(self.driver)
        # ->全部应用->浴位管理
        bm.enter_to_all_applications()
        bm.enter_to_bath_position_management()
        # 新增浴位
        bm.add_bath_device_opera()
        # 断言是否新增成功
        toast_text = bm.get_toast_text()
        self.assertEqual(toast_text, bm.add_success_toast)
        result = bm.is_exist_element(str(bm.yw_no))
        self.assertTrue(result)

    # @unittest.skip("调试，跳过")
    def test_02_edit_bath_position(self):
        '''验证编辑浴位'''
        log.info("验证编辑浴位")
        bm = BathPositionManagement(self.driver)
        # 编辑浴位操作
        bm.edit_bath_position_opera()
        # 断言是否编辑成功
        r_1 = bm.is_exist_element(str(bm.edit_yw_no))
        r_2 = bm.is_exist_element(bm.bath_position_detail_title)
        self.assertTrue(r_1)
        self.assertTrue(r_2)

    # @unittest.skip("调试，跳过")
    def test_03_set_bath_position(self):
        '''验证浴位高级设置'''
        log.info("验证浴位高级设置")
        bm = BathPositionManagement(self.driver)
        # 高级设置浴位操作
        bm.set_bath_position_opera()
        # 断言是否设置成功
        toast_text = bm.get_toast_text()
        self.assertEqual(toast_text, bm.set_success_toast)

    # @unittest.skip("调试，跳过")
    def test_04_delete_bath_position(self):
        '''验证删除浴位'''
        log.info("验证删除浴位")
        bm = BathPositionManagement(self.driver)
        # 删除浴位操作
        bm.delete_bath_position_opera()
        # 断言是否删除成功
        # r_1 = bm.is_exist_element(str(bm.edit_yw_no))
        r_2 = bm.is_exist_element(bm.bath_position_title)
        # self.assertFalse(r_1)
        self.assertTrue(r_2)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
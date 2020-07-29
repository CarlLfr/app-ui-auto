#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/17
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.base_manage_personnel_management import PersonnelManagement
from b_page.page_init import PageInit

class TestPersonnelManagement(unittest.TestCase):
    '''
    基础管理，人员管理-新增、编辑、删除
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、删除人员-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    def test_01_add_person(self):
        '''验证新增人员'''
        log.info("验证新增人员")
        # ->全部应用->人员管理
        pmg = PersonnelManagement(self.driver)
        pmg.enter_to_all_applications()
        pmg.enter_to_personnel_management()
        # 新增人员操作
        pmg.add_person_opera()
        # 断言是否新增成功
        r_1 = pmg.is_toast_exist(pmg.add_person_success_toast)
        r_2 = pmg.is_exist_element(pmg.name)
        self.assertTrue(r_1)
        self.assertTrue(r_2)

    def test_02_edit_person(self):
        '''验证编辑人员'''
        log.info("验证编辑人员")
        pmg = PersonnelManagement(self.driver)
        # 编辑人员操作
        pmg.edit_person_opera()
        # 断言是否编辑成功
        r_1 = pmg.is_toast_exist(pmg.edit_success_toast)
        self.assertTrue(r_1)

    def test_03_delete_person(self):
        '''验证删除人员'''
        log.info("验证删除人员")
        pmg = PersonnelManagement(self.driver)
        # 删除操作
        pmg.delete_person_opera()
        # 断言是否删除成功
        r_1 = pmg.is_toast_exist(pmg.delete_success_toast)
        self.assertTrue(r_1)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
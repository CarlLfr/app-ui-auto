#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/07/13
# @Author  : lfr

import time
from b_page.home import HomePage
from appium.webdriver.common.mobileby import MobileBy as By

class BathroomManagement(HomePage):
    '''
    全部应用-浴室管理
    '''
    bathroom_management_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="浴室管理"]')
    add_loc = (By.ID, 'com.qekj.merchant:id/iv_add')
    bathroom_name_input_loc = (By.ID, 'com.qekj.merchant:id/et_device_name')
    belong_shop_loc = (By.ID, 'com.qekj.merchant:id/rl_store')
    confirm_loc = (By.ID, 'com.qekj.merchant:id/btnSubmit')
    sex_loc = (By.ID, 'com.qekj.merchant:id/rl_sex')
    submit_loc = (By.ID, 'com.qekj.merchant:id/rl_submit')
    bathroom_name = "测试新增浴室"
    add_success_toast = "浴室新增成功"

    # 编辑
    bathroom_loc = (By.XPATH, '//android.widget.TextView[@text="测试新增浴室"]/..')
    edit_loc = (By.ID, 'com.qekj.merchant:id/rl_edit')
    edit_bathroom_name = "测试编辑浴室"
    edit_success_toast = "浴室编辑成功"

    # 删除
    delete_loc = (By.ID, 'com.qekj.merchant:id/rl_del')
    sure_again_loc = (By.ID, 'android:id/button1')


    def enter_to_bathroom_management(self):
        '''进入浴室管理页'''
        self.bathroom_management_btn().click()

    # 新增
    def add_bathroom_opera(self):
        '''新增浴室操作'''
        self.add_btn().click()
        self.bathroom_name_input().send_keys(self.bathroom_name)
        self.belong_shop().click()
        self.confirm_btn().click()
        self.sex().click()
        self.confirm_btn().click()
        self.submit_btn().click()


    def bathroom_management_btn(self):
        '''全部应用-浴室管理'''
        br_ele = self.get_visible_element(self.bathroom_management_loc)
        return br_ele

    def add_btn(self):
        '''浴室管理-新增'''
        br_ele = self.get_visible_element(self.add_loc)
        return br_ele

    def bathroom_name_input(self):
        '''新增浴室-浴室名称'''
        br_ele = self.get_visible_element(self.bathroom_name_input_loc)
        return br_ele

    def belong_shop(self):
        '''新增浴室-所属店铺'''
        br_ele = self.get_visible_element(self.belong_shop_loc)
        return br_ele

    def confirm_btn(self):
        '''confirm按钮'''
        br_ele = self.get_visible_element(self.confirm_loc)
        return br_ele

    def sex(self):
        '''新增浴室-性别'''
        br_ele = self.get_visible_element(self.sex_loc)
        return br_ele

    def submit_btn(self):
        '''提交按钮'''
        br_ele = self.get_visible_element(self.submit_loc)
        return br_ele



    # 编辑
    def edit_bathroom_opera(self):
        '''编辑浴室操作'''
        self.bathroom_new().click()
        self.edit_btn().click()
        self.bathroom_name_input().send_keys(self.edit_bathroom_name)
        self.submit_btn().click()


    def bathroom_new(self):
        '''新增浴室条目'''
        br_ele = self.get_visible_element(self.bathroom_loc)
        return br_ele

    def edit_btn(self):
        '''编辑按钮'''
        br_ele = self.get_visible_element(self.edit_loc)
        return br_ele



    # 删除
    def delete_bathroom_opera(self):
        '''删除浴室操作'''
        self.delete_btn().click()
        self.sure_again_btn().click()
        time.sleep(1)



    def delete_btn(self):
        '''删除按钮'''
        br_ele = self.get_visible_element(self.delete_loc)
        return br_ele

    def sure_again_btn(self):
        '''删除再次确认按钮'''
        br_ele = self.get_visible_element(self.sure_again_loc)
        return br_ele
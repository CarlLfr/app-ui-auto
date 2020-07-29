#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/16
# @Author  : lfr

import time
from b_page.home import HomePage
from appium.webdriver.common.mobileby import MobileBy as By

class ShopManagement(HomePage):
    '''
    基础管理-店铺管理
    '''
    shop_management_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="店铺管理"]')
    # 新增店铺
    add_loc = (By.ID, 'com.qekj.merchant:id/iv_add')
    shop_name_input_loc = (By.ID, 'com.qekj.merchant:id/et_shop_name')
    shop_type_loc = (By.ID, 'com.qekj.merchant:id/rl_store_type')
    shop_type_confirm_loc = (By.ID, 'com.qekj.merchant:id/btnSubmit')
    school_loc = (By.ID, 'com.qekj.merchant:id/rl_school')
    school_search_input_loc = (By.ID, 'com.qekj.merchant:id/et_search')
    school_name_loc = (By.XPATH, '//android.widget.TextView[@text="浙江大学(之江校区)"]')
    business_time_loc = (By.XPATH, '//android.widget.TextView[@text="营业时间"]')
    business_time_sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    service_phone_input_loc = (By.XPATH, '//android.widget.EditText[@text="请填写客服电话"]')
    submit_loc = (By.ID, 'com.qekj.merchant:id/rl_submit')
    school_name = "浙江大学(之江校区)"
    shop_name = "appUI自动化新增店铺"
    service_phone = 13567834546

    # 编辑
    shop_management_name_loc = (By.XPATH, '//android.widget.TextView[@text="appUI自动化新增店铺"]')
    edit_loc = (By.ID, 'com.qekj.merchant:id/rl_edit')
    edit_shop_name = "appUI自动化编辑店铺"
    edit_success_toast = "编辑成功"

    # 删除
    shop_management_edit_name_loc = (By.XPATH, '//android.widget.TextView[@text="appUI自动化编辑店铺"]')
    delete_loc = (By.ID, 'com.qekj.merchant:id/rl_delete')
    delete_sure_loc = (By.ID, 'android:id/button1')
    delete_success_toast = "删除成功"


    def enter_to_shop_management(self):
        '''管理页点击进入店铺管理'''
        self.shop_management_btn().click()

    def add_shop_opera(self):
        '''新增店铺操作'''
        self.add_btn().click()
        self.shop_name_input().send_keys(self.shop_name)
        self.shop_type_btn().click()
        self.shop_type_confirm_btn().click()
        self.school_btn().click()
        self.school_search_input().send_keys(self.school_name)
        self.school_name_btn().click()
        self.business_time_btn().click()
        self.business_time_sure_btn().click()
        self.service_phone_input().send_keys(self.service_phone)
        self.submit_btn().click()

    def edit_shop_opera(self):
        '''编辑店铺操作'''
        self.shop_management_name_btn().click()
        self.edit_btn().click()
        self.shop_name_input().clear()
        self.shop_name_input().send_keys(self.edit_shop_name)
        self.submit_btn().click()

    def delete_shop_opera(self):
        '''删除店铺操作'''
        self.shop_management_edit_name_btn().click()
        self.delete_btn().click()
        self.delete_sure_btn().click()


    def shop_management_btn(self):
        '''管理-店铺管理'''
        sm_ele = self.get_visible_element(self.shop_management_loc)
        return sm_ele

    def add_btn(self):
        '''店铺管理-新增按钮'''
        sm_ele = self.get_visible_element(self.add_loc)
        return sm_ele

    def shop_name_input(self):
        '''新增店铺-店铺名称'''
        sm_ele = self.get_visible_element(self.shop_name_input_loc)
        return sm_ele

    def shop_type_btn(self):
        '''新增店铺-店铺类型'''
        sm_ele = self.get_visible_element(self.shop_type_loc)
        return sm_ele

    def shop_type_confirm_btn(self):
        '''新增店铺-店铺类型-确定按钮'''
        sm_ele = self.get_visible_element(self.shop_type_confirm_loc)
        return sm_ele

    def school_btn(self):
        '''新增店铺-学校名称'''
        sm_ele = self.get_visible_element(self.school_loc)
        return sm_ele

    def school_search_input(self):
        '''新增店铺-学校搜索框'''
        sm_ele = self.get_visible_element(self.school_search_input_loc)
        return sm_ele

    def school_name_btn(self):
        '''新增店铺-学校搜索结果选择'''
        ms_ele = self.get_visible_element(self.school_name_loc)
        return ms_ele

    def business_time_btn(self):
        '''新增店铺-营业时间'''
        ms_ele = self.get_visible_element(self.business_time_loc)
        return ms_ele

    def business_time_sure_btn(self):
        '''新增店铺-营业时间-确定按钮'''
        ms_ele = self.get_visible_element(self.business_time_sure_loc)
        return ms_ele

    def service_phone_input(self):
        '''新增店铺-客服电话'''
        ms_ele = self.get_visible_element(self.service_phone_input_loc)
        return ms_ele

    def submit_btn(self):
        '''新增店铺-提交按钮'''
        ms_ele = self.get_visible_element(self.submit_loc)
        return ms_ele


    def shop_management_name_btn(self):
        '''店铺管理-新增的店铺条目'''
        ms_ele = self.get_visible_element(self.shop_management_name_loc)
        return ms_ele

    def edit_btn(self):
        '''店铺详情-编辑按钮'''
        ms_ele = self.get_visible_element(self.edit_loc)
        return ms_ele


    def shop_management_edit_name_btn(self):
        '''店铺管理-编辑后的店铺名称'''
        ms_ele = self.get_visible_element(self.shop_management_edit_name_loc)
        return ms_ele

    def delete_btn(self):
        '''店铺详情-删除按钮'''
        ms_ele = self.get_visible_element(self.delete_loc)
        return ms_ele

    def delete_sure_btn(self):
        '''店铺详情-删除-确定按钮'''
        ms_ele = self.get_visible_element(self.delete_sure_loc)
        return ms_ele





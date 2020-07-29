#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/16
# @Author  : lfr

import time
from b_page.home import HomePage
from appium.webdriver.common.mobileby import MobileBy as By

class PersonnelManagement(HomePage):
    '''
    基础管理-人员管理
    '''
    personnel_management_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="人员管理"]')
    # 新增
    add_person_loc = (By.ID, 'com.qekj.merchant:id/iv_add')
    telephone_input_loc = (By.ID, 'com.qekj.merchant:id/et_phone')
    name_input_loc = (By.ID, 'com.qekj.merchant:id/et_name')
    responsible_for_store_loc = (By.ID, 'com.qekj.merchant:id/rl_select_store')
    search_store_input_loc = (By.ID, 'com.qekj.merchant:id/et_search_shop')
    search_store_name_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_shop_name" and @text="appUl营销管理专用勿操作店铺"]')
    search_sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    # competence_loc = (By.ID, 'com.qekj.merchant:id/rl_permission')
    competence_loc = (By.XPATH, '//android.widget.TextView[@text="权限"]')
    home_tick_loc = (By.XPATH, '//*[@text="首页收益"]/../android.widget.ImageView')
    report_form_tick_loc = (By.XPATH, '//*[@text="报表"]/../android.widget.ImageView')
    store_manage_tick_loc = (By.XPATH, '//*[@text="店铺管理"]/../android.widget.ImageView[2]')
    device_manage_tick_loc = (By.XPATH, '//*[@text="设备管理"]/../android.widget.ImageView[2]')
    order_manage_tick_loc = (By.XPATH, '//*[@text="订单管理"]/../android.widget.ImageView[2]')
    bathroom_manage_tick_loc = (By.XPATH, '//*[@text="浴室管理"]/../android.widget.ImageView[2]')
    to_do_tick_loc = (By.XPATH, '//*[@text="待办事项"]/../android.widget.ImageView[2]')
    limit_time_discount_tick_loc = (By.XPATH, '//*[@text="限时优惠"]/../android.widget.ImageView[2]')
    vip_centre_tick_loc = (By.XPATH, '//*[@text="VIP中心"]/../android.widget.ImageView[2]')
    coupon_record_tick_loc = (By.XPATH, '//*[@text="优惠券记录"]/../android.widget.ImageView[2]')
    fault_manage_tick_loc = (By.XPATH, '//*[@text="故障管理"]/../android.widget.ImageView[2]')
    competence_sure_loc = (By.ID, 'com.qekj.merchant:id/rl_sure')
    submit_loc = (By.ID, 'com.qekj.merchant:id/rl_submit')
    telephone = 13567892354
    name = 'zdhcs'
    store_name = "appUl营销管理专用勿操作店铺"
    add_person_success_toast = "添加成功"

    # 编辑
    person_manage_name_loc = (By.XPATH, '//android.widget.TextView[@text="zdhcs"]')
    edit_loc = (By.ID, 'com.qekj.merchant:id/rl_edit')
    edit_success_toast = "修改成功"

    # 删除
    delete_loc = (By.ID, 'com.qekj.merchant:id/rl_delete')
    delete_sure_loc = (By.ID, 'android:id/button1')
    delete_success_toast = "删除成功"


    # 新增
    def enter_to_personnel_management(self):
        '''管理页-->人员管理'''
        self.personnel_management_btn().click()

    def add_person_opera(self):
        '''人员管理-新增操作'''
        self.add_person_btn().click()
        self.telephone_input().send_keys(self.telephone)
        self.name_input().send_keys(self.name)
        self.responsible_for_store_btn().click()
        self.search_store_input().send_keys(self.store_name)
        time.sleep(1)
        self.search_store_name().click()
        self.search_sure_btn().click()
        time.sleep(1)
        # 权限选择
        self.competence_btn().click()
        self.home_tick_btn().click()
        self.report_form_tick_btn().click()
        self.store_manage_tick_btn().click()
        self.device_manage_tick_btn().click()
        self.competence_sure_btn().click()
        # 提交新增
        self.submit_btn().click()

    def edit_person_opera(self):
        '''人员管理-编辑操作'''
        time.sleep(1)
        self.person_manage_name_btn().click()
        self.edit_btn().click()
        time.sleep(1)
        # 修改权限
        self.competence_btn().click()
        self.store_manage_tick_btn().click()
        self.device_manage_tick_btn().click()
        self.competence_sure_btn().click()
        # 提交编辑
        self.submit_btn().click()

    def delete_person_opera(self):
        '''人员管理-删除操作'''
        time.sleep(1)
        self.person_manage_name_btn().click()
        time.sleep(1)
        self.delete_btn().click()
        self.delete_sure_btn().click()


    def personnel_management_btn(self):
        '''管理-基础管理-人员管理按钮'''
        pm_ele = self.get_visible_element(self.personnel_management_loc)
        return pm_ele

    def add_person_btn(self):
        '''人员管理-新增按钮'''
        pm_ele = self.get_visible_element(self.add_person_loc)
        return pm_ele

    def telephone_input(self):
        '''新增人员-手机号码输入框'''
        pm_ele = self.get_visible_element(self.telephone_input_loc)
        return pm_ele

    def name_input(self):
        '''新增人员-姓名输入框'''
        pm_ele = self.get_visible_element(self.name_input_loc)
        return pm_ele

    def responsible_for_store_btn(self):
        '''新增人员-负责店铺'''
        pm_ele = self.get_visible_element(self.responsible_for_store_loc)
        return pm_ele

    def search_store_input(self):
        '''新增人员-负责店铺-搜索框'''
        pm_ele = self.get_visible_element(self.search_store_input_loc)
        return pm_ele

    def search_store_name(self):
        '''新增人员-负责店铺-搜索店铺结果'''
        pm_ele = self.get_visible_element(self.search_store_name_loc)
        return pm_ele

    def search_sure_btn(self):
        '''新增人员-负责店铺-搜索店铺结果-确定按钮'''
        pm_ele = self.get_visible_element(self.search_sure_loc)
        return pm_ele

    def competence_btn(self):
        '''新增人员-权限'''
        pm_ele = self.get_visible_element(self.competence_loc)
        return pm_ele

    def home_tick_btn(self):
        '''权限-首页勾选框'''
        pm_ele = self.get_visible_element(self.home_tick_loc)
        return pm_ele

    def report_form_tick_btn(self):
        '''权限-报表勾选框'''
        pm_ele = self.get_visible_element(self.report_form_tick_loc)
        return pm_ele

    def store_manage_tick_btn(self):
        '''权限-店铺管理勾选框'''
        pm_ele = self.get_visible_element(self.store_manage_tick_loc)
        return pm_ele

    def device_manage_tick_btn(self):
        '''权限-设备管理勾选框'''
        pm_ele = self.get_visible_element(self.device_manage_tick_loc)
        return pm_ele

    def competence_sure_btn(self):
        '''权限-确定按钮'''
        pm_ele = self.get_visible_element(self.competence_sure_loc)
        return pm_ele

    def submit_btn(self):
        '''新增人员-提交按钮'''
        pm_ele = self.get_visible_element(self.submit_loc)
        return pm_ele

    def person_manage_name_btn(self):
        '''人员管理-姓名为zdhcs的选项'''
        pm_ele = self.get_visible_element(self.person_manage_name_loc)
        return pm_ele

    def edit_btn(self):
        '''人员详情-编辑按钮'''
        pm_ele = self.get_visible_element(self.edit_loc)
        return pm_ele

    def delete_btn(self):
        '''人员详情-删除按钮'''
        pm_ele = self.get_visible_element(self.delete_loc)
        return pm_ele

    def delete_sure_btn(self):
        '''删除-二次确认按钮'''
        pm_ele = self.get_visible_element(self.delete_sure_loc)
        return pm_ele
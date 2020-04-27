#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/26
# @Author  : lfr

import time
from appium.webdriver import WebElement
from b_page.tab import Tab
from appium.webdriver.common.mobileby import MobileBy as By

class ReportFormPage(Tab):
    '''
    报表页
    '''
    # 导出
    report_export_loc = (By.ID, 'com.qekj.merchant:id/tv_export')
    report_email_loc = (By.ID, 'com.qekj.merchant:id/et_export_email')
    report_email_sure = (By.ID, 'com.qekj.merchant:id/ll_sure')

    # 筛选
    r_screen_loc = (By.ID, 'com.qekj.merchant:id/tv_screening')
    r_equipment_loc = (By.XPATH, '//android.widget.TextView[@text="设备"]')
    r_vip_loc = (By.XPATH, '//android.widget.TextView[@text="VIP"]')
    r_all_store_loc = (By.XPATH, '//android.widget.TextView[@text="全部店铺"]')
    r_store_loc = (By.XPATH, '//android.widget.TextView[@text="洗衣液投放器店"]')
    r_sure_loc = (By.XPATH, '//android.widget.TextView[@text="确定"]')
    r_reset_loc = (By.XPATH, '//android.widget.TextView[@text="重置"]')
    r_all_type_loc = (By.XPATH, '//android.widget.TextView[@text="全部类型"]')
    r_water_fountain_loc = (By.XPATH, '//android.widget.TextView[@text="饮水机"]')
    r_washing_machine_loc = (By.XPATH, '//android.widget.TextView[@text="洗衣机"]')
    r_hair_drier_loc = (By.XPATH, '//android.widget.TextView[@text="吹风机"]')
    screen_result_0 = (By.ID, 'com.qekj.merchant:id/iv_click')
    store_text = "洗衣液投放器店"
    export_success_toast = "发送成功"

    # 订单
    report_type_loc = (By.ID, 'com.qekj.merchant:id/tv_change_type')
    type_order_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_order" and @text="订单"]')
    order_store_loc = (By.XPATH, '//android.widget.TextView[@text="自动化测试专用店铺"]')
    order_result_0 = (By.ID, 'com.qekj.merchant:id/iv_click')
    title_text = "订单管理"
    order_store_text = "自动化测试专用店铺"


    def report_export_opera(self, email):
        '''报表-导出操作'''
        self.report_export_btn().click()
        self.report_email_input().send_keys(email)
        self.email_sure_btn().click()

    def report_screen_opera(self):
        '''报表-流水-筛选操作：设备-洗衣液投放器店'''
        self.screen_btn().click()
        self.equipment_btn().click()
        self.store_btn().click()
        self.screen_sure_btn().click()
        # 筛选完成后点击第一条筛选结果进入详情
        self.screen_result_btn().click()
        time.sleep(1)

    def report_order_opera(self):
        '''报表-订单-选择店铺操作'''
        self.type_btn().click()
        self.type_order_btn().click()
        self.order_store_btn().click()
        # 筛选完成后点击第一条筛选结果进入详情
        self.order_result().click()
        time.sleep(1)

    def report_export_btn(self):
        '''报表-导出按钮'''
        re_ele = self.get_visible_element(self.report_export_loc)
        return re_ele

    def report_email_input(self):
        '''email输入框'''
        re_ele = self.get_visible_element(self.report_email_loc)
        return re_ele

    def email_sure_btn(self):
        '''email确定按钮'''
        re_ele = self.get_visible_element(self.report_email_sure)
        return re_ele

    def screen_btn(self):
        '''筛选按钮'''
        re_ele = self.get_visible_element(self.r_screen_loc)
        return re_ele

    def equipment_btn(self):
        '''筛选-设备选项'''
        re_ele = self.get_visible_element(self.r_equipment_loc)
        return re_ele

    def vip_btn(self):
        '''筛选-VIP选项'''
        re_ele = self.get_visible_element(self.r_vip_loc)
        return re_ele

    def all_store_btn(self):
        '''筛选-所有店铺选项'''
        re_ele = self.get_visible_element(self.r_all_store_loc)
        return re_ele

    def store_btn(self):
        '''筛选-店铺选项'''
        re_ele = self.get_visible_element(self.r_store_loc)
        return re_ele

    def all_type_btn(self):
        '''筛选-所有类型'''
        re_ele = self.get_visible_element(self.r_all_type_loc)
        return re_ele

    def water_fountain_btn(self):
        '''筛选-饮水机'''
        re_ele = self.get_visible_element(self.r_water_fountain_loc)
        return re_ele

    def washing_machine_btn(self):
        '''筛选-洗衣机'''
        re_ele = self.get_visible_element(self.r_washing_machine_loc)
        return re_ele

    def hair_drier_btn(self):
        '''筛选-吹风机'''
        re_ele = self.get_visible_element(self.r_hair_drier_loc)
        return re_ele

    def screen_sure_btn(self):
        '''筛选-确定按钮'''
        re_ele = self.get_visible_element(self.r_sure_loc)
        return re_ele

    def screen_result_btn(self):
        '''筛选结果第一条'''
        re_ele = self.get_visible_element(self.screen_result_0)
        return re_ele

    def type_btn(self):
        '''报表-类型按钮：流水、订单'''
        re_ele = self.get_visible_element(self.report_type_loc)
        return re_ele

    def type_order_btn(self):
        '''类型-订单按钮'''
        re_ele = self.get_visible_element(self.type_order_loc)
        return re_ele

    def order_store_btn(self):
        '''订单-店铺选择：自动化测试专用店铺'''
        re_ele = self.get_visible_element(self.order_store_loc)
        return re_ele

    def order_result(self):
        '''订单-选择店铺后第一条记录'''
        re_ele = self.get_visible_element(self.order_result_0)
        return re_ele
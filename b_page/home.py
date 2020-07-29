#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/26
# @Author  : lfr

import time
from appium.webdriver import WebElement
from b_page.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class HomePage(BasePage):
    '''
    首页
    '''
    today_revenue_loc = (By.ID, 'com.qekj.merchant:id/tv_today_revenue')
    total_revenue_loc = (By.ID, 'com.qekj.merchant:id/tv_total_revenue')
    month_revenue_loc = (By.ID, 'com.qekj.merchant:id/tv_month_revenue')

    # 全部应用
    all_applications_loc = (By.XPATH, '//android.widget.TextView[@text="全部应用"]')

    # 今日收益


    # 当月收益
    export_loc = (By.ID, 'com.qekj.merchant:id/ll_export')
    email_loc = (By.ID, 'com.qekj.merchant:id/et_export_email')
    email_sure = (By.ID, 'com.qekj.merchant:id/ll_sure')
    export_success_toast = "发送成功"

    # 总收益
    bg_0_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/rl_bg" and @index=0]')

    def enter_to_today_revenue(self):
        '''点击进入今日收益页面'''
        self.today_revenue().click()
        time.sleep(1)

    def export_opera(self, email):
        '''导出操作'''
        # 点击-填写-确定
        self.export_btn().click()
        time.sleep(1)
        self.email_input().send_keys(email)
        self.email_sure_btn().click()

    def enter_to_total_revenue(self):
        '''点击进入总收益页面'''
        self.total_revenue().click()
        time.sleep(1)

    def enter_to_month_revenue(self):
        '''点击进入当月收益页面'''
        self.month_revenue().click()
        time.sleep(1)

    def total_to_month(self):
        '''总收益页面点击第一条收益记录，进入当月收益'''
        self.total_bg_0().click()
        time.sleep(1)

    def enter_to_all_applications(self):
        '''进入全部应用页面'''
        time.sleep(1)
        self.all_applications_btn().click()
        time.sleep(1)



    def today_revenue(self):
        '''今日收益按钮'''
        home_ele = self.get_visible_element(self.today_revenue_loc)
        return home_ele

    def total_revenue(self):
        '''总收益按钮'''
        home_ele = self.get_visible_element(self.total_revenue_loc)
        return home_ele

    def total_bg_0(self):
        '''总收益页面第一条收益记录'''
        home_ele = self.get_visible_element(self.bg_0_loc)
        return home_ele

    def month_revenue(self):
        '''当月收益按钮'''
        home_ele = self.get_visible_element(self.month_revenue_loc)
        return home_ele

    def export_btn(self):
        '''导出按钮'''
        home_ele = self.get_visible_element(self.export_loc)
        return home_ele

    def email_input(self):
        '''email输入框'''
        home_ele = self.get_visible_element(self.email_loc)
        return home_ele

    def email_sure_btn(self):
        '''邮箱弹窗-确定按钮'''
        home_ele = self.get_visible_element(self.email_sure)
        return home_ele

    def all_applications_btn(self):
        '''首页-全部应用'''
        home_ele = self.get_visible_element(self.all_applications_loc)
        return home_ele
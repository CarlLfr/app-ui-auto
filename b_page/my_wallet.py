#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/24
# @Author  : lfr

import time
from appium.webdriver import WebElement
from b_page.my import MyPage
from appium.webdriver.common.mobileby import MobileBy as By

class MyWallet(MyPage):
    '''
    我的-钱包
    '''
    income_out_detail_loc = (By.ID, 'com.qekj.merchant:id/tv_right_toolbar')
    screen_loc = (By.ID, 'com.qekj.merchant:id/tv_screening')
    # 筛选条件页
    screen_income_loc = (By.XPATH, '//*[@text="收入"]')
    screen_out_loc = (By.XPATH, '//*[@text="支出"]')
    screen_order_loc = (By.XPATH, '//*[@text="订单"]')
    screen_fenzhang_loc = (By.XPATH, '//*[@text="分账"]')
    screen_shop_loc = (By.XPATH, '//*[@text="洗衣液投放器店"]')
    screen_reset_loc = (By.ID, 'com.qekj.merchant:id/ll_reset')
    screen_sure_loc = (By.ID, 'com.qekj.merchant:id/ll_sure')
    # 筛选结果
    screen_result_loc = (By.XPATH, '//android.widget.RelativeLayout[@index=1]')
    order_detail_name = "退款订单"
    order_detail_store = "洗衣液投放器店"

    # 提现记录
    withdraw_record_loc = (By.ID, 'com.qekj.merchant:id/tv_withdraw_record')
    record_null_text = "暂无数据"
    withdraw_record_result = (By.XPATH, '//android.widget.RelativeLayout[@index=0]')
    record_detail_text = "发起提现申请"

    def screen_opera(self):
        '''进入筛选页面进行筛选操作：支出+订单+洗衣液投放器店'''
        self.income_out_detail_btn().click()
        self.screen_btn().click()
        self.screen_out_btn().click()
        self.screen_order_btn().click()
        self.screen_shop_btn().click()
        self.screen_sure_btn().click()
        time.sleep(1)

    def screen_reset_opera(self):
        '''筛选重置操作'''
        self.screen_btn().click()
        self.screen_reset_btn().click()
        time.sleep(1)

    def enter_to_result_detail(self):
        '''点击进入第一条筛选结果详情页'''
        self.screen_result_btn().click()
        time.sleep(1)

    def enter_to_withdraw_record(self):
        '''点击进入提现记录页，点击提现记录页第一条记录，进入记录详情'''
        self.withdraw_record_btn().click()
        self.withdraw_record_result_btn().click()
        time.sleep(1)

    def income_out_detail_btn(self):
        '''钱包页-收支明细按钮'''
        mw_ele = self.get_visible_element(self.income_out_detail_loc)
        return mw_ele

    def screen_btn(self):
        '''收支明细页-筛选按钮'''
        mw = self.get_visible_element(self.screen_loc)
        return mw

    def screen_income_btn(self):
        '''收支明细-筛选条件-收入按钮'''
        mw_ele = self.get_visible_element(self.screen_income_loc)
        return mw_ele

    def screen_out_btn(self):
        '''收支明细-筛选条件-支出按钮'''
        mw_ele = self.get_visible_element(self.screen_out_loc)
        return mw_ele

    def screen_order_btn(self):
        '''收支明细-筛选条件-订单按钮'''
        mw_ele = self.get_visible_element(self.screen_order_loc)
        return mw_ele

    def screen_fenzhang_btn(self):
        '''收支明细-筛选条件-分账按钮'''
        mw_ele = self.get_visible_element(self.screen_fenzhang_loc)
        return mw_ele

    def screen_shop_btn(self):
        '''收支明细-筛选条件-选择店铺（洗衣液投放器店）'''
        mw_ele = self.get_visible_element(self.screen_shop_loc)
        return mw_ele

    def screen_reset_btn(self):
        '''收支明细-筛选条件-重置按钮'''
        mw_ele = self.get_visible_element(self.screen_reset_loc)
        return mw_ele

    def screen_sure_btn(self):
        '''收支明细-筛选条件-确定按钮'''
        mw_ele = self.get_visible_element(self.screen_sure_loc)
        return mw_ele

    def screen_result_btn(self):
        '''筛选结果第一条'''
        mw_ele = self.get_visible_element(self.screen_result_loc)
        return mw_ele

    def withdraw_record_btn(self):
        '''我的钱包-提现记录按钮'''
        mw_ele = self.get_visible_element(self.withdraw_record_loc)
        return mw_ele

    def withdraw_record_result_btn(self):
        '''体现记录页-第一条记录'''
        mw_ele = self.get_visible_element(self.withdraw_record_result)
        return mw_ele
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/21
# @Author  : lfr

import time
from appium.webdriver import WebElement
from b_page.tab import Tab
from appium.webdriver.common.mobileby import MobileBy as By

class MySet(Tab):
    '''
    我的-设置
    '''
    set_loc = (By.ID, 'com.qekj.merchant:id/rl_set')
    personal_info_loc = (By.ID, 'com.qekj.merchant:id/rl_person')
    account_set_loc = (By.ID, 'com.qekj.merchant:id/rl_account')
    brand_info_loc = (By.ID, 'com.qekj.merchant:id/rl_brand')
    zhifutong_loc = (By.ID, 'com.qekj.merchant:id/rl_zhifutong')
    logout_loc = (By.ID, 'com.qekj.merchant:id/ll_out')
    logout_sure_loc = (By.ID, 'android:id/button1')

    update_pwd_loc = (By.ID, 'com.qekj.merchant:id/rl_update_password')
    old_pwd_loc = (By.ID, 'com.qekj.merchant:id/et_used_password')
    new_pwd_loc = (By.ID, 'com.qekj.merchant:id/et_new_password')
    new_pwd_again_loc = (By.ID, 'com.qekj.merchant:id/et_new_password_again')
    sure_pwd_loc = (By.ID, 'com.qekj.merchant:id/ll_sure')

    def enter_to_set(self):
        '''进入设置页操作'''
        self.set_btn().click()
        time.sleep(0.5)

    def change_pwd(self, old_pwd, new_pwd):
        '''修改密码操作'''
        self.account_set().click()
        time.sleep(0.5)
        # 进入修改密码页
        self.update_pwd().click()
        self.old_pwd().send_keys(old_pwd)
        self.new_pwd().send_keys(new_pwd)
        self.new_pwd_again().send_keys(new_pwd)
        time.sleep(0.5)
        self.sure_pwd().click()

    def logout_opera(self):
        '''退出登录操作'''
        self.logout_btn().click()
        self.logout_sure().click()

    def set_btn(self)->WebElement:
        '''我的-设置按钮'''
        set_ele = self.get_visible_element(self.set_loc)
        return set_ele

    def personal_info(self):
        '''设置-个人信息'''
        set_ele = self.get_visible_element(self.personal_info_loc)
        return set_ele

    def account_set(self):
        '''设置-账户设置'''
        set_ele = self.get_visible_element(self.account_set_loc)
        return set_ele

    def update_pwd(self):
        '''设置-账户设置-修改密码'''
        set_ele = self.get_visible_element(self.update_pwd_loc)
        return set_ele

    def old_pwd(self):
        '''设置-账户设置-修改密码-旧密码输入框'''
        set_ele = self.get_visible_element(self.old_pwd_loc)
        return set_ele

    def new_pwd(self):
        '''设置-账户设置-修改密码-新密码输入框'''
        set_ele = self.get_visible_element(self.new_pwd_loc)
        return set_ele

    def new_pwd_again(self):
        '''设置-账户设置-修改密码-确认新密码输入框'''
        set_ele = self.get_visible_element(self.new_pwd_again_loc)
        return set_ele

    def sure_pwd(self):
        '''设置-账户设置-修改密码-确认按钮'''
        set_ele = self.get_visible_element(self.sure_pwd_loc)
        return set_ele

    def brand_info(self):
        '''设置-商户品牌信息'''
        set_ele = self.get_visible_element(self.brand_info_loc)
        return set_ele

    def zhifutong(self):
        '''设置-直付通'''
        set_ele = self.get_visible_element(self.zhifutong_loc)
        return set_ele

    def logout_btn(self):
        '''设置-退出登录'''
        set_ele = self.get_visible_element(self.logout_loc)
        return set_ele

    def logout_sure(self):
        '''设置-退出登录-确定按钮'''
        set_ele = self.get_visible_element(self.logout_sure_loc)
        return set_ele
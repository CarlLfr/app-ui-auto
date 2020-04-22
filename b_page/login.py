# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 11:11
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : login.py
# @Software: PyCharm

from b_page.basepage import BasePage
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
import time
from common.base_driver import BaseDriver

class LoginPage(BasePage):
    '''登录页面封装'''
    mobile_loc = (By.ID,'com.qekj.merchant:id/et_account')
    pwd_loc = (By.ID,'com.qekj.merchant:id/et_password')
    login_loc = (By.ID,'com.qekj.merchant:id/rl_login')
    reset_pwd_loc = (By.ID,'com.qekj.merchant:id/tv_found_password')
    back_loc = (By.ID,'com.qekj.merchant:id/ll_back')
    phone_loc = (By.ID, 'com.qekj.merchant:id/tv_phone')

    def login_opera(self, mobile, pwd):
        '''商家端登录方法'''
        self.moblie_send(mobile)
        self.pwd_send(pwd)
        self.login_btn().click()
        time.sleep(2)

    def login_opera_again(self, mobile, pwd):
        '''未清除缓存，输入上次登录过的账号进行登录'''
        self.moblie_send(mobile)
        # 点击页面弹窗账号
        self.phone_btn().click()
        self.pwd_send(pwd)
        self.login_btn().click()
        time.sleep(2)


    def mobile(self)->WebElement:
        '''账号输入框'''
        user_ele = self.get_visible_element(self.mobile_loc)
        return user_ele

    def moblie_send(self,mobile):
        '''传入账号'''
        self.mobile().clear()
        return self.mobile().send_keys(mobile)

    def pwd(self)->WebElement:
        '''密码输入框'''
        user_ele = self.get_visible_element(self.pwd_loc)
        return user_ele

    def pwd_send(self,pwd):
        '''传入密码'''
        self.pwd().clear()
        return self.pwd().send_keys(pwd)

    def login_btn(self)->WebElement:
        '''登录按钮'''
        user_ele = self.get_visible_element(self.login_loc)
        return user_ele

    def reset_pwd(self)->WebElement:
        '''找回/重置 密码'''
        user_ele = self.get_visible_element(self.reset_pwd_loc)
        return user_ele

    def back_btn(self)->WebElement:
        '''返回按钮'''
        user_ele = self.get_clickable_element(self.back_loc)
        return user_ele

    def phone_btn(self)->WebElement:
        '''账户输入框，相同账号确定'''
        user_ele = self.get_visible_element(self.phone_loc)
        return user_ele

if __name__ == '__main__':
    # driver = BaseDriver().android_driver()
    # LoginPage(driver).login_opera('18768124236', '123456')
    pass
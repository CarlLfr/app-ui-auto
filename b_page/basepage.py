# -*- coding: utf-8 -*-
# @Time    : 2019/11/18 11:52
# @Author  : Stephen
# @Email   : jacstephen@163.com
# @File    : basepage.py
# @Software: PyCharm

from appium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
from common.base_log import log
from common.base_screenshots import Screenshots
from config.keys import Keycode
from common.base_driver import BaseDriver
from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_visible_element(self, locator, timeout=20):
        '''获取可视元素'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except Exception as e:
            Screenshots(self.driver, "获取可视元素失败")
            log.error("获取可视元素失败：{}".format(e))

    def get_presence_element(self, locator, timeout=20):
        '''获取存在元素'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(locator)
            )
        except Exception as e:
            Screenshots(self.driver, "获取存在元素失败")
            log.error("获取存在元素失败：{}".format(e))

    def get_clickable_element(self, locator, timeout=20):
        '''获取可点击元素'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
        except Exception as e:
            Screenshots(self.driver, "获取可点击元素失败")
            log.error("可点击元素获取失败：{}".format(e))

    def get_text_element(self, text_loc, timeout=20):
        '''通过text定位元素'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda driver: self.driver.find_element(*text_loc)
            )
        except Exception as e:
            Screenshots(self.driver, "通过text获取元素失败")
            log.error("通过text获取元素失败：{}".format(e))

    def is_toast_exist(self, text, timeout=20, poll_frequency=0.1):
        '''
        判断toast是否存在，是则返回True，否则返回False
        :param text: toast文本
        :param timeout: 元素定位超时时间
        :param poll_frequency: 查询频率
        :return: True or False
        '''
        try:
            toast_loc = (By.XPATH, ".//*[contains(@text, %s)]" % text)
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                ec.presence_of_element_located(toast_loc)
            )
            return True
        except:
            return False

    @property
    def width(self):
        '''获取屏幕宽度'''
        return self.driver.get_window_size().get('width', 0)

    @property
    def height(self):
        '''获取屏幕高度'''
        return self.driver.get_window_size().get('height', 0)

    def swipe_to_left(self, offset=0.1):
        '''从右向左滑动'''
        action  = self.driver.swipe(self.width*(1-offset),
                                    self.height*0.5,
                                    self.width*offset,
                                    self.height*0.5
                                    )
        return action

    def swipe_to_right(self, offset=0.1):
        '''从左向右滑动'''
        action  = self.driver.swipe(self.width*offset,
                                    self.height*0.5,
                                    self.width*(1-offset),
                                    self.height*0.5
                                    )
        return action

    def swipe_to_top(self, offset=0.9):
        '''从下向上滑动'''
        action  = self.driver.swipe(self.width*0.5,
                                    self.height*offset,
                                    self.width*0.5,
                                    self.height*(1-offset)
                                    )
        return action

    def swipe_to_bottom(self, offset=0.9):
        '''从上向下滑动'''
        action  = self.driver.swipe(self.width*0.5,
                                    self.height*(1-offset),
                                    self.width*0.5,
                                    self.height*offset
                                    )
        return action

    def click(self, locator):
        '''点击元素'''
        action = WebDriverWait(self.driver, 15, poll_frequency=0.1).until(
            ec.element_to_be_clickable(locator)
        )
        return action.click()

    def press_key_power(self):
        '''模拟按下电源键'''
        action = self.driver.press_keycode(Keycode.POWER)
        return action

    def press_key_home(self):
        '''模拟按下home键'''
        action = self.driver.press_keycode(Keycode.HOME)
        return action

    def press_key_back(self):
        '''模拟按下返回键'''
        action = self.driver.press_keycode(Keycode.BACK)
        return action

    def  is_exist_element(self, ele_attr):
        '''
        判断元素是否存在
        ele_attr: 元素的属性值
        '''
        sleep(2)
        source = self.driver.page_source
        if ele_attr in source:
            return True
        else:
            return False

if __name__ == '__main__':
    # driver = BaseDriver().android_driver()
    # sleep(5)
    # bap = BasePage(driver)
    # for i in range(2):
    #     bap.swipe_to_left()
    #     sleep(1)
    pass
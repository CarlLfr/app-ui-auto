#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/13
# @Author  : lfr

import os
import time
import yaml
from appium import webdriver
from config.path_config import DESIRED_CAPS_YAML_PATH
from common.base_log import log

class BaseDriver:
    '''
    构造driver
    '''
    def android_driver(self):
        '''Android driver'''

        # 从desired_caps.yaml读取driver配置数据
        stream = open(DESIRED_CAPS_YAML_PATH, 'r')
        data = yaml.load(stream, Loader=yaml.FullLoader)

        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['udid'] = data['udid']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['noReset'] = data['noReset']
        desired_caps['unicodeKeyBoard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['automationName'] = data['automationName']

        # 设置收到下一条命令的超时时间,超时appium会自动关闭session ,默认60秒
        desired_caps['newCommondTimeout'] = data['newCommondTimeout']

        try:
            driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
            driver.implicitly_wait(8)
            log.info("驱动app打开成功...")
            return driver
        except Exception as e:
            error_str = "Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接"
            if error_str in str(e):
                log.error("Appium服务未开启！！！")
            else:
                log.error("驱动app打开失败：{}".format(e))
            os._exit(0)

    def ios_driver(self):
        pass

if __name__ == '__main__':
    baseDriver = BaseDriver()
    driver = baseDriver.android_driver()
    time.sleep(10)
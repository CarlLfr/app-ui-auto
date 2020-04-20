#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/15
# @Author  : lfr

import os
import time
from ruamel import yaml
from common.base_log import log
from config.path_config import DESIRED_CAPS_YAML_PATH

class IsInstallApp:
    '''
    判断是否已经安装App，安装App，卸载App
    '''
    def __init__(self):
        self.appPath, self.appName, self.appPackage = self.get_app_info()
        self.install_command = 'adb install ' + self.appPath
        self.uninstall_command = 'adb uninstall ' + self.appPackage
        self.list_package_command = 'adb shell pm list package'

    def get_app_info(self):
        '''从desired_caps文件中读取app信息'''
        with open(DESIRED_CAPS_YAML_PATH, 'r') as f:
            content = yaml.load(f.read(), Loader=yaml.RoundTripLoader)
            appPath = content['app']
            appName = appPath.split('/')[-1]
            appPackage = content['appPackage']
        return appPath, appName, appPackage

    def is_install_app(self):
        '''判断设备是否已经安装应用，否则安装'''
        log.info("检查{}应用是否已安装...".format(self.appName))
        result = os.popen(self.list_package_command).read()
        if self.appPackage in result:
            log.info("---应用已安装---")
        else:
            log.info("应用未安装！！！")
            self.install_app()

    def install_app(self):
        '''安装App基本方法'''
        try:
            log.info("正在安装应用{}，请稍后...".format(self.appName))
            result = os.popen(self.install_command).read()
            if "Success" in result:
                log.info("---{}应用安装成功---")
        except Exception as e:
            log.error("应用安装失败：{}".format(e))

    def uninstall_app(self):
        '''卸载App基本方法'''
        try:
            log.info("开始卸载应用{}...".format(self.appName))
            result = os.popen(self.uninstall_command).read()
            if "Success" in result:
                log.info("---应用卸载成功---")
        except Exception as e:
            log.error("应用卸载失败：{}".format(e))

if __name__ == '__main__':
    i = IsInstallApp()
    i.is_install_app()
    # i.uninstall_app()
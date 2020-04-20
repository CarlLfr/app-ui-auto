#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/13
# @Author  : lfr

import os
import sys
from common.base_log import log

class BaseAdb:
    '''
    通过adb命令获取设备udid，系统版本号(platformVersion)，设备名(deviceName)
    '''
    def __init__(self):
        self.udid_command = 'adb devices'
        self.platformVersion_command = 'adb shell getprop ro.build.version.release'
        self.deviceName_command = 'adb shell getprop ro.product.model'

    def get_udid(self):
        '''获取设备udid。输出所有已连接电脑的android devices，去掉输出中无用的字符串，只保留devices SN'''
        devices_list = []
        result = os.popen(self.udid_command).readlines()
        # print(result)
        list_len = len(result)
        if list_len == 2:
            log.error("没有测试设备连接，结束！！！")
            sys.exit(0)
        else:
            for i in range(list_len):
                if result[i].find('\t') != -1:
                    devices_list.append(result[i].split('\t')[0])
        # print(devices_list)
        # 返回第一个udid(通常只有一台设备进行测试)
        return devices_list[0]

    def get_platformVersion(self):
        '''获取连接设备的系统版本号platformVersion'''
        try:
            result = os.popen(self.platformVersion_command).read()
            platformVersion = result.split('\n')[0]
            # print(platformVersion)
            log.info("---获取设备系统版本号成功---")
            return platformVersion
        except Exception as e:
            log.error("获取系统版本号失败：{}".format(e))

    def get_deviceName(self):
        '''获取连接设备的设备名deviceName'''
        try:
            result = os.popen(self.deviceName_command).read()
            deviceName = result.split('\n')[0]
            # print(deviceName)
            log.info("---获取设备名成功---")
            return deviceName
        except Exception as e:
            log.error("获取设备名失败：{}".format(e))

if __name__ == '__main__':
    baseAdb = BaseAdb()
    baseAdb.get_deviceName()
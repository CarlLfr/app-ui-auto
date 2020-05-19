#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/13
# @Author  : lfr

import os
import re
import sys
import subprocess
from config.path_config import APP_PATH
from common.base_log import log

class BaseApkInfo:
    '''
    获取被测apk文件信息appPackage，appActivity
    '''

    def get_apk_path(self):
        '''获取app文件的完整路径'''

        # 获取app文件夹中的所有apk文件名
        package_list = os.listdir(APP_PATH)

        # 判断app中apk文件的个数并选择
        num = len(package_list)
        if num == 0:
            log.error("未添加需要测试的apk文件！！！")
            sys.exit(0)
        elif num == 1:
            apk_path = APP_PATH + package_list[0]
        elif num >= 2:
            print(package_list)
            index = int(input("请输入要测试的包名的编号（从0开始）："))
            apk_path = APP_PATH + package_list[index]
        # print(apk_path)
        return apk_path

    def get_apk_info(self):
        '''获取apk包的appPackage、启动类appActivity'''
        mac_aapt_path = '/Users/mac/Downloads/android-sdk-macosx/build-tools/29.0.3/'
        aapt_command_base = 'aapt dump badging '
        app_path = self.get_apk_path()

        try:
            # mac获取方法
            # p = subprocess.Popen(mac_aapt_path+aapt_command_base+app_path, stdout=subprocess.PIPE,
            #                              stderr=subprocess.PIPE,
            #                              stdin=subprocess.PIPE,
            #                              shell=True)
            # windows获取方法
            p = subprocess.Popen(aapt_command_base+app_path, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=True)
            (output, err) = p.communicate()
            t = output.decode()
            # print(t)
            match_appPackage = re.compile("package: name='(.*?)'").search(t)
            match_apkActivity = re.compile("launchable-activity: name='(.*?)'").search(t)
            appPackage = match_appPackage.groups()[0]
            appActivity = match_apkActivity.groups()[0]
            # print(appPackage)
            # print(appActivity)
            log.info("获取被测apk包的appPackage、appActivity成功...")
            return appPackage, appActivity
        except Exception as e:
            log.error("获取被测apk包的appPackage、appActivity失败：{}".format(e))

if __name__ == '__main__':
    apkInfo = BaseApkInfo()
    apkInfo.get_apk_info()
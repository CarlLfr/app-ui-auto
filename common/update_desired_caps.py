#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/14
# @Author  : lfr

from ruamel import yaml
from common.base_adb import BaseAdb
from common.base_apkInfo import BaseApkInfo
from config.path_config import DESIRED_CAPS_YAML_PATH
from common.base_log import log

class UpdateDesiredCaps:
    '''
    更新desired_caps中的设备及apk文件信息
    '''
    def __init__(self):
        self.platformVersion = BaseAdb().get_platformVersion()
        self.deviceName = BaseAdb().get_deviceName()
        self.udid = BaseAdb().get_udid()
        self.appPackage, self.appActivity = BaseApkInfo().get_apk_info()
        self.app = BaseApkInfo().get_apk_path()
        self.yamlPath = DESIRED_CAPS_YAML_PATH

    def update_desired_caps(self):
        try:
            # 读取yaml中的内容并修改
            log.info("开始更新desired_caps中的app及手机参数...")
            with open(self.yamlPath, 'r', encoding='utf-8') as f:
                content = yaml.load(f.read(), Loader=yaml.RoundTripLoader)
                content['platformVersion'] = self.platformVersion
                content['deviceName'] = self.deviceName
                content['udid'] = self.udid
                content['appPackage'] = self.appPackage
                content['appActivity'] = self.appActivity
                content['app'] = self.app

            # 将修改的内容重新写入该yaml文件
            with open(self.yamlPath, 'w', encoding='utf-8') as nf:
                yaml.dump(content, nf, Dumper=yaml.RoundTripDumper)
            log.info("desired_caps更新完成...")
        except Exception as e:
            log.info("desired.caps更新失败！！！失败原因为：%s" % e)

if __name__ == '__main__':
    updateYaml = UpdateDesiredCaps()
    updateYaml.update_desired_caps()
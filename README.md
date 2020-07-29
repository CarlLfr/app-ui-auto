# qiekj-app-ui-autotest

appUI测试

## 功能描述

用于企鹅商家版appUI测试

## 环境配置

1，python 3.7.4

2，selenium 3.141.0

3, appium-desktop 1.15.1（appium环境配置）

4，Appium-Python-Client，appium-uiautomator2-driver

5，python第三方模块：pyyaml，ruamel.yaml，HTMLTestRunner，pytest，pytest-html

6，Genymotion Android模拟器

7，mac/windows

## 运行前配置

1，项目第一次运行之前，需将项目config文件夹中add_devices_IMEI.jpg和add_devices_NQT.jpg文件放入测试机或模拟器的相册中（相册中只有这两张图片或这两张图片排在第一二），否则新增设备用例会报错
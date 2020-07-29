#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/07/16
# @Author  : lfr

import time
from b_page.home import HomePage
from appium.webdriver.common.mobileby import MobileBy as By

class BathPositionManagement(HomePage):
    '''
    全部应用-浴位管理
    '''
    # 新增
    bath_position_management_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="浴位管理"]')
    add_loc = (By.ID, 'com.qekj.merchant:id/iv_add')
    add_device_loc = (By.XPATH, '//android.widget.TextView[@text="新增设备"]')
    device_type_loc = (By.XPATH, '//android.widget.TextView[@text="中卡集中淋浴(带键盘带流量计)"]')
    select_loc = (By.ID, 'com.qekj.merchant:id/iv_select')
    next_loc = (By.ID, 'com.qekj.merchant:id/tv_next')
    belong_shop_loc = (By.ID, 'com.qekj.merchant:id/ll_shop')
    belong_bathroom_loc = (By.ID, 'com.qekj.merchant:id/ll_yushi')
    maichong_input_loc = (By.ID, 'com.qekj.merchant:id/et_maichong')
    price_input_loc = (By.ID, 'com.qekj.merchant:id/et_price')
    # price_input_loc = (By.XPATH, '//android.widget.EditText[@text="请输入单价"]')
    confirm_loc = (By.ID, 'com.qekj.merchant:id/btnSubmit')
    add_next_loc = (By.ID, 'com.qekj.merchant:id/tv_next')
    yw_no_input_loc = (By.ID, 'com.qekj.merchant:id/et_yw_no')
    device_no_loc = (By.ID, 'com.qekj.merchant:id/rl_sb_no')
    scan_allow_loc = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    scan_photo_loc = (By.XPATH, '//android.widget.TextView[@text="相册"]')
    select_album_loc = (By.ID, 'com.qekj.merchant:id/selected_album')
    picture_loc = (By.XPATH, '//android.widget.TextView[@text="Pictures"]')
    code_1_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/recyclerview"]/android.widget.FrameLayout[@index=0]')
    scan_check_view_loc = (By.ID, 'com.qekj.merchant:id/check_view')
    scan_photo_sure_loc = (By.ID, 'com.qekj.merchant:id/button_apply')
    submit_loc = (By.ID, 'com.qekj.merchant:id/tv_submit')
    maichong = 1000
    maichong_price = 1
    yw_no = 1278
    add_success_toast = "添加成功"


    # 编辑
    bath_position_name_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_device_name" and @text="1278"]')
    device_detail_point_loc = (By.ID, 'com.qekj.merchant:id/iv_search_single')
    edit_device_btn_loc = (By.XPATH, '//android.widget.TextView[@text="编辑设备"]')
    edit_yw_no_input_loc = (By.ID, 'com.qekj.merchant:id/et_yw_no')
    edit_yw_no = 1268
    bath_position_detail_title = "设备详情"

    # 高级设置
    set_device_btn_loc = (By.XPATH, '//android.widget.TextView[@text="高级设置"]')
    no_flow_timeout_input_loc = (By.XPATH, '//android.widget.TextView[@text="无流量超时时长(秒)"]/../android.widget.EditText[1]')
    warning_times_input_loc = (By.XPATH, '//android.widget.TextView[@text="无流量超时自动报警次数(次)"]/../android.widget.EditText[1]')
    suspend_timeout_input_loc = (By.XPATH, '//android.widget.TextView[@text="暂停超时时长(秒)"]/../android.widget.EditText[1]')
    max_water_input_loc = (By.XPATH, '//android.widget.TextView[@text="最大允许出水量(升)"]/../android.widget.EditText[1]')
    p_input_loc = (By.XPATH, '//android.widget.TextView[@text="P值（脉冲/吨）"]/../android.widget.EditText[1]')
    no_flow_timeout = 3000
    warning_times = 100
    suspend_timeout = 2000
    max_water = 110
    p = 10000
    set_sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    set_success_toast = "设置成功"

    # 删除设备
    delete_device_btn_loc = (By.XPATH, '//android.widget.TextView[@text="删除设备"]')
    delete_sure_again_loc = (By.ID, 'android:id/button1')
    bath_position_title = "浴位管理"



    # 新增
    def enter_to_bath_position_management(self):
        '''进入浴室管理页'''
        self.bath_position_management_btn().click()

    def add_bath_device_opera(self):
        '''新增浴室操作'''
        self.add_btn().click()
        self.add_device_btn().click()
        time.sleep(0.5)
        # 设备型号
        self.device_type().click()
        self.select_btn().click()
        self.next_btn().click()
        # 添加设备
        self.belong_shop_btn().click()
        self.confirm_btn().click()
        self.belong_bathroom_btn().click()
        self.confirm_btn().click()
        self.maichong_input().send_keys(self.maichong)
        self.price_input().send_keys(self.maichong_price)
        self.add_next_btn().click()
        # 浴位、编号
        self.yw_no_input().send_keys(self.yw_no)
        self.device_no_scan().click()
        self.scan_allow_btn().click()
        self.scan_photo_btn().click()
        self.scan_allow_btn().click()
        self.select_album_btn().click()
        self.picture_btn().click()
        self.code_1().click()
        self.scan_check_view_btn().click()
        self.scan_photo_sure_btn().click()
        self.submit_btn().click()


    def bath_position_management_btn(self):
        '''全部应用-浴位管理'''
        bp_ele = self.get_visible_element(self.bath_position_management_loc)
        return bp_ele

    def add_btn(self):
        '''新增'''
        bp_ele = self.get_visible_element(self.add_loc)
        return bp_ele

    def add_device_btn(self):
        '''新增设备按钮'''
        bp_ele = self.get_visible_element(self.add_device_loc)
        return bp_ele

    def device_type(self):
        '''选择设备类型'''
        bp_ele = self.get_visible_element(self.device_type_loc)
        return bp_ele

    def select_btn(self):
        '''勾选'''
        bp_ele = self.get_visible_element(self.select_loc)
        return bp_ele

    def next_btn(self):
        '''下一步按钮'''
        bp_ele = self.get_visible_element(self.next_loc)
        return bp_ele

    def belong_shop_btn(self):
        '''所属店铺'''
        bp_ele = self.get_visible_element(self.belong_shop_loc)
        return bp_ele

    def belong_bathroom_btn(self):
        '''所属浴室'''
        bp_ele = self.get_visible_element(self.belong_bathroom_loc)
        return bp_ele

    def confirm_btn(self):
        '''confirm按钮'''
        bp_ele = self.get_visible_element(self.confirm_loc)
        return bp_ele

    def maichong_input(self):
        '''脉冲流量'''
        bp_ele = self.get_visible_element(self.maichong_input_loc)
        return bp_ele

    def price_input(self):
        '''单价'''
        bp_ele = self.get_visible_element(self.price_input_loc)
        return bp_ele

    def add_next_btn(self):
        '''添加设备-下一步按钮'''
        bp_ele = self.get_visible_element(self.add_next_loc)
        return bp_ele

    def yw_no_input(self):
        '''浴位编号'''
        bp_ele = self.get_visible_element(self.yw_no_input_loc)
        return bp_ele

    def device_no_scan(self):
        '''设备编码'''
        bp_ele = self.get_visible_element(self.device_no_loc)
        return bp_ele

    def scan_allow_btn(self):
        '''相机许可'''
        bp_ele = self.get_visible_element(self.scan_allow_loc)
        return bp_ele

    def scan_photo_btn(self):
        '''相册按钮'''
        bp_ele = self.get_visible_element(self.scan_photo_loc)
        return bp_ele

    def select_album_btn(self):
        '''相册-选择文件夹'''
        bp_ele = self.get_visible_element(self.select_album_loc)
        return bp_ele

    def picture_btn(self):
        '''pictures目录'''
        bp_ele = self.get_visible_element(self.picture_loc)
        return bp_ele

    def code_1(self):
        '''设备二维码'''
        bp_ele = self.get_visible_element(self.code_1_loc)
        return bp_ele

    def scan_check_view_btn(self):
        '''相片勾选'''
        bp_ele = self.get_visible_element(self.scan_check_view_loc)
        return bp_ele

    def scan_photo_sure_btn(self):
        '''相片确定按钮'''
        bp_ele = self.get_visible_element(self.scan_photo_sure_loc)
        return bp_ele

    def submit_btn(self):
        '''提交按钮'''
        bp_ele = self.get_visible_element(self.submit_loc)
        return bp_ele



    # 编辑
    def edit_bath_position_opera(self):
        '''编辑浴位操作'''
        self.bath_position_name().click()
        self.device_detail_point_btn().click()
        self.edit_device_btn().click()
        self.edit_yw_no_input().clear()
        self.edit_yw_no_input().send_keys(self.edit_yw_no)
        self.submit_btn().click()
        time.sleep(1)


    def bath_position_name(self):
        '''浴位管理-新增浴位名'''
        bp_ele = self.get_visible_element(self.bath_position_name_loc)
        return bp_ele

    def device_detail_point_btn(self):
        '''浴位详情-...'''
        bp_ele = self.get_visible_element(self.device_detail_point_loc)
        return bp_ele

    def edit_device_btn(self):
        '''编辑设备按钮'''
        bp_ele = self.get_visible_element(self.edit_device_btn_loc)
        return bp_ele

    def edit_yw_no_input(self):
        '''编辑设备-浴位编号输入框'''
        bp_ele = self.get_visible_element(self.edit_yw_no_input_loc)
        return bp_ele



    # 高级设置
    def set_bath_position_opera(self):
        '''高级设置操作'''
        self.device_detail_point_btn().click()
        self.set_device_btn().click()
        self.no_flow_timeout_input().send_keys(self.no_flow_timeout)
        self.warning_times_input().send_keys(self.warning_times)
        self.suspend_timeout_input().send_keys(self.suspend_timeout)
        self.max_water_input().send_keys(self.max_water)
        self.p_input().send_keys(self.p)
        self.set_sure_btn().click()


    def set_device_btn(self):
        '''设备详情-高级设置'''
        bp_ele = self.get_visible_element(self.set_device_btn_loc)
        return bp_ele

    def no_flow_timeout_input(self):
        '''无流量超时时长(秒)'''
        bp_ele = self.get_visible_element(self.no_flow_timeout_input_loc)
        return bp_ele

    def warning_times_input(self):
        '''无流量超时自动报警次数(次)'''
        bp_ele = self.get_visible_element(self.warning_times_input_loc)
        return bp_ele

    def suspend_timeout_input(self):
        '''暂停超时时长(秒)'''
        bp_ele = self.get_visible_element(self.suspend_timeout_input_loc)
        return bp_ele

    def max_water_input(self):
        '''最大允许出水量(升)'''
        bp_ele = self.get_visible_element(self.max_water_input_loc)
        return bp_ele

    def p_input(self):
        '''P值（脉冲/吨）'''
        bp_ele = self.get_visible_element(self.p_input_loc)
        return bp_ele

    def set_sure_btn(self):
        '''高级设置-确定按钮'''
        bp_ele = self.get_visible_element(self.set_sure_loc)
        return bp_ele



    # 删除
    def delete_bath_position_opera(self):
        '''删除浴位操作'''
        self.device_detail_point_btn().click()
        self.delete_device_btn().click()
        self.delete_sure_again_btn().click()
        time.sleep(2)


    def delete_device_btn(self):
        '''删除设备按钮'''
        bp_ele = self.get_visible_element(self.delete_device_btn_loc)
        return bp_ele

    def delete_sure_again_btn(self):
        '''删除再次确认按钮'''
        bp_ele = self.get_visible_element(self.delete_sure_again_loc)
        return bp_ele
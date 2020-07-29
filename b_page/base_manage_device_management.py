#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/22
# @Author  : lfr

import time
from b_page.home import HomePage
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.common.exceptions import NoSuchElementException

class DeviceManagement(HomePage):
    '''
    管理-基础管理-设备管理
    '''
    devices_management_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="设备管理"]')
    add_loc = (By.ID, 'com.qekj.merchant:id/iv_add')
    add_device_loc = (By.ID, 'com.qekj.merchant:id/ll_add_device')
    batch_start_loc = (By.ID, 'com.qekj.merchant:id/ll_batch_start')
    # 新增
    device_name_input_loc = (By.ID, 'com.qekj.merchant:id/et_device_name')
    # belong_shop_loc = (By.ID, 'com.qekj.merchant:id/rl_store')
    belong_shop_loc = (By.XPATH, '//android.widget.TextView[@text="所属店铺"]')
    belong_shop_confirm = (By.ID, 'com.qekj.merchant:id/btnSubmit')
    device_type_loc = (By.ID, 'com.qekj.merchant:id/rl_device_type')
    device_model_loc = (By.ID, 'com.qekj.merchant:id/rl_device_model')
    often_model_first_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/rv_device_model_often"]/android.widget.RelativeLayout[1]')
    model_more_loc = (By.ID, 'com.qekj.merchant:id/iv_more')
    other_model_first_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/rv_device_model_other"]/android.widget.RelativeLayout[1]')
    device_model_sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    nqt_scan_loc = (By.ID, 'com.qekj.merchant:id/ll_nqt')
    scan_allow_loc = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    scan_photo_loc = (By.XPATH, '//android.widget.TextView[@text="相册"]')
    select_album_loc = (By.ID, 'com.qekj.merchant:id/selected_album')
    download_loc = (By.XPATH, '//android.widget.TextView[@text="Download"]')

    code_2_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/recyclerview"]/android.widget.FrameLayout[@index=1]')
    scan_check_view_loc = (By.ID, 'com.qekj.merchant:id/check_view')
    scan_photo_sure_loc = (By.ID, 'com.qekj.merchant:id/button_apply')
    imei_scan_loc = (By.ID, 'com.qekj.merchant:id/ll_imei')
    code_1_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/recyclerview"]/android.widget.FrameLayout[@index=0]')
    function_set_loc = (By.ID, 'com.qekj.merchant:id/rl_function_set')
    function_set_edit_input_loc = (By.XPATH, '//android.widget.EditText[@text="0"]')
    finish_time_input_loc = (By.XPATH, '//android.widget.LinearLayout[@index=5]/android.widget.LinearLayout[2]/android.widget.EditText')
    finish_price_input_loc = (By.XPATH, '//android.widget.LinearLayout[@index=5]/android.widget.LinearLayout[3]/android.widget.EditText')
    function_set_sure_loc = (By.ID, 'com.qekj.merchant:id/ll_sure')
    device_name = "appUI自动化新增设备"
    function_set_num_0 = '0'
    function_set_num = 1
    add_device_submit_loc = (By.ID, 'com.qekj.merchant:id/rl_submit')
    add_success_toast = "添加成功"
    # 搜索设备
    search_loc = (By.ID, 'com.qekj.merchant:id/iv_search')
    i_know_loc = (By.ID, 'com.qekj.merchant:id/ll_iknow')
    i_know = "我知道了"
    search_name_input_loc = (By.ID, 'com.qekj.merchant:id/et_search_shop')
    search_name_option_loc = (By.XPATH, '//android.widget.TextView[@text="appUI自动化新增设备"]')
    search_result_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_device_name" and @text="appUI自动化新增设备"]')
    device_detail_point_loc = (By.ID, 'com.qekj.merchant:id/iv_search_single')
    # 编辑设备
    edit_device_loc = (By.ID, 'com.qekj.merchant:id/ll_edit_device')
    device_edit_name = "appUI自动化编辑设备"
    edit_success_toast = "编辑成功"
    # 高级设置
    senior_set_loc = (By.ID, 'com.qekj.merchant:id/ll_senior_set')
    search_edit_device_option_loc = (By.XPATH, '//android.widget.TextView[@text="appUI自动化编辑设备"]')
    search_edit_result_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_device_name" and @text="appUI自动化编辑设备"]')
    dehydration_only_time_input_loc = (By.XPATH, '//android.widget.TextView[@text="单脱时长"]/../*[@resource-id="com.qekj.merchant:id/et_centent"]')
    laundry_fast_time_input_loc = (By.XPATH, '//android.widget.TextView[@text="快速洗时长"]/../*[@resource-id="com.qekj.merchant:id/et_centent"]')
    laundry_standard_time_input_loc = (By.XPATH, '//android.widget.TextView[@text="标准洗时长"]/../*[@resource-id="com.qekj.merchant:id/et_centent"]')
    laundry_object_time_input_loc = (By.XPATH, '//android.widget.TextView[@text="大物洗时长"]/../*[@resource-id="com.qekj.merchant:id/et_centent"]')
    laundry_fast_level_loc = (By.XPATH, '//android.widget.TextView[@text="快速洗水位"]/../*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    laundry_standard_level_loc = (By.XPATH, '//android.widget.TextView[@text="标准洗水位"]/../*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    laundry_object_level_loc = (By.XPATH, '//android.widget.TextView[@text="大物洗水位"]/../*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    canister_clear_loc = (By.XPATH, '//android.widget.TextView[@text="设置桶清洁"]/../*[@resource-id="com.qekj.merchant:id/tv_centent"]')
    dehydration_only_time = 15
    laundry_fast_time = 20
    laundry_standard_time = 45
    laundry_object_time = 55
    set_success_toast = "设置成功"
    # 删除设备
    delete_loc = (By.ID, 'com.qekj.merchant:id/ll_del')
    delete_sure_loc = (By.ID, 'android:id/button1')
    delete_success_toast = "机器设备被删除"
    device_manage_title = "设备管理"

    # 批量修改
    batch_update_loc = (By.ID, 'com.qekj.merchant:id/ll_batch_update')
    update_shop_loc = (By.ID, 'com.qekj.merchant:id/ll_shop')
    shop_search_input_loc = (By.ID, 'com.qekj.merchant:id/et_search')
    shop_search_result_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/ll_sn" and @index=0]')
    shop_search_sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    update_device_type_loc = (By.ID, 'com.qekj.merchant:id/ll_device')
    update_model_loc = (By.ID, 'com.qekj.merchant:id/ll_model')
    next_loc = (By.ID, 'com.qekj.merchant:id/tv_next')
    dehydration_only_price_input_loc = (By.XPATH, '//*[@text="单脱"]/../../android.widget.LinearLayout[3]/android.widget.EditText[1]')
    laundry_fast_price_input_loc = (By.XPATH, '//*[@text="快洗"]/../../android.widget.LinearLayout[3]/android.widget.EditText[1]')
    laundry_standard_price_input_loc = (By.XPATH, '//*[@text="标准洗"]/../../android.widget.LinearLayout[3]/android.widget.EditText[1]')
    laundry_object_price_input_loc = (By.XPATH, '//*[@text="大物洗"]/../../android.widget.LinearLayout[3]/android.widget.EditText[1]')
    finished_price_input_loc = (By.XPATH, '//*[@text="结束"]/../../android.widget.LinearLayout[3]/android.widget.EditText[1]')
    canister_clear_input_loc = (By.XPATH, '//*[@text="桶自洁"]/../../android.widget.LinearLayout[3]/android.widget.EditText[1]')
    batch_update_page_submit_loc = (By.ID, 'com.qekj.merchant:id/tv_submit')
    sure_again_loc = (By.ID, 'android:id/button1')
    update_shop_name = "appUl营销管理专用勿操作店铺"
    laundry_standard_price_update_0 = 5
    laundry_standard_price_update_1 = 6
    batch_update_success_toast = "批量编辑成功"

    # 批量启动
    batch_start_search_input_loc = (By.ID, 'com.qekj.merchant:id/et_search_device')
    batch_start_search_result_loc = (By.XPATH, '//android.widget.TextView[@text="appUl营销管理专用勿操作店铺"]')
    batch_start_device_type_loc =(By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_device_name" and @text="洗衣机"]')
    device_function_finish_loc = (By.XPATH, '//android.widget.TextView[@text="结束"]')
    start_now_loc = (By.XPATH, '//android.widget.TextView[@text="立即启动"]')
    batch_start_success_toast = "操作成功"



    def enter_to_devices_management(self):
        '''管理页点击进入设备管理'''
        self.devices_management_btn().click()

    def add_device_opera(self):
        '''新增设备操作'''
        self.add_btn().click()
        self.add_device_btn().click()
        self.device_name_input().send_keys(self.device_name)
        time.sleep(1)
        self.belong_shop_btn().click()
        self.confirm_btn().click()
        self.device_type_btn().click()
        self.confirm_btn().click()
        # 选择设备型号，如果常用栏下面没有，则点击其他栏选择第一项
        self.device_model_btn().click()
        self.often_model_first_btn().click()
        # self.model_more_btn().click()
        # self.other_model_first_btn().click()
        self.device_model_sure_btn().click()
        # NQT，存放在手机相册里（测试手机相册里只能有NQT二维码与IMEI二维码，且NQT为第一张，否则脚本执行报错）
        self.nqt_scan_btn().click()
        time.sleep(1)
        self.scan_allow_btn().click()
        time.sleep(1)
        self.scan_photo_btn().click()
        time.sleep(1)
        self.scan_allow_btn().click()
        time.sleep(1)
        self.album_btn().click()
        self.download_btn().click()
        self.code_1().click()
        self.scan_check_view_btn().click()
        self.scan_photo_sure_btn().click()
        time.sleep(2)
        # 判断如果选错二维码择选择另一张
        r = self.is_exist_element("新增设备")
        if r:
            pass
        else:
            self.scan_photo_btn().click()
            time.sleep(1)
            self.album_btn().click()
            self.download_btn().click()
            self.code_2().click()
            self.scan_check_view_btn().click()
            self.scan_photo_sure_btn().click()
        # IMEI
        self.imei_scan_btn().click()
        time.sleep(1)
        self.scan_photo_btn().click()
        time.sleep(1)
        self.album_btn().click()
        self.download_btn().click()
        self.code_2().click()
        self.scan_check_view_btn().click()
        self.scan_photo_sure_btn().click()
        # 判断如果选错二维码择选择另一张
        r = self.is_exist_element("新增设备")
        if r:
            pass
        else:
            self.scan_photo_btn().click()
            time.sleep(1)
            self.album_btn().click()
            self.download_btn().click()
            self.code_1().click()
            self.scan_check_view_btn().click()
            self.scan_photo_sure_btn().click()

        # 功能设置，结束栏时间、原价都填写为1
        self.function_set_btn().click()
        self.finish_time_input().clear()
        time.sleep(0.5)
        self.finish_time_input().send_keys(self.function_set_num)
        self.finish_price_input().clear()
        time.sleep(0.5)
        self.finish_price_input().send_keys(self.function_set_num)
        # 判断是否有为0的选项，有则填充1
        # result = self.is_exist_element(self.function_set_num_0)
        # while True:
        #     if result:
        #         self.function_set_edit_input().clear()
        #         time.sleep(0.5)
        #         self.function_set_edit_input().send_keys(self.function_set_num)
        #     else:
        #         break
        self.function_set_sure_btn().click()
        self.add_device_submit_btn().click()


    def search_edit_device_opera(self):
        '''设备管理-搜索设备、编辑设备操作'''
        # 搜索
        self.search_btn().click()
        # 判断是否有【我知道了】按钮，有则点击
        result = self.is_exist_element(self.i_know)
        if result:
            self.i_know_btn().click()
        else:
            pass
        self.search_name_input().send_keys(self.device_name)
        time.sleep(1)
        self.search_name_option().click()
        self.search_result().click()
        # 编辑
        self.device_detail_point_btn().click()
        self.edit_device_btn().click()
        self.device_name_input().clear()
        self.device_name_input().send_keys(self.device_edit_name)
        self.add_device_submit_btn().click()

    def senior_set_opera(self):
        '''高级设置操作'''
        # 搜索
        self.search_btn().click()
        # 判断是否有【我知道了】按钮，有则点击
        result = self.is_exist_element(self.i_know)
        if result:
            self.i_know_btn().click()
        else:
            pass
        self.search_name_input().send_keys(self.device_edit_name)
        time.sleep(1)
        self.search_edit_device_option().click()
        self.search_edit_result().click()
        # 高级设置
        self.device_detail_point_btn().click()
        self.senior_set_btn().click()
        self.dehydration_only_time_input().send_keys(self.dehydration_only_time)
        self.laundry_fast_time_input().send_keys(self.laundry_fast_time)
        self.laundry_standard_time_input().send_keys(self.laundry_standard_time)
        self.laundry_object_time_input().send_keys(self.laundry_object_time)
        self.laundry_fast_level_btn().click()
        self.confirm_btn().click()
        self.laundry_standard_level_btn().click()
        self.confirm_btn().click()
        self.laundry_object_level_btn().click()
        self.confirm_btn().click()
        self.canister_clear_btn().click()
        self.confirm_btn().click()
        self.device_model_sure_btn().click()

    def delete_device_opera(self):
        '''删除设备操作'''
        time.sleep(1)
        self.delete_btn().click()
        self.delete_sure_btn().click()



    def devices_management_btn(self):
        '''管理-设备管理按钮'''
        dm_ele = self.get_visible_element(self.devices_management_loc)
        return dm_ele

    def add_btn(self):
        '''设备管理-增加按钮'''
        dm_ele = self.get_visible_element(self.add_loc)
        return dm_ele

    def add_device_btn(self):
        '''设备管理-新增按钮'''
        dm_ele = self.get_visible_element(self.add_device_loc)
        return dm_ele

    def device_name_input(self):
        '''新增设备-设备名称输入框'''
        dm_ele = self.get_visible_element(self.device_name_input_loc)
        return dm_ele

    def belong_shop_btn(self):
        '''新增设备-所属店铺按钮'''
        dm_ele = self.get_visible_element(self.belong_shop_loc)
        return dm_ele

    def confirm_btn(self):
        '''所属店铺-confirm按钮'''
        dm_ele = self.get_visible_element(self.belong_shop_confirm)
        return dm_ele

    def device_type_btn(self):
        '''新增设备-设备类型'''
        dm_ele = self.get_visible_element(self.device_type_loc)
        return dm_ele

    def device_model_btn(self):
        '''新增设备-设备型号'''
        dm_ele = self.get_visible_element(self.device_model_loc)
        return dm_ele

    def often_model_first_btn(self):
        '''设备型号-常用型号第一条'''
        dm_ele = self.get_visible_element(self.often_model_first_loc)
        return dm_ele

    def model_more_btn(self):
        '''设备型号-其他按钮'''
        dm_ele = self.get_visible_element(self.model_more_loc)
        return dm_ele

    def other_model_first_btn(self):
        '''设备型号-其他型号第一条'''
        dm_ele = self.get_visible_element(self.other_model_first_loc)
        return dm_ele

    def device_model_sure_btn(self):
        '''设备型号-确定按钮'''
        dm_ele = self.get_visible_element(self.device_model_sure_loc)
        return dm_ele

    def nqt_scan_btn(self):
        '''新增设备-NQT'''
        dm_ele = self.get_visible_element(self.nqt_scan_loc)
        return dm_ele

    def scan_allow_btn(self):
        '''扫码允许调用相机按钮'''
        dm_ele = self.get_visible_element(self.scan_allow_loc)
        return dm_ele

    def scan_photo_btn(self):
        '''NQT扫码-相册按钮'''
        dm_ele = self.get_visible_element(self.scan_photo_loc)
        return dm_ele

    def album_btn(self):
        '''相册-all media按钮'''
        dm_ele = self.get_visible_element(self.select_album_loc)
        return dm_ele

    def download_btn(self):
        '''相册-Download按钮'''
        dm_ele = self.get_visible_element(self.download_loc)
        return dm_ele

    def code_2(self):
        '''扫码-相册-NQT二维码'''
        dm_ele = self.get_visible_element(self.code_2_loc)
        return dm_ele

    def scan_check_view_btn(self):
        '''相册-选中二维码'''
        dm_ele = self.get_visible_element(self.scan_check_view_loc)
        return dm_ele

    def scan_photo_sure_btn(self):
        '''相册-选中二维码-sure'''
        dm_ele = self.get_visible_element(self.scan_photo_sure_loc)
        return dm_ele

    def imei_scan_btn(self):
        '''新增设备-IMEI扫码按钮'''
        dm_ele = self.get_visible_element(self.imei_scan_loc)
        return dm_ele

    def code_1(self):
        '''相册-IMEI二维码'''
        dm_ele = self.get_visible_element(self.code_1_loc)
        return dm_ele

    def function_set_btn(self):
        '''新增设备-功能设置'''
        dm_ele = self.get_visible_element(self.function_set_loc)
        return dm_ele

    def function_set_edit_input(self):
        '''功能设置-为0的选项'''
        dm_ele = self.get_visible_element(self.function_set_edit_input_loc)
        return dm_ele

    def finish_time_input(self):
        '''功能设置-结束-时间'''
        dm_ele = self.get_visible_element(self.finish_time_input_loc)
        return dm_ele

    def finish_price_input(self):
        '''功能设置-结束-原价'''
        dm_ele = self.get_visible_element(self.finish_price_input_loc)
        return dm_ele

    def function_set_sure_btn(self):
        '''功能设置-确定按钮'''
        dm_ele = self.get_visible_element(self.function_set_sure_loc)
        return dm_ele

    def add_device_submit_btn(self):
        '''新增设备-提交按钮'''
        dm_ele = self.get_visible_element(self.add_device_submit_loc)
        return dm_ele




    # 搜索
    def search_btn(self):
        '''设备管理-搜索按钮'''
        dm_ele = self.get_visible_element(self.search_loc)
        return dm_ele

    def i_know_btn(self):
        '''点击搜索后-我知道了按钮'''
        dm_ele = self.get_visible_element(self.i_know_loc)
        return dm_ele

    def search_name_input(self):
        '''搜索输入框'''
        dm_ele = self.get_visible_element(self.search_name_input_loc)
        return dm_ele

    def search_name_option(self):
        '''搜索选项'''
        dm_ele = self.get_visible_element(self.search_name_option_loc)
        return dm_ele

    def search_result(self):
        '''搜索结果'''
        dm_ele = self.get_visible_element(self.search_result_loc)
        return dm_ele

    def device_detail_point_btn(self):
        '''设备详情页-...按钮'''
        dm_ele = self.get_visible_element(self.device_detail_point_loc)
        return dm_ele

    def edit_device_btn(self):
        '''编辑设备按钮'''
        dm_ele = self.get_visible_element(self.edit_device_loc)
        return dm_ele



    # 高级设置
    def senior_set_btn(self):
        '''高级设置按钮'''
        dm_ele = self.get_visible_element(self.senior_set_loc)
        return dm_ele

    def search_edit_device_option(self):
        '''高级设置-搜索编辑后的设备'''
        dm_ele = self.get_visible_element(self.search_edit_device_option_loc)
        return dm_ele

    def search_edit_result(self):
        '''编辑后设备搜索结果'''
        dm_ele = self.get_visible_element(self.search_edit_result_loc)
        return dm_ele

    def dehydration_only_time_input(self):
        '''高级设置-单脱时长'''
        dm_ele = self.get_visible_element(self.dehydration_only_time_input_loc)
        return dm_ele

    def laundry_fast_time_input(self):
        '''高级设置-快速洗时长'''
        dm_ele = self.get_visible_element(self.laundry_fast_time_input_loc)
        return dm_ele

    def laundry_standard_time_input(self):
        '''高级设置-标准洗时长'''
        dm_ele = self.get_visible_element(self.laundry_standard_time_input_loc)
        return dm_ele

    def laundry_object_time_input(self):
        '''高级设置-大物洗时长'''
        dm_ele = self.get_visible_element(self.laundry_object_time_input_loc)
        return dm_ele

    def laundry_fast_level_btn(self):
        '''高级设置-快速洗水位'''
        dm_ele = self.get_visible_element(self.laundry_fast_level_loc)
        return dm_ele

    def laundry_standard_level_btn(self):
        '''高级设置-标准洗水位'''
        dm_ele = self.get_visible_element(self.laundry_standard_level_loc)
        return dm_ele

    def laundry_object_level_btn(self):
        '''高级设置-大物洗水位'''
        dm_ele = self.get_visible_element(self.laundry_object_level_loc)
        return dm_ele

    def canister_clear_btn(self):
        '''高级设置-设置筒清洁'''
        dm_ele = self.get_visible_element(self.canister_clear_loc)
        return dm_ele


    # 删除
    def delete_btn(self):
        '''设备管理-删除设备按钮'''
        dm_ele = self.get_visible_element(self.delete_loc)
        return dm_ele

    def delete_sure_btn(self):
        '''删除设备-确认删除按钮'''
        dm_ele = self.get_visible_element(self.delete_sure_loc)
        return dm_ele



    # 批量修改
    def batch_update_opera(self):
        '''批量修改操作'''
        self.add_btn().click()
        self.batch_update_btn().click()
        self.update_shop_btn().click()
        self.shop_search_input().send_keys(self.update_shop_name)
        time.sleep(1)
        self.shop_search_result().click()
        self.shop_search_sure_btn().click()
        self.update_device_type_btn().click()
        self.confirm_btn().click()
        self.update_model_btn().click()
        self.confirm_btn().click()
        self.next_btn().click()
        # 功能属性设置，标准洗在5/6之间切换
        current_text = self.get_element_text(self.laundry_standard_price_input_loc, attr='text')
        current_text = int(current_text)
        # print(current_text)
        if current_text == self.laundry_standard_price_update_0:
            text = self.laundry_standard_price_update_1
        elif current_text == self.laundry_standard_price_update_1:
            text = self.laundry_standard_price_update_0
        else:
            text = self.laundry_standard_price_update_0

        # print(text)
        self.laundry_standard_price_input().clear()
        self.laundry_standard_price_input().send_keys(text)
        # 提交
        self.batch_update_page_submit_btn().click()
        self.sure_again_btn().click()


    def batch_update_btn(self):
        '''设备管理-批量修改'''
        dm_ele = self.get_visible_element(self.batch_update_loc)
        return dm_ele

    def update_shop_btn(self):
        '''批量修改-所属店铺'''
        dm_ele = self.get_visible_element(self.update_shop_loc)
        return dm_ele

    def shop_search_input(self):
        '''批量修改-所属店铺-搜索框'''
        dm_ele = self.get_visible_element(self.shop_search_input_loc)
        return dm_ele

    def shop_search_result(self):
        '''所属店铺-搜索结果'''
        dm_ele = self.get_visible_element(self.shop_search_result_loc)
        return dm_ele

    def shop_search_sure_btn(self):
        '''所属店铺-确定按钮'''
        dm_ele = self.get_visible_element(self.shop_search_sure_loc)
        return dm_ele

    def update_device_type_btn(self):
        '''批量修改-设备类型'''
        dm_ele = self.get_visible_element(self.update_device_type_loc)
        return dm_ele

    def update_model_btn(self):
        '''批量修改-设备型号'''
        dm_ele = self.get_visible_element(self.update_model_loc)
        return dm_ele

    def next_btn(self):
        '''批量修改-下一步'''
        dm_ele = self.get_visible_element(self.next_loc)
        return dm_ele

    def dehydration_only_price_input(self):
        '''批量修改-功能属性设置-单脱原价'''
        dm_ele = self.get_visible_element(self.dehydration_only_price_input_loc)
        return dm_ele

    def laundry_fast_price_input(self):
        '''批量修改-功能属性设置-快洗原价'''
        dm_ele = self.get_visible_element(self.laundry_fast_price_input_loc)
        return dm_ele

    def laundry_standard_price_input(self):
        '''批量修改-功能属性设置-标准洗原价'''
        dm_ele = self.get_visible_element(self.laundry_standard_price_input_loc)
        return dm_ele

    def laundry_object_price_input(self):
        '''批量修改-功能属性设置-大物洗原价'''
        dm_ele = self.get_visible_element(self.laundry_object_price_input_loc)
        return dm_ele

    def finished_price_input(self):
        '''批量修改-功能属性设置-结束原价'''
        dm_ele = self.get_visible_element(self.finished_price_input_loc)
        return dm_ele

    def canister_clear_input(self):
        '''批量修改-功能属性设置-桶自洁原价'''
        dm_ele = self.get_visible_element(self.canister_clear_input_loc)
        return dm_ele

    def batch_update_page_submit_btn(self):
        '''批量修改-功能属性设置-提交按钮'''
        dm_ele = self.get_visible_element(self.batch_update_page_submit_loc)
        return dm_ele

    def sure_again_btn(self):
        '''批量修改-再次确定按钮'''
        dm_ele = self.get_visible_element(self.sure_again_loc)
        return dm_ele



    # 批量启动
    def batch_start_opera(self):
        '''批量启动操作'''
        self.add_btn().click()
        self.batch_start_btn().click()
        self.batch_start_search_input().send_keys(self.update_shop_name)
        time.sleep(0.5)
        self.batch_start_search_result().click()
        self.batch_start_device_type().click()
        self.device_function_finish().click()
        self.start_now_btn().click()
        self.sure_again_btn().click()


    def batch_start_btn(self):
        '''设备管理-批量启动按钮'''
        dm_ele = self.get_visible_element(self.batch_start_loc)
        return dm_ele

    def batch_start_search_input(self):
        '''设备管理-批量启动-搜索框'''
        dm_ele = self.get_visible_element(self.batch_start_search_input_loc)
        return dm_ele

    def batch_start_search_result(self):
        '''批量启动-搜索结果'''
        dm_ele = self.get_visible_element(self.batch_start_search_result_loc)
        return dm_ele

    def batch_start_device_type(self):
        '''批量启动-设备类型-洗衣机'''
        dm_ele = self.get_visible_element(self.batch_start_device_type_loc)
        return dm_ele

    def device_function_finish(self):
        '''批量启动-功能-结束'''
        dm_ele = self.get_visible_element(self.device_function_finish_loc)
        return dm_ele

    def start_now_btn(self):
        '''批量启动-立即启动'''
        dm_ele = self.get_visible_element(self.start_now_loc)
        return dm_ele

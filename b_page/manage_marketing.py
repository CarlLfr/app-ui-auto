#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/22
# @Author  : lfr

import time
from b_page.tab import Tab
from b_page.home import HomePage
from common.base_operate import SwitchElement
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By

class ManageMarketing(HomePage):
    '''
    营销管理
    '''
    finance_lease_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="融资租赁"]')
    limited_time_discount_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="限时优惠"]')
    vip_center_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="VIP中心"]')
    coupon_record_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="优惠券记录"]')
    currency_ticket_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_name" and @text="通用小票管理"]')
    # 融资租赁


    # 通用小票管理
    # 新增
    currency_ticket_manage_page_title = "通用小票管理"
    add_currency_ticket_loc = (By.ID, 'com.qekj.merchant:id/iv_search')
    use_store_loc = (By.ID, 'com.qekj.merchant:id/iv_shopname')
    store_name_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_shop_name" and @text="appUl营销管理专用勿操作店铺"]')
    use_store_sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    add_coin_loc = (By.ID, 'com.qekj.merchant:id/iv_add_coin')
    coin_submit_loc = (By.ID, 'com.qekj.merchant:id/ll_submit')
    # 编辑
    currency_ticket_store_name = "appUl营销管理专用勿操作店铺"
    new_coin_plan_loc = (By.XPATH, '//*[@text="appUl营销管理专用勿操作店铺"]')
    edit_coin_loc = (By.ID, 'com.qekj.merchant:id/rl_edit')
    force_use_switch_loc = (By.ID, 'com.qekj.merchant:id/sc_open')
    chongzhi_loc = (By.XPATH, '//android.widget.LinearLayout[@index=6]/android.widget.LinearLayout[1]/android.widget.EditText')
    sell_coin_loc = (By.XPATH, '//android.widget.LinearLayout[@index=6]/android.widget.LinearLayout[3]/android.widget.EditText')
    chongzhi_money = 300
    sell_coin = 5800
    delete_plan_loc = (By.XPATH, '//android.widget.LinearLayout[@index=6]/android.widget.LinearLayout[4]')
    switch_state_1 = "开启"
    # 删除
    delete_loc = (By.ID, 'com.qekj.merchant:id/rl_delete')
    delete_sure_loc = (By.ID, 'android:id/button1')
    # 充值通用小票
    three_point_loc = (By.ID, 'com.qekj.merchant:id/iv_add')
    recharge_coin_loc = (By.XPATH, '//*[@text="充值通用小票"]')
    telephone_input_loc = (By.ID, 'com.qekj.merchant:id/et_phone')
    shop_name_loc = (By.ID, 'com.qekj.merchant:id/tv_shop_name')
    recharge_shop_loc = (By.XPATH, '//*[@text="自动化测试专用店铺"]')
    recharge_price_input_loc = (By.ID, 'com.qekj.merchant:id/et_chongzhi_price')
    give_input_loc = (By.ID, 'com.qekj.merchant:id/et_zengsong')
    telephone = 18768124236
    recharge_price = 10
    give_coin = 100
    recharge_success_toast = "通用小票充值成功"
    # 会员充值记录
    recharge_record_loc = (By.XPATH, '//*[@text="会员充值记录"]')
    search_device_input_loc = (By.ID, 'com.qekj.merchant:id/et_search_device')
    search_device_name_loc = (By.XPATH, '//*[@resource-id="com.qekj.merchant:id/tv_shop" and @text="自动化测试专用店铺"]')
    search_single_loc = (By.ID, 'com.qekj.merchant:id/iv_search_single')
    search_telephone_input_loc = (By.ID, 'com.qekj.merchant:id/et_search')
    the_first_record_time_loc = (By.ID, 'com.qekj.merchant:id/tv_time')
    the_first_record_type_loc = (By.ID, 'com.qekj.merchant:id/tv_type')
    recharge_shop_name = "自动化测试专用店铺"
    recharge_telephone = 18768124236
    recharge_type_1 = "商户代充"
    recharge_type_2 = "通用小票回收"
    recharge_record_cancel_loc = (By.ID, 'com.qekj.merchant:id/tv_cancel')
    recharge_record_back_loc = (By.ID, 'com.qekj.merchant:id/ll_back')
    # 会员管理
    member_manage_loc = (By.XPATH, '//*[@text="会员管理"]')
    coin_recovery_loc = (By.ID, 'com.qekj.merchant:id/ll_jinbihuishou')
    recharge_money_input_loc = (By.ID, 'com.qekj.merchant:id/et_chongzhi_price')
    member_give_coin_input_loc = (By.ID, 'com.qekj.merchant:id/et_zengsong_price')
    member_manage_sure_loc = (By.ID, 'com.qekj.merchant:id/ll_sure')
    recovery_coin = 1000
    recovery_given_coin = 100
    recovery_sure_again_loc = (By.ID, 'android:id/button1')
    recovery_success_toast = "用户通用小票回收操作成功"


    # 限时优惠
    discount_add_loc = (By.ID, 'com.qekj.merchant:id/iv_search_single')
    belong_store_loc = (By.ID, 'com.qekj.merchant:id/rl_belong_store')
    belong_store_name_loc = (By.XPATH, '//*[@text="appUl营销管理专用勿操作店铺"]')
    discount_sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    belong_store_select_loc = (By.XPATH, '//*[@text="appUl营销管理专用勿操作店铺"]/../[@resource-id="com.qekj.merchant:id/iv_select"]')

    device_type_loc = (By.ID, 'com.qekj.merchant:id/rl_device_type')
    discount_confirm_loc = (By.ID, 'com.qekj.merchant:id/btnSubmit')
    discount_cancel_loc = (By.ID, 'com.qekj.merchant:id/btnCancel')
    promotional_start_loc = (By.ID, 'com.qekj.merchant:id/rl_promotional_start')
    promotional_end_loc = (By.ID, 'com.qekj.merchant:id/rl_promotional_end')
    day_time_loc = (By.ID, 'com.qekj.merchant:id/day')
    promotional_topbar_loc = (By.ID, 'com.qekj.merchant:id/rv_topbar')
    activity_day_loc = (By.ID, 'com.qekj.merchant:id/rl_activity_day')
    activity_period_loc = (By.ID, 'com.qekj.merchant:id/rl_every_day_activity')
    discount_loc = (By.ID, 'com.qekj.merchant:id/et_discount')
    discount_submit_loc = (By.ID, 'com.qekj.merchant:id/rl_submit')
    discount = 7
    limited_time_page_page_title = "限时优惠"
    belong_store_name = "appUl营销管理专用勿操作店铺"
    add_success_toast = "添加成功"
    # 编辑
    edit_loc = (By.ID, 'com.qekj.merchant:id/rl_edit')
    edit_discount = 8
    discount_switch_loc = (By.XPATH, '//*[@text="appUl营销管理专用勿操作店铺"]/../../../android.widget.Switch')
    discount_switch_state = "OFF"
    edit_success_toast = "修改成功"
    delete_success_toast = "删除成功"


    # VIP中心
    add_vip_loc = (By.ID, 'com.qekj.merchant:id/iv_search')
    apply_store_loc = (By.ID, 'com.qekj.merchant:id/rl_shop')
    sure_loc = (By.ID, 'com.qekj.merchant:id/tv_sure')
    input_discount_loc = (By.ID, 'com.qekj.merchant:id/et_input_discount')
    input_limit_times_loc = (By.ID, 'com.qekj.merchant:id/et_input_times')
    three_price_loc = (By.ID, 'com.qekj.merchant:id/et_three_price')
    six_price_loc = (By.ID, 'com.qekj.merchant:id/et_six_price')
    twelve_price_loc = (By.ID, 'com.qekj.merchant:id/et_twelve_price')
    vip_submit_loc = (By.ID, 'com.qekj.merchant:id/ll_submit')
    vip_discount = 7
    modify_vip_discount = 6
    limit_time = 8
    modify_limit_time = 9
    three_price = 50
    six_price = 100
    twelve_price = 180
    modify_twelve_price = 190
    vip_add_success_toast = "新增成功"
    vip_edit_success_toast = "修改成功"
    vip_centre_title = "VIP中心"

    # 优惠券记录
    search_loc = (By.ID, 'com.qekj.merchant:id/iv_search_single')
    search_input_loc = (By.ID, 'com.qekj.merchant:id/et_search')

    def enter_to_financeLease(self):
        '''点击进入融资租赁页'''
        self.finance_lease_btn().click()

    def finance_lease_btn(self):
        '''营销管理-融资租赁按钮'''
        mk_ele = self.get_visible_element(self.finance_lease_loc)
        return mk_ele


    # 通用小票管理
    def enter_to_currency_ticket_manage(self):
        '''点击进入通用小票管理页面'''
        self.currency_ticket_btn().click()

    def add_currency_ticket_opera(self):
        '''新增通用小票操作'''
        self.add_currency_ticket_btn().click()
        self.use_store_btn().click()
        self.store_name().click()
        self.use_store_sure_btn().click()
        self.coin_submit_btn().click()
        time.sleep(2)

    def edit_currency_ticket_opera(self):
        '''编辑通用小票操作'''
        self.new_currency_ticket_btn().click()
        self.edit_coin_btn().click()
        # 打开强制使用开关
        self.force_use_switch_btn().click()
        # 新增通用小票方案
        self.add_coin_btn().click()
        self.chongzhi_input_box().send_keys(self.chongzhi_money)
        self.sell_coin_input_box().send_keys(self.sell_coin)
        self.coin_submit_btn().click()
        time.sleep(1)

    def delete_opera(self):
        '''删除通用小票操作'''
        self.delete_btn().click()
        self.delete_sure_btn().click()
        time.sleep(1)

    def recharge_coin_opera(self):
        '''充值通用小票操作'''
        self.three_point_btn().click()
        self.recharge_coin_btn().click()
        self.telephone_input().send_keys(self.telephone)
        self.shop_name_btn().click()
        self.coin_shop_btn().click()
        self.sure_btn().click()
        self.recharge_price_input().send_keys(self.recharge_price)
        self.give_input().send_keys(self.give_coin)
        time.sleep(1)
        self.coin_submit_btn().click()

    def recharge_record_opera(self):
        '''查询会员充值记录操作：自动化测试专用店铺-搜索手机号18768124236'''
        self.three_point_btn().click()
        self.recharge_record_btn().click()
        self.search_device_input().send_keys(self.recharge_shop_name)
        time.sleep(1)
        self.search_device_name_btn().click()
        self.search_single_btn().click()
        self.search_telephone_input().send_keys(self.recharge_telephone)
        time.sleep(1)

    def the_first_recharge_record_time(self):
        '''获取会员充值记录 第一条记录的日期'''
        text = self.the_first_record_time().get_attribute('text')
        date = text.split(" ")[0]
        return date

    def the_first_recharge_record_type(self):
        '''获取会员充值记录 第一条记录的type'''
        text = self.the_first_record_type().get_attribute('text')
        return text

    def back_to_manage_page_opera(self):
        '''会员记录页返回至通用小票管理页'''
        self.recharge_record_cancel_btn().click()
        self.recharge_record_back_btn().click()
        time.sleep(1)

    def member_manage_recovery_coin_opera(self):
        '''会员管理-回收小票操作'''
        self.three_point_btn().click()
        self.member_manage_btn().click()
        # 搜索对应手机号的充值记录
        self.search_device_input().send_keys(self.recharge_shop_name)
        time.sleep(1)
        self.search_device_name_btn().click()
        self.search_single_btn().click()
        self.search_telephone_input().send_keys(self.recharge_telephone)
        # 点击【小票回收】
        self.coin_recovery_btn().click()
        self.recharge_money_input().send_keys(self.recovery_coin)
        self.member_give_coin_input().send_keys(self.recovery_given_coin)
        self.member_manage_sure_btn().click()
        self.recovery_sure_again_btn().click()



    def currency_ticket_btn(self):
        '''营销管理-通用小票管理按钮'''
        mk_ele = self.get_visible_element(self.currency_ticket_loc)
        return mk_ele

    def add_currency_ticket_btn(self):
        '''通用小票管理-新增按钮'''
        mk_ele = self.get_visible_element(self.add_currency_ticket_loc)
        return mk_ele

    def use_store_btn(self):
        '''新增通用小票-适用店铺按钮'''
        mk_ele = self.get_visible_element(self.use_store_loc)
        return mk_ele

    def store_name(self):
        '''新增通用小票-使用店铺名称'''
        mk_ele = self.get_visible_element(self.store_name_loc)
        return mk_ele

    def use_store_sure_btn(self):
        '''新增通用小票-使用店铺-确定按钮'''
        mk_ele = self.get_visible_element(self.use_store_sure_loc)
        return mk_ele

    def coin_submit_btn(self):
        '''新增通用小票-提交按钮'''
        mk_ele = self.get_visible_element(self.coin_submit_loc)
        return mk_ele

    def new_currency_ticket_btn(self):
        '''通用小票管理页-新增的通用小票'''
        mk_ele = self.get_visible_element(self.new_coin_plan_loc)
        return mk_ele

    def edit_coin_btn(self):
        '''通用小票详情页-编辑按钮'''
        mk_ele = self.get_visible_element(self.edit_coin_loc)
        return mk_ele

    def force_use_switch_btn(self):
        '''通用小票编辑页-强制使用按钮'''
        mk_ele = self.get_visible_element(self.force_use_switch_loc)
        return mk_ele

    def add_coin_btn(self):
        '''通用小票编辑页-增加方案按钮'''
        mk_ele = self.get_visible_element(self.add_coin_loc)
        return mk_ele

    def chongzhi_input_box(self):
        '''通用小票编辑页-充值金额输入框'''
        mk_ele = self.get_visible_element(self.chongzhi_loc)
        return mk_ele

    def sell_coin_input_box(self):
        '''通用小票编辑页-赠送小票输入框'''
        mk_ele = self.get_visible_element(self.sell_coin_loc)
        return mk_ele

    def delete_btn(self):
        '''用小票详情页-删除按钮'''
        mk_ele = self.get_visible_element(self.delete_loc)
        return mk_ele

    def delete_sure_btn(self):
        '''删除通用小票-删除按钮'''
        mk_ele = self.get_visible_element(self.delete_sure_loc)
        return mk_ele

    def three_point_btn(self):
        '''通用小票管理-...按钮'''
        mk_ele = self.get_visible_element(self.three_point_loc)
        return mk_ele

    def recharge_coin_btn(self):
        '''通用小票管理-充值通用小票按钮'''
        mk_ele = self.get_visible_element(self.recharge_coin_loc)
        return mk_ele

    def telephone_input(self):
        '''通用小票管理-充值通用小票-手机号输入框'''
        mk_ele = self.get_visible_element(self.telephone_input_loc)
        return mk_ele

    def shop_name_btn(self):
        '''充值通用小票-适用店铺'''
        mk_ele = self.get_visible_element(self.shop_name_loc)
        return mk_ele

    def coin_shop_btn(self):
        '''充值通用小票-适用店铺-选择店铺'''
        mk_ele = self.get_visible_element(self.recharge_shop_loc)
        return mk_ele

    def recharge_price_input(self):
        '''充值通用小票-充值金额'''
        mk_ele = self.get_visible_element(self.recharge_price_input_loc)
        return mk_ele

    def give_input(self):
        '''充值通用小票-赠送金额'''
        mk_ele = self.get_visible_element(self.give_input_loc)
        return mk_ele

    def recharge_record_btn(self):
        '''通用小票管理-会员充值记录'''
        mk_ele = self.get_visible_element(self.recharge_record_loc)
        return mk_ele

    def search_device_input(self):
        '''会员充值记录-店铺搜索'''
        mk_ele = self.get_visible_element(self.search_device_input_loc)
        return mk_ele

    def search_device_name_btn(self):
        '''会员充值记录-店铺搜索-店铺'''
        mk_ele = self.get_visible_element(self.search_device_name_loc)
        return mk_ele

    def search_single_btn(self):
        '''会员充值记录-手机号搜索按钮'''
        mk_ele = self.get_visible_element(self.search_single_loc)
        return mk_ele

    def search_telephone_input(self):
        '''会员充值记录-手机号搜索输入框'''
        mk_ele = self.get_visible_element(self.search_telephone_input_loc)
        return mk_ele

    def the_first_record_time(self):
        '''会员充值记录-手机号搜索第一条记录的时间'''
        mk_ele = self.get_visible_element(self.the_first_record_time_loc)
        return mk_ele

    def the_first_record_type(self):
        '''会员充值记录-手机号搜索第一条记录的type'''
        mk_ele = self.get_visible_element(self.the_first_record_type_loc)
        return mk_ele

    def recharge_record_cancel_btn(self):
        '''会员充值记录-取消按钮'''
        mk_ele = self.get_visible_element(self.recharge_record_cancel_loc)
        return mk_ele

    def recharge_record_back_btn(self):
        '''会员充值记录-返回按钮'''
        mk_ele = self.get_visible_element(self.recharge_record_back_loc)
        return mk_ele

    def member_manage_btn(self):
        '''通用小票管理-会员管理'''
        mk_ele = self.get_visible_element(self.member_manage_loc)
        return mk_ele

    def coin_recovery_btn(self):
        '''会员管理-小票回收'''
        mk_ele = self.get_visible_element(self.coin_recovery_loc)
        return mk_ele

    def recharge_money_input(self):
        '''小票回收-小票本金输入框'''
        mk_ele = self.get_visible_element(self.recharge_money_input_loc)
        return mk_ele

    def member_give_coin_input(self):
        '''小票回收-赠送小票输入框'''
        mk_ele = self.get_visible_element(self.member_give_coin_input_loc)
        return mk_ele

    def member_manage_sure_btn(self):
        '''小票回收-确定按钮'''
        mk_ele = self.get_visible_element(self.member_manage_sure_loc)
        return mk_ele

    def recovery_sure_again_btn(self):
        '''小票回收-再次确认按钮'''
        mk_ele = self.get_visible_element(self.recovery_sure_again_loc)
        return mk_ele




    # 限时优惠
    def enter_to_limited_time_discount(self):
        '''点击进入限时优惠'''
        self.limited_time_discount_btn().click()

    def add_discount_opera(self):
        '''新增限时优惠操作'''
        self.discount_add_btn().click()
        self.belong_store_btn().click()
        # 所属店铺
        self.belong_store_name_btn().click()
        self.discount_sure_btn().click()
        # 设备类型
        self.device_type_btn().click()
        self.discount_confirm_btn().click()
        # 优惠期
        self.promotional_start_btn().click()
        self.discount_confirm_btn().click()
        self.promotional_end_btn().click()
        se = SwitchElement(self.driver, self.day_time(), self.promotional_topbar())
        se.switch_element_up()
        self.discount_confirm_btn().click()
        # 活动日，每日活动时段，优惠折扣
        self.activity_day_btn().click()
        self.discount_confirm_btn().click()
        self.activity_period_btn().click()
        self.discount_sure_btn().click()
        self.discount_input().send_keys(self.discount)
        self.discount_submit_btn().click()
        time.sleep(1)

    def edit_discount_opera(self):
        '''编辑限时优惠操作'''
        self.belong_store_name_btn().click()
        self.edit_btn().click()
        self.discount_input().clear()
        time.sleep(0.5)
        self.discount_input().send_keys(self.edit_discount)
        time.sleep(1.5)
        self.discount_submit_btn().click()
        time.sleep(1)

    def switch_discount_opera(self):
        '''限时优惠开关操作'''
        self.discount_switch_btn().click()
        time.sleep(1)

    def delete_discount_opera(self):
        '''删除限时优惠操作'''
        self.belong_store_name_btn().click()
        self.delete_opera()


    def limited_time_discount_btn(self):
        '''营销管理-限时优惠'''
        mk_ele = self.get_visible_element(self.limited_time_discount_loc)
        return mk_ele

    def discount_add_btn(self):
        '''限时优惠-新增优惠按钮'''
        mk_ele = self.get_visible_element(self.discount_add_loc)
        return mk_ele

    def belong_store_btn(self):
        '''限时优惠-新增优惠-所属店铺'''
        mk_ele = self.get_visible_element(self.belong_store_loc)
        return mk_ele

    def belong_store_input(self):
        '''限时优惠-新增优惠-所属店铺搜索输入框'''
        mk_ele = self.get_visible_element(self.belong_store_name_loc)
        return mk_ele

    def belong_store_select_btn(self):
        '''限时优惠-新增优惠-所属店铺-选择'''
        mk_ele = self.get_visible_element(self.belong_store_select_loc)
        return mk_ele

    def belong_store_name_btn(self):
        '''限时优惠-新增优惠-所属店铺-店铺'''
        mk_ele = self.get_visible_element(self.belong_store_name_loc)
        return mk_ele

    def discount_sure_btn(self):
        '''限时优惠-新增优惠-确定按钮'''
        mk_ele = self.get_visible_element(self.discount_sure_loc)
        return mk_ele

    def device_type_btn(self):
        '''限时优惠-新增优惠-设备类型'''
        mk_ele = self.get_visible_element(self.device_type_loc)
        return mk_ele

    def discount_confirm_btn(self):
        '''限时优惠-新增优惠-confirm'''
        mk_ele = self.get_visible_element(self.discount_confirm_loc)
        return mk_ele

    def discount_cancel_btn(self):
        '''限时优惠-新增优惠-cancel'''
        mk_ele = self.get_visible_element(self.discount_cancel_loc)
        return mk_ele

    def promotional_start_btn(self):
        '''限时优惠-新增优惠-优惠期开始'''
        mk_ele = self.get_visible_element(self.promotional_start_loc)
        return mk_ele

    def promotional_end_btn(self):
        '''限时优惠-新增优惠-优惠期结束'''
        mk_ele = self.get_visible_element(self.promotional_end_loc)
        return mk_ele

    def day_time(self):
        '''限时优惠-新增优惠-优惠期结束-天'''
        mk_ele = self.get_visible_element(self.day_time_loc)
        return mk_ele

    def promotional_topbar(self):
        '''限时优惠-新增优惠-优惠期结束-时间弹窗topbar'''
        mk_ele = self.get_visible_element(self.promotional_topbar_loc)
        return mk_ele
        # mk_ele = self.driver.find_element_by_id('com.qekj.merchant:id/rv_topbar')
        # return mk_ele

    def activity_day_btn(self):
        '''限时优惠-新增优惠-活动日'''
        mk_ele = self.get_visible_element(self.activity_day_loc)
        return mk_ele

    def activity_period_btn(self):
        '''限时优惠-新增优惠-每日活动时段'''
        mk_ele = self.get_visible_element(self.activity_period_loc)
        return mk_ele

    def discount_input(self):
        '''限时优惠-新增优惠-折扣优惠'''
        mk_ele = self.get_visible_element(self.discount_loc)
        return mk_ele

    def discount_submit_btn(self):
        '''限时优惠-新增优惠-提交'''
        mk_ele = self.get_visible_element(self.discount_submit_loc)
        return mk_ele

    def edit_btn(self):
        '''限时优惠-优惠详情-编辑按钮'''
        mk_ele = self.get_visible_element(self.edit_loc)
        return mk_ele

    def discount_switch_btn(self):
        '''限时优惠-开关'''
        mk_ele = self.get_visible_element(self.discount_switch_loc)
        return mk_ele



    # VIP中心
    def enter_to_vip_center(self):
        '''进入vip中心'''
        self.vip_center_btn().click()

    def add_vip_opera(self):
        '''新增vip操作'''
        self.add_vip_btn().click()
        self.apply_store_btn().click()
        self.vip_apply_store_name().click()
        time.sleep(1)
        self.sure_btn().click()
        self.input_discount().send_keys(self.vip_discount)
        self.input_limit_times_input().send_keys(self.limit_time)
        self.three_price_input().send_keys(self.three_price)
        self.six_price_input().send_keys(self.six_price)
        self.twelve_price_input().send_keys(self.twelve_price)
        self.vip_submit_btn().click()
        time.sleep(1)

    def edit_vip_opera(self):
        '''编辑vip操作'''
        self.belong_store_name_btn().click()
        self.edit_btn().click()
        self.input_discount().clear()
        self.input_discount().send_keys(self.modify_vip_discount)
        self.input_limit_times_input().clear()
        self.input_limit_times_input().send_keys(self.modify_limit_time)
        self.twelve_price_input().clear()
        self.twelve_price_input().send_keys(self.modify_twelve_price)
        self.vip_submit_btn().click()
        time.sleep(1)

    def delete_vip_opera(self):
        '''删除vip操作'''
        self.belong_store_name_btn().click()
        self.delete_opera()


    def vip_center_btn(self):
        '''营销管理-VIP中心'''
        mk_ele = self.get_visible_element(self.vip_center_loc)
        return mk_ele

    def add_vip_btn(self):
        '''营销管理-VIP中心-新增按钮'''
        mk_ele = self.get_visible_element(self.add_vip_loc)
        return mk_ele

    def apply_store_btn(self):
        '''VIP中心-新增-适用店铺'''
        mk_ele = self.get_visible_element(self.apply_store_loc)
        return mk_ele

    def vip_apply_store_name(self):
        '''VIP中心-新增-适用店铺-店铺名'''
        mk_ele = self.get_visible_element(self.belong_store_name_loc)
        return mk_ele

    def sure_btn(self):
        '''VIP中心-新增-适用店铺-确定'''
        mk_ele = self.get_visible_element(self.sure_loc)
        return mk_ele

    def input_discount(self):
        '''VIP中心-新增-折扣'''
        mk_ele = self.get_visible_element(self.input_discount_loc)
        return mk_ele

    def input_limit_times_input(self):
        '''VIP中心-新增-每日限用次数'''
        mk_ele = self.get_visible_element(self.input_limit_times_loc)
        return mk_ele

    def three_price_input(self):
        '''VIP中心-新增-3个月价格'''
        mk_ele = self.get_visible_element(self.three_price_loc)
        return mk_ele

    def six_price_input(self):
        '''VIP中心-新增-6个月价格'''
        mk_ele = self.get_visible_element(self.six_price_loc)
        return mk_ele

    def twelve_price_input(self):
        '''VIP中心-新增-12个月价格'''
        mk_ele = self.get_visible_element(self.twelve_price_loc)
        return mk_ele

    def vip_submit_btn(self):
        '''VIP中心-新增-提交按钮'''
        mk_ele = self.get_visible_element(self.vip_submit_loc)
        return mk_ele




    def coupon_record_btn(self):
        '''营销管理-优惠券记录'''
        mk_ele = self.get_visible_element(self.coupon_record_loc)
        return mk_ele

import time
import unittest
import warnings
from common.app_common.element_action import *
import os
import re
from appium import webdriver
from common.app_common.read_config import *
from config.load_file import *
from utx import log
from utx import *
from common.app_common.read_config import *
from common.app_common.shell_install_adb import *
from common.app_common.shell_boot_adb import *
from common.app_common.shell_monkey_adb import *
from demo.baseclass.base_mine_pageUI import *
from demo.baseclass.base_message_pageUI import *

class BasePage():

    def driver_begin(self, app):
        """
        param app: appName
        """
        deviceName = os.popen('adb shell getprop ro.product.model').read()  # 获取设备名称
        log.info("测试设备为%s" % deviceName)
        # 读取设备系统版本号
        deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
        log.info("测试设备系统版本为%s" % deviceAndroidVersion)
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        package_name = read_ini(ini_file_path=load_file('app_conf'), name=app, value='appPackage')
        activity_name = read_ini(ini_file_path=load_file('app_conf'), name=app, value='appActivity')
        platformName = 'Android'
        print(package_name, activity_name)
        desired_caps = {
            'platformName': platformName,
            'deviceName': deviceName,
            'platformVersion': deviceVersion,
            'appPackage': package_name,
            'appActivity': activity_name,
            'noReset': False,
            'resetKeyboard': False  # 将键盘给隐藏起来
            # 'unicodeKeyboard': True,# 使用unicodeKeyboard的编码方式来发送字符串
        }
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def login_base(self, driver,user_number, password):
        time.sleep(2)
        log.info("开始执行登录操作")
        log.info("----" * 15)
        inputting(driver=driver, type='id_type', section_name='登录页面', name='输入框', txt=user_number)
        log.info("输入账号")
        inputting(driver=driver, type='id_type', section_name='登录页面', name='密码', txt=password)
        log.info("输入密码")
        clicking(driver=driver, type='id_type', section_name='登录页面', name='登录按钮')
        log.info("点击登录")

    def skip_limits(self,driver):
        """跳过权限弹窗，允许"""
        time.sleep(2)
        log.info("操作权限弹窗")
        clicking(driver=driver, type='id_type', section_name='权限', name='允许')
        time.sleep(2)

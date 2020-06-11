import os
import re

from appium import webdriver

from common.appium_common.read_config import read_ini
from config.appium_conf.load_file import load_file
from utx import log


def driver_begin(app):
    deviceName = os.popen('adb shell getprop ro.product.model').read()  # 获取设备名称
    log.info("测试设备为%s"%deviceName)
    # 读取设备系统版本号
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    log.info("测试设备系统版本为%s" % deviceAndroidVersion)
    deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
    package_name = read_ini(ini_file_path=load_file(5), name=app, value='appPackage')
    activity_name = read_ini(ini_file_path=load_file(5), name=app, value='appActivity')
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

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
# from common.app_common.session import *
from common.app_common.shell_monkey_adb import *
from demo.my_test import *


class BasePageMine():

    def into_mine(self, driver):
        """从导航进入我的页面"""
        time.sleep(2)
        log.info("进入我的")
        clicking(driver=driver, type=id_type, section_name='导航', name='我的')

    def into_my_information(self, driver):
        """从我的页面点开我的个人信息"""
        time.sleep(1)
        log.info("进入我的个人信息")
        clicking(driver=driver, type=id_type, section_name='我的', name='个人信息')

    def user_name(self, driver):
        """从个人信息点击昵称"""
        time.sleep(1)
        log.info("点击昵称进行修改")
        clicking(driver=driver, type=id_type, section_name='我的', name='昵称')

    def user_img(self, driver):
        """点击头像信息"""
        time.sleep(1)
        log.info("点击昵称进行修改")
        clicking(driver=driver, type=id_type, section_name='我的', name='头像')
        # clicking(driver=driver, type=id_type, section_name='相机', name='拍照')

    def back(self, driver):
        """返回"""
        time.sleep(0.5)
        log.info("返回")
        clicking(driver=driver, type=id_type, section_name='我的', name='返回')

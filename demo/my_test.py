from common.conf_path import *
from common.api_common.comm import *
from utx import *
from common.app_common.read_config import *
from common.app_common.shell_install_adb import *
from common.app_common.shell_boot_adb import *
from common.app_common.shell_monkey_adb import *
import time
import warnings
import unittest
import os
import re
from appium import webdriver
from common.app_common.element_action import *

# 用户信息
user_1 = read_ini(ini_file_path=parameter_conf_path, name='用户', value='user_1')
password = read_ini(ini_file_path=parameter_conf_path, name='用户', value='password')

# app信息
app_name_nly = read_ini(ini_file_path=app_conf_path, name='牛老幺', value='appName')
package_name_nly = read_ini(ini_file_path=app_conf_path, name='牛老幺', value='appPackage')
activity_name_nly = read_ini(ini_file_path=app_conf_path, name='牛老幺', value='appActivity')
print(app_name_nly)

# 元素类型
id_type = 'id_type'
class_name_type = 'class_name_type'
location_type = 'location_type'
xpath_type = 'xpath_type'

# 安装包存放路径release包
# apk_path = r"D:\PythonWorkSpace\Test_Api_App\data\app-release.apk"
# 安装包存放路径debug包
apk_path=r"D:\PythonWorkSpace\Test_Api_App\data\app-debug.apk"

# monkey日志存放路径
monkey_log_path = "D:\\PythonWorkSpace\\Test_Api_App\\demo\\report"

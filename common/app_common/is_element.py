# —*- coding:utf-8 -*-
#Created by Administrator on 2020/6/16
#Copyright (C) 2020 $USER.All rights reserved.
import time
from common.app_common.read_config import read_ini
from common.conf_path import *


def is_element(driver,ini_file_path,section_name,name):
    """判断当前页面元素是否存在"""
    ele=read_ini(ini_file_path,section_name,name)
    time.sleep(4)
    if ini_file_path==ele_id_conf_path:
        if driver.find_elements_by_id(ele) == []:
            return False
        else:
            return True
    if ini_file_path==ele_xpath_conf_path:
        if driver.find_elements_by_xpath(ele)==[]:
            return False
        else:
            return True



# —*- coding:utf-8 -*-
# Created by Administrator on 2020/6/11
# Copyright (C) 2020 $USER.All rights reserved.
# 执行测试，times为次数，结果取平均值
import os
import re

from common.appium_common.shell_adb import *


def run_boot_test(times):
    cold_time = []
    hot_time = []
    # 读取设备 id
    read_device_id = list(os.popen('adb devices').readlines())

    # 正则表达式匹配出 id 信息
    device_id = re.findall(r'^\w*\b', read_device_id[1])[0]

    for i in range(times):
        cold_time.append(get_cold_boot_time('com.foryou.agent', '.appentry.EntryActivity'))
        hot_time.append(get_hot_boot_time('com.foryou.agent', '.appentry.EntryActivity', device_id))
    res_cold_time = 0
    res_hot_time = 0
    print("冷启动时间 = " + str(cold_time))
    print("热启动时间 = " + str(hot_time))
    for i in cold_time:
        res_cold_time = res_cold_time + i
    print('平均冷启动时间: ' + str(res_cold_time / times) + ' ms')
    for i in hot_time:
        res_hot_time = res_hot_time + i
    print('平均热启动时间: ' + str(res_hot_time / times) + ' ms')


if __name__ == '__main__':
    run_boot_test(5)

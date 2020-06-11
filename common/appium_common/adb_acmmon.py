# —*- coding:utf-8 -*-
# Created by Administrator on 2020/6/11
# Copyright (C) 2020 $USER.All rights reserved.
# python module for interacting with adb
import os
import time

import subprocess

'''
基本的adb操作
'''


class AndroidDebugBridge():
    def install(self,dev):
        cmd1 = "adb -s  " + dev + "  install  " + Config.path + "\\script\\haoyun_4.4.0_100_201909091812.apk"
        os.popen(cmd1)
        time.sleep(20)


    def ram_monkey(dev):
        # Monkey测试结果日志:monkey_log
        adb_monkey = "shell monkey -p %s -s %s %s" % (Config.package_name, Config.monkey_seed, Config.monkey_parameters)
        monkey_log = Config.path + "\\log\\" + dev + "monkey.log"
        cmd_monkey = "adb -s %s %s > %s" % (dev, adb_monkey, monkey_log)
        os.popen(cmd_monkey)
        time.sleep(300)


    def rm_file(dev, logincmd):
        d1 = "adb -s " + dev + " shell   rm  -r   /sdcard/" + logincmd
        os.popen(d1)


    def close(self,dev):
        pid = AdbCommon.get_pid(Config.package_name, dev)
        close_cmd = "adb -s  " + dev + " shell kill   " + pid
        os.popen(close_cmd)


    def uninstall(self,dev):
        cmdunin = "adb -s  " + dev + " uninstall   com.foryou.haoyun"
        AdbCommon.call_adb(cmdunin)

    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        # print(command_text)
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # check for any fastboot device
    def fastboot(self, device_id):
        pass

    # 检查设备
    def attached_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]

    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    # 重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def push(self, dev, local, remote):
        result = self.call_adb("push  -s  %s  %s %s" % (dev, local, remote))
        return result

    # 拉数据到本地
    def pull(self, dev, remote, local):
        result = self.call_adb("pull %s %s" % (dev, remote, local))
        return result

    # 同步更新 很少用此命名
    def sync(self, directory, **kwargs):
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = self.call_adb(command)
            return result

    # 打开指定app
    def open_app(self, packagename, activity, dev):
        result = self.call_adb("-s " + dev + " shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    def get_pid(pkg_name, dev):
        # print("----get_pid-------")
        pid = subprocess.Popen("adb -s " + dev + " shell ps | findstr " + pkg_name, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.readlines()
        for item in pid:
            if item.split()[8].decode() == pkg_name:
                return item.split()[1].decode()

    def get_report(dev):
        path = os.path.abspath('.')
        d1 = "adb -s  " + dev + "  bugreport  " + path + "\\report\\" + dev + "_bugreport.zip "
        os.popen(d1)
        time.sleep(200)
        t1 = "mkdir  " + path + "\\report\\" + dev + "_bugreport"
        os.popen(t1)
        d2 = "7z x " + path + "\\report\\" + dev + "_bugreport.zip   -o" + path + "\\report\\" + dev + "_bugreport"
        os.popen(d2)
        time.sleep(10)
        for filename in os.listdir(path + "\\report\\" + dev + "_bugreport"):
            if 'bugreport' in filename:
                d8 = "java -jar  " + path + "\\chkbugreport-0.5-215.jar   " + path + "\\report\\" + dev + "_bugreport\\" + filename
                os.popen(d8)
                time.sleep(200)


if __name__ == '__main__':
    pass

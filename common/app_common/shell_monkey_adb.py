import os
import random
import re
import time


class MonkeyShell():

    def __init__(self, package, times, path):
        self.package = package
        self.times = times
        self.path = path

    def monkey(self):
        monkey_seed = str(random.randrange(1, 1000))
        # 读取设备 id
        readDeviceId = list(os.popen('adb devices').readlines())
        # 正则表达式匹配出 id 信息
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        # monkey参数设置
        monkey_parameters = " --ignore-timeouts --hprof  --pct-syskeys 0  --pct-touch 40 --pct-trackball 40 --pct-appswitch 0  --pct-motion 20  --monitor-native-crashes  -v -v -v --throttle  200 %s" % self.times
        # monkey脚本拼接
        shell_monkey = "shell monkey -p %s -s %s %s" % (self.package, monkey_seed, monkey_parameters)
        # 日志输出命令
        now = time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))
        monkey_log = self.path + "\\monkey.log"+now
        # 拼接命令
        adb_monkey = "adb  -s %s %s>%s" % (deviceId, shell_monkey, monkey_log)
        # 执行脚本
        os.system(adb_monkey)

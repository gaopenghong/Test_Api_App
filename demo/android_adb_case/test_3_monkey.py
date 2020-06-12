import os
import random
import re
import unittest
import  warnings
from common.appium_common.read_config import *
from utx import log


class MonkeyCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore',ResourceWarning)
        cls.app = '牛老幺'
        cls.package = read_package_name(cls.app)# 包名获取
        cls.activity = read_activity_name(cls.app)# 入口名获取
        cls.path = "D:\\PythonWorkSpace\\Test_Api_App\\demo\\report"#  monkey日志存放路径
        # monkey执行时间次数
        cls.times = int(1000)

    def test_monkey(self):
        monkey_seed = str(random.randrange(1, 1000))
        # 读取设备 id
        readDeviceId = list(os.popen('adb devices').readlines())
        # 正则表达式匹配出 id 信息
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        # monkey参数设置
        monkey_parameters = " --ignore-timeouts --pct-touch 40 --pct-trackball 40 --pct-appswitch 0  --pct-motion 20 -v -v  --throttle  500 %s"%self.times
        # monkey脚本拼接
        shell_monkey = "shell monkey -p %s -s %s %s" % (self.package, monkey_seed, monkey_parameters)
        # 日志输出命令
        monkey_log = self.path + "\\monkey.log"
        # 拼接命令
        adb_monkey = "adb  -s %s %s>%s" % (deviceId, shell_monkey,monkey_log)
        # 执行脚本
        os.system(adb_monkey)
        log.info("开始执行monkey脚本，大约用时%s分钟")%str(self.times/120)



if __name__ == '__main__':
    unittest.main()

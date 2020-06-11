import os
import random
import re
import unittest
import  warnings
from common.appium_common.read_config import *


class MonkeyCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore',ResourceWarning)
        cls.app = '牛老幺'
        cls.package = read_package_name(cls.app)
        cls.activity = read_activity_name(cls.app)
        cls.path = "D:\\PythonWorkSpace\\Test_Api_App\\demo\\report"

    def test_monkey(self):
        monkey_seed = str(random.randrange(1, 1000))
        # 读取设备 id
        readDeviceId = list(os.popen('adb devices').readlines())
        # 正则表达式匹配出 id 信息
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        monkey_parameters = " --ignore-timeouts --pct-touch 40 --pct-trackball 40 --pct-appswitch 0  --pct-motion 20 -v -v  --throttle  200 100"
        shell_monkey = "shell monkey -p %s -s %s %s" % (self.package, monkey_seed, monkey_parameters)
        monkey_log = self.path + "\\monkey.log"
        adb_monkey = "adb  -s %s %s>%s" % (deviceId, shell_monkey,monkey_log)
        os.system(adb_monkey)

        print(monkey_log)


if __name__ == '__main__':
    unittest.main()

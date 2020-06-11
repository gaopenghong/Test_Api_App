import os
import random
import unittest

from common.appium_common.read_config import *


class MonkeyCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = '牛老幺'
        cls.package = read_package_name(cls.app)
        cls.activity = read_activity_name(cls.app)
        cls.path =r"D:\\PythonWorkSpace\\Test_Api_App\\demo\\report"
    def test_monkey(self):
        monkey_seed = str(random.randrange(1, 1000))

        monkey_parameters = " --ignore-timeouts --pct-touch 40 --pct-trackball 40 --pct-appswitch 0  --pct-motion 20 -v -v  --throttle  200 100"
        shell_monkey = "shell monkey -p %s -s %s %s" % (self.package, monkey_seed, monkey_parameters)
        monkey_log = self.path + r"\\log\\" + "monkey.log"
        adb_monkey="adb  %s > %s" % ( shell_monkey, str(monkey_log))
        os.popen(adb_monkey)

        print(adb_monkey)



if __name__ == '__main__':
    unittest.main()

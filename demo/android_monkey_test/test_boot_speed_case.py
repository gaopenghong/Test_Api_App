
import unittest

from common.appium_common.read_config import *
from common.appium_common.shell_adb import *


class TestBootSpeed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boot_times = 10

    def test_run_boot_test(self):

        cold_time = []
        hot_time = []
        # 读取设备 id
        read_device_id = list(os.popen('adb devices').readlines())

        # 正则表达式匹配出 id 信息
        device_id = re.findall(r'^\w*\b', read_device_id[1])[0]
        package = read_package_name('牛老幺')
        activity = read_activity_name('牛老幺')

        for i in range(self.boot_times):
            cold_time.append(get_cold_boot_time(package, activity))
            hot_time.append(get_hot_boot_time(package, activity, device_id))
        res_cold_time = 0
        res_hot_time = 0
        print("冷启动时间 = " + str(cold_time))
        print("热启动时间 = " + str(hot_time))
        for i in cold_time:
            res_cold_time = res_cold_time + i
        print('平均冷启动时间: ' + str(res_cold_time / self.boot_times) + ' ms')
        for i in hot_time:
            res_hot_time = res_hot_time + i
        print('平均热启动时间: ' + str(res_hot_time / self.boot_times) + ' ms')

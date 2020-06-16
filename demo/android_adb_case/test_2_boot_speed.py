from demo.appium_case.base_case import *

class TestBootSpeed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boot_times = 3

    @tag(Tag.BOOT_TIME)
    def test_run_boot(self):
        """冷启动和热启动的平均速度"""
        log.info('在执行测试用例：%s，file：%s，line：%s' % (get_function_name(), sys._getframe().f_code.co_filename,
                                                sys._getframe().f_lineno))

        cold_time = []
        hot_time = []
        # 读取设备 id
        read_device_id = list(os.popen('adb devices').readlines())

        # 正则表达式匹配出 id 信息
        device_id = re.findall(r'^\w*\b', read_device_id[1])[0]
        package = read_package_name(app_name_nly)
        activity = read_activity_name(app_name_nly)

        for i in range(self.boot_times):
            cold_time.append(get_cold_boot_time(package, activity))
            hot_time.append(get_hot_boot_time(package, activity, device_id))
        res_cold_time = 0
        res_hot_time = 0
        log.info("冷启动时间 = " + str(cold_time))
        log.info("热启动时间 = " + str(hot_time))
        for i in cold_time:
            res_cold_time = res_cold_time + i
        log.info('平均冷启动时间: ' + str(res_cold_time / self.boot_times) + ' ms')
        for i in hot_time:
            res_hot_time = res_hot_time + i
        log.info('平均热启动时间: ' + str(res_hot_time / self.boot_times) + ' ms')


if __name__ == '__main__':
    unittest.main()

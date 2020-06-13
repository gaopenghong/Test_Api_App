from demo.appium_case.base_case import *


class MonkeyCase(BaseCaseSetup):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.times = int(100)  # monkey执行时间次数


    @tag(Tag.MONKEY)
    def test_monkey_fast(self):
        """执行monkey测试，导出日志"""
        MonkeyShell(package_name_nly, self.times, monkey_log_path).monkey()
        log.info("开始执行monkey脚本，大约用时%s分钟" % str(self.times / 120))

    @tag(Tag.MONKEY)
    def test_monkey_slow(self):
        """执行monkey测试，导出日志"""
        MonkeyShell(package_name_nly, self.times, monkey_log_path).monkey()
        log.info("开始执行monkey脚本，大约用时%s分钟" % str(self.times / 120))


if __name__ == '__main__':
    unittest.main()

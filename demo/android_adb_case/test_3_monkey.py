import unittest
import warnings
from common.app_common.read_config import *
from common.app_common.shell_monkey_adb import MonkeyShell
from utx import *


class MonkeyCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.app = '牛老幺'
        cls.package = read_package_name(cls.app)  # 包名获取
        cls.path = "D:\\PythonWorkSpace\\Test_Api_App\\demo\\report"  # monkey日志存放路径
        cls.times = int(100)  # monkey执行时间次数

    @tag(Tag.MONKEY)
    def test_monkey(self):
        """执行monkey测试，导出日志"""
        MonkeyShell(self.package, self.times, self.path).monkey()
        log.info("开始执行monkey脚本，大约用时%s分钟"% str(self.times / 120))


if __name__ == '__main__':
    unittest.main()

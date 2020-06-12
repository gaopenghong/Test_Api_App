import os
import time
import unittest
from common.appium_common.read_config import *
from utx import *


class TestInstall(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = '牛老幺'
        cls.package = read_package_name(cls.app)
        cls.activity = read_activity_name(cls.app)
        cls.apk_path = r"D:\PythonWorkSpace\Test_Api_App\data\app-release.apk"

    @tag(Tag.INSTALL)
    def test_install_status(self):
        adb_monkey = """adb  shell  pm list packages | find "com.dtysp.niuly" """
        adb_monkey2 = """adb  shell  pm list packages | find "%s" """ % self.package
        status = os.popen(adb_monkey2).read()
        log.info(status)
        if status:
            adb = "adb   uninstall  %s" % self.package
            os.system(adb)
            log.info('开始卸载旧包')
        else:
            log.info("未安装旧包，可以直接安装新包哈哈")

    @tag(Tag.INSTALL)
    def test_install(self):
        """安装APP"""
        adb = "adb install  %s" % self.apk_path
        print(adb)
        r = os.system(adb)
        log.info("安装成功")
        return r

    @tag(Tag.INSTALL)
    def test_uninstall(self):
        """卸载APP"""
        time.sleep(5)
        adb = "adb   uninstall  %s" % self.package
        r = os.system(adb)
        log.info("卸载成功")
        return r

    @tag(Tag.INSTALL)
    def test_reinstall(self):
        """再次安装APP"""
        adb = "adb install  %s" % self.apk_path
        print(adb)
        r = os.system(adb)
        log.info("再次安装成功")
        return r


if __name__ == '__main__':
    unittest.main()

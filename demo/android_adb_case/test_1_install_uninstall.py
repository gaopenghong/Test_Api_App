import os
import time
import unittest
from common.app_common.read_config import *
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
        """查找是否已经安装此安装包,如果有的话删除旧包，如果没有安装就直接安装"""
        adb_monkey2 = """adb  shell  pm list packages | find "%s" """ % self.package # adb命令查看是否已经安装此包
        status = os.popen(adb_monkey2).read()
        log.info(status)
        if status:
            adb = "adb   uninstall  %s" % self.package
            os.system(adb)
            log.info('开始卸载旧包')
        else:
            log.info("未安装旧包，可以直接安装新包哈哈")

    @tag(Tag.INSTALL,Tag.SMOKE)
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

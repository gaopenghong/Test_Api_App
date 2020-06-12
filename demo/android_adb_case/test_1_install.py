import time
import unittest
from common.app_common.read_config import *
from common.app_common.shell_install_adb import InstallUninstall
from utx import *


class TestInstallUninstall(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = '牛老幺'
        cls.package = read_package_name(cls.app)
        cls.apk_path = r"D:\PythonWorkSpace\Test_Api_App\data\app-release.apk"

    @tag(Tag.INSTALL)
    def test_install_status(self):
        """查找是否已经安装此安装包,如果有的话删除旧包，如果没有安装就直接安装"""
        s = InstallUninstall().apk_install_status(self.package)
        if s:
            InstallUninstall().apk_uninstall(self)
            log.info("已安装旧包，开始删除旧安装包")
        else:
            log.info("未安装旧包，可以直接安装新包哈哈")

    @tag(Tag.INSTALL)
    def test_install(self):
        """安装APP"""
        InstallUninstall().apk_install(self.apk_path)
        log.info("安装成功")

    @tag(Tag.INSTALL)
    def test_uninstall(self):
        """卸载APP"""
        time.sleep(5)
        InstallUninstall().apk_uninstall(self.package)
        log.info("卸载成功")

    @tag(Tag.INSTALL)
    def test_reinstall(self):
        """再次安装APP"""
        InstallUninstall().apk_install(self.apk_path)
        log.info("再次安装成功")


if __name__ == '__main__':
    unittest.main()

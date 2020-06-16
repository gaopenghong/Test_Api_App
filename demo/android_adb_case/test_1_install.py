from demo.appium_case.base_case import *


class TestInstallUninstall(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass


    @tag(Tag.INSTALL)
    def test_install_status(self):
        """查找是否已经安装此安装包,如果有的话删除旧包，如果没有安装就直接安装"""
        s = InstallUninstall().apk_install_status(package_name_nly)
        if s:
            InstallUninstall().apk_uninstall(self)
            log.info("已安装旧包，开始删除旧安装包")
        else:
            log.info("未安装旧包，可以直接安装新包哈哈")

    @tag(Tag.INSTALL)
    def test_install(self):
        """安装APP"""
        re = InstallUninstall().apk_install(apk_path)
        print('安装成功的返回值为：'+re)
        log.info("安装中")

    @tag(Tag.INSTALL)
    def test_uninstall(self):
        """卸载APP"""
        time.sleep(5)
        InstallUninstall().apk_uninstall(package_name_nly)
        log.info("卸载中")

    @tag(Tag.INSTALL)
    def test_reinstall(self):
        """再次安装APP"""
        InstallUninstall().apk_install(apk_path)
        log.info("再次安装")




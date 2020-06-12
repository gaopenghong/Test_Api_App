import os
import time


class InstallUninstall():
    def apk_install_status(self,package):
        """
        功能查找是否已经安装此安装包
        package：包名
        apk_path：包存放路径
        """
        adb_monkey2 = """adb  shell  pm list packages | find "%s" """ % package  # adb命令查看是否已经安装此包
        status = os.popen(adb_monkey2).read()
        if status:
            return True
        else:
            return False

    def apk_install(self,apk_path):
        """
        功能安装APP
        package：包名
        apk_path：包存放路径
        """
        adb = "adb install  %s" % apk_path
        print(adb)
        os.system(adb)

    def apk_uninstall(self,package):
        """
       功能： 卸载APP
        package：包名
        apk_path：包存放路径
        """
        time.sleep(5)
        adb = "adb   uninstall  %s" % package
        os.system(adb)




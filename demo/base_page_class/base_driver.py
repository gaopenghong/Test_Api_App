from demo.my_test import *

class BaseDriver():

    def driver_begin(self,package_name,activity_name):
        """
        driver驱动启动
        """
        deviceName = os.popen('adb shell getprop ro.product.model').read()  # 获取设备名称
        log.info("测试设备为%s" % deviceName)
        # 读取设备系统版本号
        deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
        log.info("测试设备系统版本为%s" % deviceAndroidVersion)
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        # package_name = read_ini(ini_file_path=app_conf_path, name=app, value='appPackage')
        platformName = 'Android'
        desired_caps = {
            'platformName': platformName,
            'deviceName': deviceName,
            'platformVersion': deviceVersion,
            'appPackage': package_name,
            'appActivity': activity_name,
            'noReset': False,
            'resetKeyboard': False  # 将键盘给隐藏起来
            # 'unicodeKeyboard': True,# 使用unicodeKeyboard的编码方式来发送字符串
        }
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
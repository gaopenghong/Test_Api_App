from demo.my_test import *


class BasePageLogin():

    def login_base(self, driver, user_number, password):
        """登录base方法"""
        time.sleep(2)
        log.info("开始执行登录操作")
        log.info("----" * 15)
        inputting(driver=driver, type=id_type, section_name='登录页面', name='输入框', txt=user_number)
        log.info("输入账号")
        inputting(driver=driver, type=id_type, section_name='登录页面', name='密码', txt=password)
        log.info("输入密码")
        clicking(driver=driver, type=id_type, section_name='登录页面', name='登录按钮')
        log.info("点击登录")
        time.sleep(2)

    def skip_limits(self, driver):
        """跳过权限弹窗，允许"""
        log.info("操作权限弹窗")
        clicking(driver=driver, type=id_type, section_name='权限', name='允许')
        time.sleep(1)

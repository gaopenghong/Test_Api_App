from demo.my_test import *


class MonkeyCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.app = '牛老幺'
        cls.package = read_package_name(cls.app)  # 包名获取
        cls.path = "D:\\PythonWorkSpace\\Test_Api_App\\demo\\report"  # monkey日志存放路径
        cls.times = int(100)  # monkey执行时间次数
        cls.user_number = 18636299591
        cls.password = 123456
        cls.driver = driver_begin(cls.app)
        log.debug("初始化APP，测试数据初始化")
        time.sleep(1)
        log.info("开始执行登录操作")
        log.info("----" * 15)
        inputting(driver=cls.driver, type='id_type', section_name='登录页面', name='输入框', txt=cls.user_number)
        log.info("输入账号")
        inputting(driver=cls.driver, type='id_type', section_name='登录页面', name='密码', txt=cls.password)
        log.info("输入密码")
        clicking(driver=cls.driver, type='id_type', section_name='登录页面', name='登录按钮')
        log.info("点击登录")
        time.sleep(2)
        log.info("操作权限弹窗三次")
        for i in range(3):
            clicking(driver=cls.driver, type='id_type', section_name='权限', name='允许')
            time.sleep(1.5)

    @tag(Tag.MONKEY)
    def test_monkey_fast(self):
        """执行monkey测试，导出日志"""
        MonkeyShell(self.package, self.times, self.path).monkey()
        log.info("开始执行monkey脚本，大约用时%s分钟" % str(self.times / 120))

    @tag(Tag.MONKEY)
    def test_monkey_slow(self):
        """执行monkey测试，导出日志"""
        MonkeyShell(self.package, self.times, self.path).monkey()
        log.info("开始执行monkey脚本，大约用时%s分钟" % str(self.times / 120))


if __name__ == '__main__':
    unittest.main()

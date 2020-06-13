from demo.baseclass.basepage import *


class TestAbout(unittest.TestCase):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """

    @classmethod
    def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
        cls.driver = driver_begin(app_name_nly)
        log.debug("初始化APP，测试数据初始化")
        BasePage(driver=cls.driver).login_base(user_number=user_1,password=password)
        time.sleep(2)
        for i in range(3):
            BasePage(driver=cls.driver).skip_limits()

    @tag(Tag.UI_F2)
    def test_create_user_name(self):
        """修改昵称"""
        log.info("进入我的")
        clicking(driver=self.driver, type=id_type, section_name='导航', name='我的')
        log.info("进入我的个人信息")
        clicking(driver=self.driver, type=id_type, section_name='我的', name='个人信息')
        log.info("点击昵称进行修改")
        clicking(driver=self.driver, type=id_type, section_name='我的', name='昵称')
        log.info("返回")
        clicking(driver=self.driver, type=id_type, section_name='我的', name='返回')
        clicking(driver=self.driver, type=id_type, section_name='我的', name='返回')

    @tag(Tag.UI_F2)
    def test_send_massage(self):
        """发送消息给好友"""
        pass

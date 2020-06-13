from demo.baseclass.base_login_pageUI import *


class TestMessage(unittest.TestCase):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """

    @classmethod
    def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
        cls.driver = BasePage().driver_begin(app_name_nly)
        log.debug("初始化APP，测试数据初始化")

    @tag(Tag.UI_F1)
    def test_login(self):
        """测试登陆操作"""
        BasePage().login_base(driver=self.driver,user_number=user_1, password=password)

    @tag(Tag.UI_F1)
    def test_skip_limits(self):
        """第一次进入APP的权限弹窗"""
        for i in range(3):
            BasePage().skip_limits(driver=self.driver)


    @skip
    @tag(Tag.UI_F1)
    def test_send_massage(self):
        """发送消息给好友"""
        log.debug("进入通讯录")
        clicking(driver=self.driver, type=id_type, section_name='导航', name='通讯录')
        log.debug("找到李飞")
        clicking(driver=self.driver, type=xpath_type, section_name='通讯录', name='李飞')
        log.info("准备发送100条消息")
        clicking(driver=self.driver, type=id_type, section_name='好友', name='发送消息')
        for i in range(100):
            inputting(driver=self.driver, type=id_type, section_name='好友', name='消息输入框', txt='你好')
            clicking(driver=self.driver, type=id_type, section_name='好友', name='发送按钮')
            log.info("发送第" + str(i + 1) + "成功，发送消息内容“你好”")

    def test_111(self):
        print("ssssssssssssssssssssssssssssssss" * 100)

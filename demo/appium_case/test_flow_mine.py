from demo.appium_case.base_case import *


class TestMine(BaseCaseSetup):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """

    # @classmethod
    # def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
    #     cls.driver = BasePage().driver_begin(app_name_nly)
    #     log.debug("初始化APP，测试数据初始化")
    #     BasePage().login_base(driver=cls.driver,user_number=user_1,password=password)
    #     time.sleep(2)
    #     for i in range(3):
    #         BasePage().skip_limits(cls.driver)

    @tag(Tag.UI_F2)
    def test_create_user_name(self):
        """修改昵称"""
        self.u=BasePageMine()
        self.u.into_mine(self.driver)
        self.u.into_my_information(self.driver)
        self.u.user_name(self.driver)
        for  i in range(2):
            self.u.back(self.driver)



    @tag(Tag.UI_F2)
    def test_send_massage(self):
        """发送消息给好友"""
        pass

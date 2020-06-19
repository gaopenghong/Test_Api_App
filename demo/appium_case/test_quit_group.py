from demo.appium_case.base_case import *



class TestQuitGroup(BaseCaseSetup):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """

    @tag(Tag.UI_F4)
    def test_quit_groups(self):
        "发送消息测试"
        self.me = BasePageMessage()
        for i in range(4):
            self.me.into_book(self.driver)
            self.me.into_my_groups(self.driver)
            BasePageLimits().is_ele_do_it(driver=self.driver)
            self.me.into_group(self.driver,name='我的群第%s个'%str(i+1))
            BasePageLimits().is_ele_do_it(driver=self.driver)
            self.me.quit_group(self.driver)



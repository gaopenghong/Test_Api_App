from demo.appium_case.base_case import *


class TestMessage(BaseCaseSetup):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """
    @skip
    @tag(Tag.UI_F1)
    def test_chat_group(self):
        "发送消息测试"
        message = "为中华之崛起而读书"
        for i in range(500):
            message = message + "读书"

        me = BasePageMessage()
        me.into_chat_list(self.driver)
        BasePageLimits().is_ele_do_it(driver=self.driver)
        me.into_chat_group(self.driver)
        BasePageLimits().is_ele_do_it(driver=self.driver)
        for i in range(10):
            me.write(driver=self.driver, message=message)
            me.send(self.driver)
            log.info("第%s条消息发送成功" % int(i + 1))
    @skip
    @tag(Tag.UI_F1)
    def test_group_info(self):
        me = BasePageMessage()
        me.into_chat_list(self.driver)
        BasePageLimits().is_ele_do_it(driver=self.driver)
        me.into_chat_group(self.driver)
        clicking(driver=self.driver, type=id_type, section_name='群聊', name='群设置')
        mess = str("好" * 498)
        me.group_info(self.driver, message=mess)

    @tag(Tag.UI_F1)
    def test_biaoqian(self):
        me = BasePageMessage()
        me.into_book(self.driver)
        me.biaoqian(self.driver,3000)


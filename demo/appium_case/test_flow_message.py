from demo.appium_case.base_case import *
from demo.baseclass.base_message_pageUI import *


class TestMessage(BaseCaseSetup):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """

    @tag(Tag.UI_F1)
    def test_chat_group(self):
        "发送消息测试"
        message = "我爱中华"
        for i in range(200):
            message = message + "爱"
        me = BasePageMessage()
        me.into_chat_list(self.driver)
        me.into_chat_group(self.driver)
        for i in range(1000):
            me.write(driver=self.driver, message=message)
            me.send(self.driver)

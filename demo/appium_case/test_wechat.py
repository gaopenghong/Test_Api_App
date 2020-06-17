from demo.appium_case.base_case import *



class TestWx(BaseCaseSetupWx):

    @tag(Tag.UI_F3)
    def test_chat(self):
        """微信聊天"""
        self.u =WhChat()
        self.u.chat(driver=self.driver)

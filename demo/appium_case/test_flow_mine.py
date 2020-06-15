from demo.appium_case.base_case import *


class TestMine(BaseCaseSetup):

    @tag(Tag.UI_F2)
    def test_create_user_name(self):
        """修改昵称"""
        self.u = BasePageMine()
        self.u.into_mine(self.driver)
        self.u.into_my_information(self.driver)
        self.u.user_name(self.driver)
        for i in range(2):
            self.u.back(self.driver)

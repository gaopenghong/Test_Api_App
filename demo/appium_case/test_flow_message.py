from demo.appium_case.base_case import *


class TestMessage(BaseCaseSetup):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """






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

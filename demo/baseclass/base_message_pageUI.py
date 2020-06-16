from demo.my_test import *


class BasePageMessage():

    def into_chat_list(self, driver):
        "打开消息列表"
        time.sleep(1)
        log.info("打开消息列表")
        clicking(driver=driver, type=id_type, section_name='导航', name='消息')

    def into_chat_group(self, driver):
        "进入第一个群聊"
        log.info("输入列表里第一个群聊")
        clicking(driver=driver, type=xpath_type, section_name='消息', name='群聊第一个')

    def write(self, driver, message):
        "输入消息"
        time.sleep(2)
        inputting(driver=driver, type=id_type, section_name='好友', name='消息输入框', txt=message)
        log.info("输入消息")

    def send(self, driver):
        time.sleep(1)
        log.info("发送消息")
        clicking(driver=driver, type=id_type, section_name='好友', name='发送按钮')

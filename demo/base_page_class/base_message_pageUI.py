import string

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

    def into_book(self, driver):
        time.sleep(1)
        log.info("通讯录")
        clicking(driver=driver, type=id_type, section_name='导航', name='通讯录')

    def into_my_groups(self, driver):
        time.sleep(1)
        log.info("我的群组")
        clicking(driver=driver, type=xpath_type, section_name='通讯录', name='我的群组')

    def into_group(self, driver, name):
        clicking(driver=driver, type=xpath_type, section_name='通讯录', name=name)

    def quit_group(self, driver):
        """退出或解散群"""
        clicking(driver=driver, type=id_type, section_name='群聊', name='群设置')
        swipe_up(driver)
        clicking(driver=driver, type=id_type, section_name='群聊', name='退出群')
        clicking(driver=driver, type=id_type, section_name='群聊', name='确定退出')

    def group_info(self, driver, message):
        """群介绍"""
        clicking(driver=driver, type=id_type, section_name='群聊', name='群介绍')
        inputting(driver=driver, type=id_type, section_name='群聊', name='群介绍输入框', txt=message)
        clicking(driver=driver, type=id_type, section_name='群聊', name='群介绍确定')

    def biaoqian(self,driver,times,randomlength=5):

        clicking(driver=driver, type=id_type, section_name='通讯录', name='标签分组')
        for i in range(times):
            string.digits = '0123456789'
            string.ascii_letters = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
            str_list = random.sample(string.digits + string.ascii_letters, randomlength)
            random_str = ''.join(str_list)
            inputting(driver=driver, type=id_type, section_name='通讯录', name='标签分组输入', txt=random_str)
            clicking(driver=driver, type=id_type, section_name='通讯录', name='标签分组添加')
            driver,quit()





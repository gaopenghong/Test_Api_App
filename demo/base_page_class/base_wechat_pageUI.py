from demo.my_test import *


class  WhChat():
    def login(self,driver):
        clicking(driver=driver, type=id_type, section_name='微信', name='登录')
        inputting(driver=driver, type=id_type, section_name='微信', name='手机号',txt=18636299591)
        clicking(driver=driver, type=id_type, section_name='微信', name='下一步')
        clicking(driver=driver, type=id_type, section_name='微信', name='知道了')
        clicking(driver=driver, type=id_type, section_name='微信', name='确定')
        inputting(driver=driver, type=id_type, section_name='微信', name='密码',txt='gaibianziji666')
        clicking(driver=driver, type=id_type, section_name='微信', name='确定登录')
        time.sleep(3)






    def chat(self,driver):
        clicking(driver=driver, type=xpath_type, section_name='微信', name='第一个聊天')
        inputting(driver=driver,type=xpath_type,section_name='微信',name='输入框',txt="小兵真厉害")

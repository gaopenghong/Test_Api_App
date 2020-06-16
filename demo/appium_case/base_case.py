from demo.baseclass.base_login_pageUI import *
from demo.baseclass.base_mine_pageUI import *
from demo.baseclass.base_message_pageUI import *

class BaseCaseSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
        cls.driver = BasePage().driver_begin(app_name_nly)
        log.debug("初始化APP，测试数据初始化")
        BasePage().login_base(driver=cls.driver, user_number=user_1, password=password)
        for i in range(3):
            BasePage().skip_limits(cls.driver)


if __name__ == '__main__':
    pass

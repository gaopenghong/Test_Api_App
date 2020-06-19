from demo.base_page_class.base_driver import *
from demo.base_page_class.base_login_pageUI import *
from demo.base_page_class.base_mine_pageUI import *
from demo.base_page_class.base_message_pageUI import *
from demo.base_page_class.base_limits_action import *
from demo.base_page_class.base_wechat_pageUI import *

class BaseCaseSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
        cls.driver = BaseDriver().driver_begin(package_name=package_name_nly,activity_name=activity_name_nly)
        log.debug("初始化APP，测试数据初始化")
        BasePageLogin().login_base(driver=cls.driver, user_number=user_1, password=password)
        BasePageLimits().is_ele_do_it(driver=cls.driver)


class BaseCaseSetupWx(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
        cls.driver = BaseDriver().driver_begin(package_name=package_name_wx,activity_name=activity_name_wx)
        log.debug("初始化APP，测试数据初始化")


if __name__ == '__main__':
    pass

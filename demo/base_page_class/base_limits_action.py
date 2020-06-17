from demo.base_page_class.base_login_pageUI import BasePageLogin
from demo.my_test import *


class BasePageLimits():

    def skip_limits(self, driver):
        """跳过权限弹窗，允许"""
        log.info("操作权限弹窗")
        clicking(driver=driver, type=id_type, section_name='权限', name='允许')
        time.sleep(1)

    def is_ele_do_it(self, driver):
        """判断有没有元素，有的话就操作直到没有"""
        while True:
            is_not_is = is_element(driver=driver, ini_file_path=ele_id_conf_path, section_name='权限', name='允许')
            if is_not_is:
                BasePageLogin().skip_limits(driver)
            else:
                break

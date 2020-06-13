from common.app_common.element_action import *

# 用户信息
user_1 = read_ini(ini_file_path=load_file('parameter'), name='用户', value='user_1')
password = read_ini(ini_file_path=load_file('parameter'), name='用户', value='password')
# app信息
app_name_nly = read_ini(ini_file_path=load_file('app_conf'), name='牛老幺', value='appName')
package_name_nly = read_ini(ini_file_path=load_file('app_conf'), name='牛老幺', value='appPackage')
print(package_name_nly)

# 元素类型
id_type = 'id_type'
class_name_ini = 'class_name_ini'
location_type = 'location_type'
xpath_type = 'xpath_type'

#路径
apk_path = read_ini(ini_file_path=load_file('parameter'), name='路径', value='apk_path')
print(apk_path)


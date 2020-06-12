import os

def load_file(a):
    # 返回当前目录下目标文件的绝对文件路径
    id_ini_path = os.path.abspath(os.path.dirname(__file__))+"\id.ini"
    class_name_ini_path = os.path.abspath(os.path.dirname(__file__)) + "\class_name.ini"
    location_ini_path = os.path.abspath(os.path.dirname(__file__)) + "\location_ini.ini"
    x_path_ini_path = os.path.abspath(os.path.dirname(__file__)) +"\path.ini"
    app_ini_path=os.path.abspath(os.path.dirname(__file__)) +r"\appPadkage_appActivity.ini"
    parameter_ini_path=os.path.abspath(os.path.dirname(__file__)) +"\parameter.ini"
    dict_load = {
        'id_ini': id_ini_path,
        'class_name_ini':class_name_ini_path,
        'location_ini':location_ini_path,
        'xpath_ini':x_path_ini_path,
        'app_conf':app_ini_path,
        'parameter':parameter_ini_path
    }
    if a in dict_load.keys():
         print(dict_load[a])
         return dict_load[a]
# if __name__ == '__main__':
#     load_file('app_conf')




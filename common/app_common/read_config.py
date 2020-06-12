import configparser

from config.load_file import *


def read_ini(ini_file_path, name, value):  # 根据文件读取ini文件
    conf = configparser.ConfigParser()
    conf.read(ini_file_path, encoding="utf-8-sig")
    temp = conf.get(name, value)
    return temp


def read_package_name(app, ini_type='app_conf'):
    package_name = read_ini(ini_file_path=load_file(ini_type), name=app, value='appPackage')
    return  package_name

def read_activity_name(app, ini_type='app_conf'):
    activity_name = read_ini(ini_file_path=load_file(ini_type), name=app, value='appActivity')
    return activity_name

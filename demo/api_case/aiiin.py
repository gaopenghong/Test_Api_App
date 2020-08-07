# —*- coding:utf-8 -*-
# Created by Administrator on 2020/8/6
# Copyright (C) 2020 $USER.All rights reserved.
f = "D:\PythonWorkSpace\data\owner"
def make_owner(floor):
    number = 1
    with open(f, "a+") as file:
        file.write("\n")
    while number < 21:
        if number < 10:
            owner = "18-%s0%s" % (floor, number)
            with open(f, "a+") as file:
                file.write(owner + "    ")
            number = number + 1
        else:
            owner = "18-%s%s" % (floor, number)
            with open(f, "a+") as file:
                file.write(owner + "    ")
            number = number + 1
if __name__ == '__main__':
    list=[x for x in range(10) if x/2>1]
    print(list)



#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/19 17:40
# author:wangshuai

# import os
#
# basePath = "F:/VPS"
#
# folder = os.listdir(basePath)
#
# print(type(folder))
# print(folder)



import os
path = r'C:\Users\HP\Desktop\搜索引擎文件遍历'
for dirpath,dirnames,filenames in os.walk(path):
    print(dirpath, dirnames, filenames)
    print(dirpath+'\小米科技.txt')

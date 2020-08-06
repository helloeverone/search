#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/26 17:20
# author:wangshuai

import jieba

file_object2 = open(r'C:\Users\HP\Desktop\搜索引擎文件遍历\锤子科技.txt', 'r')
list2 = str(file_object2.read())


seg_list = jieba.cut_for_search(list2)
print("【搜索引擎模式】：", " ," .join(seg_list))

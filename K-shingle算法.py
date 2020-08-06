#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/19 16:45
# author:wangshuai
import os
import jieba
def getShingle(s, k):
    dic = dict()
    for i in range(0, len(s) - k + 1):
        s1 = s[i:i + k]  # 拆分词
        j = dic.get(s1)
        if j:
            dic[s1] +=1
        else:
            dic[s1] = 1
    # print(dic)

# getShingle('我在重庆理工大学上学', 1)


def getSimilarity(s1, s2, k):
    if s1 == s2:
        return 1
    set1 = set()
    set2 = set()
    profile1 = getShingle(s1, k)
    profile2 = getShingle(s2, k)

    for i in profile1.keys():
        set1.add(i)  # 加入到set中
    for i in profile2.keys():
        set2.add(i)  # 加入到set中
    print("相似度为:",1.0 * len(set1 & set2) / len(set1 | set2))
    inter = len(profile1.keys()) + len(profile2.keys()) - len(set1)
    # print(sorted(set(s1).union(s2)))
    print("重复文字如下:",set2)
    # for i in list(set2):
    #
    #     info = i
    #     f = list1
    #     count = 0
    #     for line in f:
    #         # print(line)
    #         line = line.strip('\n').split()
    #         if info in line:
    #             line = ["\033[31m %s \033[0m" % info if i == info else i for i in line]
    #             for i in line:
    #                 print(i),
    #             # print('\n')
    #             count += 1
        # if count == 0:
        #     print('the info is not exists in your txt')
        # else:
        #     print('match %d lines' % (count))

path = r'C:\Users\HP\Desktop\搜索引擎文件遍历'
for dirpath,dirnames,filenames in os.walk(path):
    # print(dirpath, dirnames, filenames)

    file_object1=open(dirpath+'\小米科技.txt','r')
    list1 = str(file_object1.read().split('\n'))

    file_object2=open(r'C:\Users\HP\Desktop\搜索引擎文件遍历\锤子科技.txt','r')
    list2 = str(file_object2.read().split('\n'))
    getSimilarity(list1, list2, 1)
# print(list1)

# getSimilarity(list1,list2,1)











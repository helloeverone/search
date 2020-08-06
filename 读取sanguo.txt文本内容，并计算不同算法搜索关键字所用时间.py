#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/19 0:37
# author:wangshuai

# -*- coding:utf-8 -*-
# !/usr/bin/python
import time
import datetime
def Index(s1, s2, count=0):
    i = count
    j = 0
    while (i < len(s1) and j < len(s2)):
        if (s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if (j >= len(s2)):
        return i - len(s2)
    else:
        return 'none'


def Index_KMP(s1, s2, pos):
    next = get_next(s2)
    i = pos
    j = 0
    while (i < len(s1) and j < len(s2)):
        if (j == -1 or s1[i] == s2[j]):
            i += 1
            j += 1
        else:
            j = next[j]

    if (j >= len(s2)):
        return i - len(s2)
    else:
        return 'none'

def get_next(s2):
    i = 0
    next = [-1]
    j = -1
    while (i < len(s2) - 1):
        if (j == -1 or s2[i] == s2[j]):
            i += 1
            j += 1
            next.append(j)
        else:
            j = next[j]
    return next
def printcolor(printlist, str1, str2):
    printlist2 = [0]
    for i in printlist:
        printlist2.append(i + len(str2))
    for j in range(len(printlist)):
        s3 = str1[printlist2[j]:printlist[j]]
        print(s3, end='')
        print("\033[1;30;41m%s\033[0m" % s2, end='')
    s4 = str1[printlist[-1] + len(str2):]
    print(s4, end='')


if __name__ == "__main__":
    with open('sanguo.txt', 'r') as f:
        s1 = f.read()
    s2 = "重庆理工大学"
    location = 0
    locationlist = []
    while location < len(s1):
        oldtime2 = datetime.datetime.now()
        location = Index(s1, s2)
        newtime2 = datetime.datetime.now()
        microtime2 = (newtime2 - oldtime2).microseconds
        print(' 本次BF算法花费时间：' + str(microtime2) + '微秒')
        oldtime = datetime.datetime.now()
        location = Index_KMP(s1, s2, int(location))
        newtime = datetime.datetime.now()
        microtime = (newtime - oldtime).microseconds
        print('本次KMP算法花费时间：' + str(microtime) + '微秒')
        # location = Index(s1, s2, location)
        if location == 'none':
            break
        else:
            print('查找到的字符串所在位置：' + str(location))
            input("enter继续查找(查找成功即显示结果)-->：")
            locationlist.append(location)
            location = location + 1





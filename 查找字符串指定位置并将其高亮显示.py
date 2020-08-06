#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/14 22:47
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
    s1 = """
北京小米科技有限责任公司成立于2010年3月3日，是一家专注于智能硬件和电子产品研发的移动互联网公司，同时也是一家专注于高端智能手机、互联网电视以及智能家居生态链建设的创新型科技企业。小米公司创造了用互联网模式开发手机操作系统、发烧友参与开发改进的模式。小米还是继苹果、三星、华为之后第四家拥有手机芯片自研能力的科技公司。2018年7月9日在香港交易所主板挂牌上市，成为港交所上市制度改革后首家采用不同投票权架构的上市企业
“为发烧而生”是小米的产品概念。“让每个人都能享受科技的乐趣”是小米公司的愿景。小米公司应用了互联网开发模式开发产品的模式，用极客精神做产品，用互联网模式干掉中间环节，致力让全球每个人，都能享用来自中国的优质科技产品。
小米已经建成了全球最大消费类IoT物联网平台，连接超过1亿台智能设备，MIUI月活跃用户达到2.42亿 。小米系投资的公司接近400家，覆盖智能硬件、生活消费用品、教育、游戏、社交网络、文化娱乐、医疗健康、汽车交通、金融等领域。
2019年6月，小米科技入选2019福布斯中国最具创新力企业榜。2019年7月，2019世界500强排行榜发布，小米排名468位 。2019年10月，2019福布斯全球数字经济100强榜发布，小米位列第56位。
    """
    s2 = "小米科技"
    location = 0
    locationlist = []
    while location < len(s1):
        location = Index_KMP(s1, s2, location)
        # location = Index(s1, s2, location)
        if location == 'none':
            break
        else:
            print('查找到的字符串所在位置：' + str(location))
            input("enter继续查找(查找成功即显示结果)-->：")
            locationlist.append(location)
            location = location + 1
    print('')
    print('#' * 50)
    print('#' * 50)
    print('查找到的结果数组：' + str(locationlist))
    print('查找到的结果高亮显示：')
    printcolor(locationlist, s1, s2)
    print('')
    print('#' * 50)
    print('#' * 50)

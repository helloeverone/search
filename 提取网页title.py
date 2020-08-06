#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/19 1:29
# author:wangshuai


import os
from bs4 import BeautifulSoup
import requests
def requ(url):
    """提取网页内容"""
    resq = requests.get(url)
    resq.encoding = 'utf-8'
    content = resq.text
    return content
con = (requ("http://tieba.baidu.com/p/6343172376?red_tag=x2051452134"))

def get_title(cont):
    soup = BeautifulSoup(cont,'html.parser')
    te = soup.find('title')
    return te

path = "F:\python项目\爬虫title"
if not os.path.isdir(path):
    # print("meiyou")
    os.makedirs(path)
# print (os.getcwd())
title = get_title(con)
# print(title)
f_title = open('F:\\python项目\\爬虫title\\title.txt', 'w')
f_title.write(str(title))
print(get_title(con))
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/19 2:13
# author:wangshuai


from bs4 import BeautifulSoup
import os
import requests
def requ(url):
    resq = requests.get(url)
    resq.encoding = 'utf-8'
    content = resq.text
    return content
aa = requ("http://tieba.baidu.com/p/6343564511?red_tag=n2718034719")
def extract_a_label(content):
    """提取网页子链接"""
    soup = BeautifulSoup(content,'html.parser')
    alink = soup.find_all('a')
    return alink
print(extract_a_label(aa))

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/18 14:39
# author:wangshuai

import requests
def requ(url):
    """提取网页内容"""
    resq = requests.get(url)
    resq.encoding = 'utf-8'
    content = resq.text
    return content
print(requ("http://tieba.baidu.com/p/6343564511?red_tag=n2718034719"))
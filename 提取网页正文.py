#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/18 20:05
# author:wangshuai


import requests
import re
def requ(url):
    """提取网页内容"""
    resq = requests.get(url)
    resq.encoding = 'utf-8'
    content = resq.text
    return content
aa = (requ("http://tieba.baidu.com/p/6343564511?red_tag=n2718034719"))

def remove_empty_line(content):
    r = re.compile(r'''^\s+$''', re.M | re.S)
    s = r.sub('', content)
    r = re.compile(r'''\n+''', re.M | re.S)
    s = r.sub('\n', s)
    return s

bb = remove_empty_line(aa)

def remove_js_css(content):
    r = re.compile(r'''<script.*?</script>''', re.I | re.M | re.S)
    s = r.sub('', content)
    r = re.compile(r'''<style.*?</style>''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<!--.*?-->''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<meta.*?>''', re.I | re.M | re.S)
    s = r.sub('', s)
    r = re.compile(r'''<ins.*?</ins>''', re.I | re.M | re.S)
    s = r.sub('', s)
    return s

cc = remove_js_css(bb)
def remove_any_tag(s):
    s = re.sub(r'''<[^>]+>''', '', s)
    return s.strip()
dd = remove_any_tag(cc)
def extract_text(content):
    s = remove_empty_line(remove_js_css(content))
    s = remove_any_tag(s)
    s = remove_empty_line(s)
    return s
ff = extract_text(dd)
print(ff)
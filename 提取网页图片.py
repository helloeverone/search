#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/18 20:17
# author:wangshuai

import re
import urllib
import requests
import os
url = "http://tieba.baidu.com/f?kw=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6&red_tag=m1231290973"
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')

def getImg(html):
    reg = r'http:\/\/[^\s,"]*\.jpg'
    img_reg = re.compile(reg)
    img_list = re.findall(img_reg, html)
    print(img_list)
    x = 0
    path = 'D:\\test\\img'
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path+'\\'
    for imgurl in img_list:
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))
        x = x + 1
    return img_list
getImg(getHtml(url))







# import datetime
# import os
# import re
# from urllib import request
#
#
# class ImageCrawler(object):
#
#     @staticmethod
#     def get_url(url):
#         # 赋值一个headers，将程序访问网站伪装成浏览器，以防止被禁止访问
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
#         }
#         url = request.Request(url, headers=headers)
#         # 打开网页，并读取网页源码
#         target_html = request.urlopen(url)
#         html_content = target_html.read()
#         # 此处需要注意:返回值是bytes类型时，要将其转换成utf-8才能正常显示在python程序中
#         html_content = html_content.decode('utf-8', "ignore")
#         return html_content
#
#     @staticmethod
#     def get_img(target_html):
#         # 从网页源码中，通过正泽匹配出jpg格式的url链接
#         reg = r'http:\/\/[^\s,"]*\.jpg'
#         img_reg = re.compile(reg)
#         img_list = re.findall(img_reg, target_html)
#         return img_list
#
#     @staticmethod
#     def save_img(target_img_list):
#         # 将获取到的图片链接保存到当前文件所在本地目录
#         file_dir = os.getcwd()
#         file_path = os.path.join(file_dir, 'downlosd_image')
#         check_exists = os.path.exists(file_path)
#         if not check_exists:
#             os.makedirs(file_path)
#         count_num = 0
#         for img in target_img_list:
#             count_num = count_num + 1
#             now_time = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
#             image_name = r"{0}\{1}_image_{2}.jpg".format(file_path, now_time, count_num)
#             request.urlretrieve(img, image_name)
#             print("Save image:{0}".format(image_name))
#
#
# if __name__ == '__main__':
#     imageCrawler = ImageCrawler()
#     # 获取被爬取网页信息
#     test_target_html = imageCrawler.get_url("http://tieba.baidu.com/f?kw=%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6&red_tag=m1231290973")
#     # 获取图片
#     test_img_list= imageCrawler.get_img(test_target_html)
#     # 保存图片到本地
#     imageCrawler.save_img(test_img_list)





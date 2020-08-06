#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/28 16:23
# author:wangshuai

f = open(r"C:\Users\HP\Desktop\搜索引擎文件遍历\yiduanwenben.txt","r")
str = f.read()
print(str)
f.close()
max_size=5
dict = set()
file = open(r'C:\Users\HP\Desktop\搜索引擎文件遍历\cidian.txt', 'r')
for line in file:
    def get_str_btw(s, f, b):
        par = s.partition(f)
        return (par[2].partition(b))[0][:]
    aa = get_str_btw(line, "【", "】")

    dict.add(aa)
# print(dict)

def max_math_segment(line, dic):
    chars = line
    words = []
    idx = 0
    while idx < len(chars):
        matched = False
        for i in range(max_size, 0, -1):
            cand = chars[idx:idx + i]
            if cand in dic:
                words.append(cand)
                matched = True
                break
        if not matched:
            i = 1
            words.append(chars[idx])
        idx += i
    return words
print("")

print("'\033[7;31m该段文本分词后的结果为：'",max_math_segment(str,dict))














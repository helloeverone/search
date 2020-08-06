#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/18 23:11
# author:wangshuai


def not_n(s):
    if s[-1]=="\n":
        return s[:len(s)-1]
    else:
        return s
def getindex(findlist,str1,str2,i):
    if i < len(str2)-len(str1):
        k = str2.index(str1,i)
        findlist.append(k)
        return getindex(str1,str2,k+1)
    else:
        return findlist

def not_empty(s):
    return s and s.strip()

def sp(line):
    line = line.split(" ")
    line = list(filter(not_empty, line))
    line[-1] = not_n(line[-1])
    return line

def extract_content():
    file = open("1.txt", "r")
    content1 = file.readlines()
    file.close()
    file = open("1.txt", "r")
    content = file.readlines()
    i = 0
    while i < len(content):
        content[i] = sp(content[i])
        #print(content[i])
        i = i + 1
    file.close()
    return (content,content1)

s = 'is'
mylist = []
mylist2 = []
myset = set()
findlist = []
(getcontent,getcontent1) = extract_content()
for m in range(0,len(getcontent)):
    for n in range(len(getcontent[m])):
        s = getcontent[m][n]
        mylist = []
        myset = set()
        for i in range(0,len(getcontent)):
            count = getcontent[i].count(s)
            #print(count)
            if count != 0:
                for j in range(count):
                    k = getcontent1[i].index(s)
                    #k = getindex(findlist,getcontent1[i],s,i=0)
                    mylist.append(s)
                    if (i+1,k+1) not in mylist:
                        myset.add((i+1, k+1))
        if myset != set([]):
            mylist2.append([s, myset])
mylist3 = []

for i in mylist2:
    if i not in mylist3:
        mylist3.append(i)
for i in mylist3:
    print(i[0],end='')
    for q in i[1:]:
        pass
        print(q)

def getindex(str1,str2,i):
    k = str2.index(str1,i)
    print()
    return getindex(str1,str2,k)

def printcolor(printlist,str1,str2):
    printlist2 = [0]
    for i in printlist:
        printlist2.append(i+len(str2))
    for j in range(len(printlist)):
        s3 = str1[printlist2[j]:printlist[j]]
        print(s3,end='')
        print("\033[1;30;41m%s\033[0m" % str2, end='')
    s4 = str1[printlist[-1]+len(str2):]
    print(s4, end='')

s = 'are'
sortlist = []
rowlist = []
for k in mylist3:
    for i in k[1:]:
        newlist = list(i)
        newlist.sort(key=lambda elem: elem[0])
        if k[0] == s:
            print(newlist)
            for n in newlist:
                rowlist.append(n[0])
            print(rowlist)
            for m in range(len(getcontent1)):
                if m+1 not in rowlist:
                    print(getcontent1[m], end='')
                else:
                    templist = []
                    templist.append(newlist[rowlist.index(m+1)][1]-1)
                    printcolor(templist, getcontent1[m], s)

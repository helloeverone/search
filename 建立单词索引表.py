#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/11/18 23:46
# author:wangshuai

index={}
word=['so']
with open('2.txt','r') as f:
    lines=f.readlines()
    l=0
    for line in lines:
        line=line.split(' ')
        for s in range(len(line)):
            if(s==len(line)-1 and l!=len(lines)-1):
                line[s]=line[s][0:len(line[s])-1]
            if(line[s] in index):
                index[line[s]].append([l,s])
            else:
                index[line[s]]=[[l,s]]
        l+=1
file=open('2.txt','r')
lines=file.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].split(' ')
for w in word:
    if(w in index):
        for i in index[w]:
            lines[i[0]][i[1]]='\033[95m'+lines[i[0]][i[1]]+'\033[0m'
for line in lines:
    print(' '.join(line))
file.close()


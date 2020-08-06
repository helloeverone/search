#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2019/12/16 18:00
# author:wangshuai
import numpy as np

M = [[0, 1 / 2, 0, 1 / 2],
     [1 / 3, 0, 0, 1 / 2],
     [1 / 3, 1 / 2, 1, 0],
     [1 / 3, 0, 0, 0]]
U = [1 / 4, 1 / 4, 1 / 4, 1 / 4]
U0 = np.array(U)

U_past_none_alpha = []
while True:
    U = np.dot(M, U)
    # print('Un: ', U)
    if str(U) == str(U_past_none_alpha):
        break
    U_past_none_alpha = U
print('Un converge1 to: ', U)

U_past_has_alpha = []
while True:
    U = 0.8 * (np.dot(M, U)) + 0.2 * U0
    # print('Un: ', U)
    if str(U) == str(U_past_has_alpha):
        break
    U_past_has_alpha = U
print('Un converge2 to: ', U)

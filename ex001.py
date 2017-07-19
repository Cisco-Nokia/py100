#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

list1 = [1, 2, 3, 4]
result = []
count = 0
for i in list1:
    for j in list1:
        for k in list1:
            if i != j and j !=k and k != i:
                count += 1
                print(i, j, k)

print(u'总共有%d个这样的数字。' % (count))
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""


a = int(input("输入第一个数字："))
b = int(input("输入第二个数字："))
c = int(input("输入第三个数字："))

user_input = (a, b, c)
result = sorted(user_input)
print(result)



#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
闰年需要同时满足以下条件：
1、年份能被4整除；
2、年份若是 100 的整数倍的话需被400整除，否则是平年。
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天
"""


year = int(input("输入年份："))
month = int(input("输入月份："))
day = int(input("输入日份："))

leap_year = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
normal_year = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def get_day():
    pass

result = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 == 0)):
    for i in range(month-1):
        result += leap_year[i]
else:
    for i in range(month-1):
        result += normal_year[i]
result = result + day
print(result)

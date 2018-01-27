# -*- coding:utf-8 -*-
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records.
"""
# 定义一个空集合，用于存储电话号码
phone = set()
def count_phone(list_data):
    """
    该函数用于将传入的列表的电话号码添加到集合中
    list_data:参数为列表
    """
    for number in list_data:
        phone.add(number[0])
        phone.add(number[1])

# 调用函数，传入短信和通话记录两个列表
count_phone(texts)
count_phone(calls)

# 输出集合中共有多少个电话号码
print("There are {} different telephone numbers in the records.".
    format(len(phone)))





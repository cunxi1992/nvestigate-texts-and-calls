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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""


def add_phone_list(phone_list,index):
    """
    该函数用于，将一个列表中的元素，去重后 添加到另一个列表中
    ：param phone_list:要处理的列表， 这里分别指的是电话列表calls、短信列表texts
    ：param index：要被处理列表的索引，这里指具体的某一列，如calls列表的第一、二列、texts列表的第一、二列
    ：return：返回一个list
    """
    phone_numbers_list = []
    for temp in range(len(phone_list)):
        if phone_list[temp][index] not in phone_numbers_list:
            phone_numbers_list.append(phone_list[temp][index])

    return phone_numbers_list

# 拨打的电话列表
phone_numbers = add_phone_list(calls,0)
# 被拨打的电话列表
numbers = add_phone_list(calls,1) + add_phone_list(texts,0) + add_phone_list(texts,1)
# 存储用于推销的电话号码
advertisement_phone = []
# 如果拨打电话列表中的电话不在被拨打、发短信、接受短信电话列表中，则该号码是用于推销的电话号码
for phone in range(len(phone_numbers)):
    if phone_numbers[phone] not in numbers:
        advertisement_phone.append(phone_numbers[phone])

print("These numbers could be telemarketers: ")
advertisement_phone.sort()
for phone in advertisement_phone:
    print(phone)





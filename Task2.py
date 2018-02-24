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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""


def get_dictionary(list_call):
    """
    该函数用于将传入的参数列表生成一个字典，并返回
    list_call:参数为一个列表
    """
    call_times = {}
    for list_data in list_call:
        if list_data[0] not in call_times:
            # 读取的文件内容均是字符串，因此需要使用int()将其转换为数字
            call_times[list_data[0]] = int(list_data[3])
        else:
            call_times[list_data[0]] += int(list_data[3])

    for list_data in list_call:
        if list_data[1] not in call_times:
            call_times[list_data[1]] = int(list_data[3])
        else:
            call_times[list_data[1]] += int(list_data[3])

    return call_times

# 调用函数
call_times = get_dictionary(calls)

# 获取字典中最大值对应的键
number_key = max(call_times,key = call_times.get)

# 输出哪一个电话号码通话时长最长，且最长时长是多少
print ("{0} spent the longest time,{1} seconds, on the phone during September 2016.".format(number_key,call_times[number_key]))

# # 利用列表生成式将通话时长生成列表
# times = [value for value in call_times.values()]

# # 计算最长的通话时长是多少
# max_times = max(times)

# # 将原有字典的键和值互换生成新的字典，以便直接获取最大通话时长的电话号码
# new_dict = {v:k for k,v in call_times.items()}

# # 通话时长最长的电话号码
# phone_number = new_dict[max_times]

# # 输出哪一个电话号码通话时长最长，且最长时长是多少
# print ("{0} spent the longest time,{1} seconds, on the phone during September 2016.".format(phone_number,max_times))







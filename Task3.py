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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""


# 被班加罗尔地区的固定电话所拨打的电话总数
total_phone_numbers = 0
# 由班加罗尔地区的固定电话拨打到班加罗尔地区的电话总数
ban_phone_numbers = 0

def called_phone_symbol(phone,phonelist):
    """
    该函数用于，将传入的参数phone加入到列表phonelist中
    """
    if phone not in phonelist:
        phonelist.append(phone)

# 定义一个空列表，用于存储被拨打的号码代号
called_phone_list = []

for call in calls:
    # 找出被班加罗尔地区的固定电话所拨打的所有电话
    # find()函数返回包含指定子字符串开始的索引值，若不存在则返回-1
    if call[0].find('(080)') == 0:
        if call[1].find('(') == 0:
            # 若被叫号码是以'('开头，则获取以')'结束的索引值+1
            end_index = call[1].find(')') + 1
            # 调用函数，将被拨打电话的代号加入到指定列表中
            called_phone_symbol(call[1][0:end_index],called_phone_list)
            # 计算被班加罗尔地区的固定电话所拨打的电话总数
            total_phone_numbers += 1
            # 计算由班加罗尔地区的固定电话拨打到班加罗尔地区的电话总数
            if call[1].find('080') == 0:
                ban_phone_numbers += 1
        # 判断被拨打号码的前缀是否为7、8、9，若是，则将其添加到指定列表中
        elif call[1][0] in ['7','8','9']:
            called_phone_symbol(call[1][0:4],called_phone_list)
            # 计算被班加罗尔地区的固定电话所拨打的电话总数
            total_phone_numbers += 1

# 对列表元素进行永久性排序
called_phone_list.sort()

# **** 第一部分 ****
# 输出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）
print("The numbers called by people in Bangalore have codes:")
for phone in called_phone_list:
    print(phone)


# ****  第二部分  ****
# 计算由班加罗尔固话打往班加罗尔的电话所占比例是多少
percent = ban_phone_numbers / total_phone_numbers * 100
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))








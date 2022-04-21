'''
判断字符串a="welcome to my world" 是否包含单词b="world"

包含返回True，不包含返回 False
'''


a = 'welcome to my world'
b = 'world'

#1逻辑运算
print(b in a)

#2index查找

#3find

'''
find(str, beg=0, end=len(string))
检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
'''

if a.find(b) == -1:
    print(False)
else:
    print(True)

print(False if a.find(b) == -1 else True)
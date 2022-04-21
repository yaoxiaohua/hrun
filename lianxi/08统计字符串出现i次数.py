'''
统计字符串“Hello, welcome to my world.” 中字母w出现的次数
统计单词 my 出现的次数
'''


a = "Hello, welcome to my world."
print(a.count('w'))

print(a.count('my'))

#添加起始位置
print(a.count('w',5,10))
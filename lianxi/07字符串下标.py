'''
找出单词 “welcome” 在 字符串“Hello, welcome to my world.” 中出现的位置，找不到返回-1

从下标0开始索引
'''


a = "Hello, welcome to my world."

#索引
print(a.index('w'))     #查找w所在位置

print(a.index('world'))

print(a.index('e'))
print(a.index('e',6,10))    #指定开始和结束位置

#找不到返回-1
b = input('查找:')
if b in a:
    print(a.index(b))
else:
    print('没找到给-1')



#三元表达式
print(a.index(b) if b in a else -1)
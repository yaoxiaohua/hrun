'''
如何判断一个字符串是不是纯数字组成
'''


a = '123456'
b = 'abc'

print(int(a))
print(type(a))
print(type(int(a)))


c = 123
d = 1.63

print(int(c),int(d))

e = input()
try:
    print(int(e))
except:
    print('异常')

#判断是否为纯数字，是TURE不是False
print(e.isdigit())
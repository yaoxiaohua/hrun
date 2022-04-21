
'''
已知 a 的值为 "hello"，b 的值为 "world"，如何交换 a 和 b 的值？
得到 a 的值为 "world"，b 的值为 "hello"
'''

a = "hello"
b = "world"


# 中间值，通用
temp = a
a = b
b = temp

print(a,b)

# python
a,b = b,a

print(a,b)
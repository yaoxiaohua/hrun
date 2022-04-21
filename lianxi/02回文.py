
'''
回文的定义： "回文"就是正读倒读都一样的。

如奇数个： "98789" ，这个数字正读是"98789" 倒读也是"98789"。
偶数个数字"3223"也是回文数。

字母 "abcba" 也是回文。


判断一个字符串是否是回文字符串，是打印True， 不是打印False
'''

a = "abcba"


#1.切片  前闭后开
# 范围
print(a[:4:])

# 步长
print(a[:4:2])

# 反转
print(a[::-1])

# 判断
print(a == a[::-1])


#2.reversed：将其元素从后向前颠倒构建成一个新的迭代器
b = reversed(a)   #reversed   object 迭代器  next()
print(b)
# for c in b:
#     print(c)
# print("".join(b))
print(a == "".join(b))


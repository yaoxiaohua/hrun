'''
s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
'''


s = "ajldjlajfdljfddd"
s1 = []


# 去重
for i in s:
    if i not in s1:
        s1.append(i)
print(s1)

# 排序
print(sorted(s1))
print(''.join(s1))      #转字符串



# 集合 1.无序  2.不重复
b = {}      #不能直接定义集合，要用set函数
print(type(b))


c = set(s)
print(type(c))
print(c)
print(sorted(c))
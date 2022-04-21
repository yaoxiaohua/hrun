'''
s = "ajldjlajfdljfddd"，去重保留原来的顺序，输出"ajldf"
'''


s = "ajldjlajfdljfddd"
s1 = []
for i in s:
    if i not in s1:
        s1.append(i)
print(s1)


#集合
s2 = set(s)
print(sorted(s2))
print(sorted(s2,reverse = True))    #降序排序
print(sorted(s2,key=lambda x:s.index(x)))   #按照x排序,x=索引下标（s.index(x)）
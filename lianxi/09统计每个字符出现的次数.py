'''
输入一个字符串 str, 输出第 m 个只出现过 n 次的字符，如在字符串 gbgkkdehh 中,
找出第2个只出现1 次的字符，输出结果：d


解决思路：

利用 collections 库的 Counter方法统计字符串每个单词出现的次数
'''


from collections import Counter

a = 'gbgkkdehh'
b = Counter(a)  #统计
print(b)
print(dict(b))

s = []
for i, j in dict(b).items():
    print('字母%s出现了%s次' %(i,j))
    if j == 1:
        s.append(i)
print(s[1])




#列表推导式

print([i for i, j in dict(b).items() if j == 1][1])
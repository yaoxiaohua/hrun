'''
把字符串 s 中的每个空格替换成"%20"

输入：s = "We are happy."
输出："We%20are%20happy."
'''

s = "We are happy."

print(s.replace(' ','%20'))


# 只替换第一个(替换次数)
print(s.replace(' ','%20',1))


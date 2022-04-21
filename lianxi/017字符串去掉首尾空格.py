'''
将字符串 a = "  welcome to my world   "首尾空格去掉
'''


a = "  welcome to my world   "
b = "@@@welcome to my world@@@@@@@@"


#去首尾空格
print(a.strip())
print(b.strip('@'))


#去左边的
print(b.lstrip('@'))

#去右边的
print(b.rstrip('@'))
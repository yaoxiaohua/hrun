'''
给定一个数a，判断一个数字是否为奇数或偶数
'''



a = 5
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)      #2.7整数除整数只能得到整数 3.6可得到浮点数
print(a%b)
print(a//b)
print(a**b)



print('偶数' if a % b == 0 else '奇数')
print('奇数' if a % b else '偶数')  #0 为Fasle 非0 为Ture
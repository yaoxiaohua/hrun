'''
菱形
'''



s = 14                              #总行数
s2 = int((s+1)/2)                   #一半的行数
num = [2*i+1 for i in range(s2)]    #一半行数的每行个数
num = num+num[len(num)-2::-1]       #全部行数的每行个数
for i in num:
    print((s-i)//2*' ',i*'*')




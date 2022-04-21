'''
九九乘法表
'''


a = range(10)
print(a)
for i in range(1,10):
    # print(i)    #行数
    print('')
    # print('\n')  #print本身自带换行
    for j in range(1,i+1):
        print('%s * %s = %-2s' %(j, i, i*j),end=' ')     #%-2s  -代表左对齐  2代表两个占位符

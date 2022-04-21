'''
有个列表 ["hello", "world", "yoyo"]


如何把把列表里面的字符串联起来，

得到字符串 "hello_world_yoyo"
'''



a = ["hello", "world", "yoyo"]
b = {'k1':'v1','k2':'v2','k3':'v3'}
c = 'asd'

print(''.join(a))
print(' '.join(a))
print('-'.join(b))
print('_'.join(c))
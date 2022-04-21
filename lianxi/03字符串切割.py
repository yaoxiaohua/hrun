'''
1.已知一个字符串为"hello_world_yoyo",
如何得到一个队列 ["hello", "world", "yoyo"]
 
 
2.让用户输入任意的用户名与密码，然后将他输入的用户名与 密码打印出来，如用户输入 abc/123 ，则打印
您输入的用户名是: abc
密码是:123
'''



a = "hello_world_yoyo"
# 分割
print(a.split("_"))

# 分割次数
print(a.split("_",1))

b = input("账号密码（user/password）")
c = b.split("/")
print('用户名:',c[0])
print('密码:',c[1])

'''
输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A,则输出-1
从 0 开始计数
A = "hello"
B = "hi how are you hello world, hello yoyo !"
'''


a = "hello"
b = "hi how are you hello world, hello yoyo !"

print(b.rfind(a))
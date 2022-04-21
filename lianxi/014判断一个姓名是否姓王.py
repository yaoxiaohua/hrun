'''
startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
startswith()方法语法：str.startswith(str, beg=0,end=len(string));
'''


a = input('姓名')

print('姓王' if str(a).startswith('王') else '不姓王')


#判断已什么结尾

print(str(a).endswith('王'))
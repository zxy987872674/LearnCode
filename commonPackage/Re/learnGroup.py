#coding=utf-8
'''
match和search一旦匹配成功，就是一个match object对象，而match object对象有以下方法：
group() 返回被 RE 匹配的字符串
start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置
group() 返回re整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。
a. group（）返回re整体匹配的字符串，
b. group (n,m) 返回组号为n，m所匹配的字符串，如果组号不存在，则返回indexError异常
c.groups（）groups() 方法返回一个包含正则表达式中所有小组字符串的元组，从 1 到所含的小组号，通常groups()不需要参数，返回一个元组，元组中的元就是正则表达式中定义的组。 
'''

import re
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))   #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456

###group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。###

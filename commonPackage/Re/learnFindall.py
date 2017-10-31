#coding=utf-8
import re
tt = "Tina is a good girl, she is cool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))
print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式 
print(re.findall(r'(\w)*oo(\w)',tt))[0][0] 

'''
执行结果如下：
['good', 'cool']
[('g', 'd'), ('c', 'l')]
g
'''

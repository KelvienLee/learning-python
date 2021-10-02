import re

text = 'python'


# match方法从前往后匹配, 返回object对象
# 
result = re.match('py', text)

print(result.group())
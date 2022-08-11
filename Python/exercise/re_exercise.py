import re

re.match('Hello', 'Hello123').group()

"""
========================
匹配单个字符
========================
"""
# 任意字符
re.match('..', 'H').group()
# 指定字符
re.match('[Hh]', 'H').group()
# 数字
re.match('[0123456789]', '1').group()
re.match('[0-9]', '1').group()
re.match('\d', '1').group()
# 单词字符a-zA-Z0-9
re.match('[a-zA-Z0-9]', 'a').group()
re.match('\w', 'H').group()
# 非单词字符
re.match('\W', '&').group()

"""
========================
匹配多个字符
========================
"""
# 0次或多次
re.match('a*', 'abc').group()
# 1次或多次
re.match('a+', 'abc')
# 0次或1次
re.match('a?', '').group()
# m次
re.match('a{3}', 'aaa').group()
# m到n次
re.match('a{3,5}', 'aaaa').group()

"""
========================
匹配开头或结尾
========================
"""
# 匹配开头
re.match('^https://.+', 'https://www.baidu.com').group()
# 匹配结尾
re.match('\w+@qq.com$', 'xxx@qq.com').group()

"""
========================
匹配方式
========================
"""
# match--从左到右依次匹配
re.match("Hello", "HelloWorld").group()
# search--扫描整个字符串，返回第一个匹配成功的字符串
re.search("World", "HelloWorld").group()
# findall--扫描整个字符串，返回所有匹配成功的字符串
re.findall("World", "HelloWorldWorld")
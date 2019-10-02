# 常用模块
# 文字处理 re

import re

# .(任意字符）                ^(以什么字符开头)
# $(以什么字符结尾)
# *(前一个字符出现0次或多次)    +(前一个字符出现1次或多次)
# ?(前一个字符出现0次或1次)     {num}(前一个字符出现指定的次数)
# {m,n}(前一个字符出现m次到n次) [abc]指定字符
# \d(一个数字)                \D(所有非数字字符)
# \s ()
re_compile = re.compile('ca*t')
pattern = re_compile
p = pattern
print(p.match('caaaaaat'))
print('----------------')

# [abc]
p = re.compile('c[abc]t')
num = p.match('cat')
print(num.start(), num.end())
print(p.match('cat'))
print(p.match('cbt'))
print(p.match('cct'))
print(p.match('cdt'))
print('----------------')

# .
p = re.compile('...')
print(p.match('cat'))
print('----------------')

# \d
p = re.compile('(\d+)-(\d+)-(\d+)')
print(p.match('2018-10-08'))
print(p.match('2018-10-09').group(0))
print(p.match('2018-10-09').group(1))
print(p.match('2018-10-09').group(2))
print(p.match('2018-10-09').group(3))
print(p.match('2018-10-09').groups())
year, month, day = p.match('2018-10-10').groups()
print(year, month, day)
print('----------------')

print(p.search('aa2018-10-09bb'))
print('----------------')

phone = '156-5902-5790 #这是手机号码'
phone = re.sub(r'#.*', '', phone)
print(phone)
phone = re.sub('\D', '', phone)
print(phone)
print('----------------')

print(re.findall('2018', 'aa2018-10-09bbaa2018-10-09bb'))
print(re.findall('\d', 'aa2018-10-09bbaa2018-10-09bb'))  # 数字
print(re.findall('\D', 'aa2018-10-09bbaa2018-10-09bb'))  # 除了数字以外的字符
print(re.findall('\w', 'aa2018-10-09bbaa2018-10-09bb'))  # 大小写英文字母、10个数字
print(re.findall('\W', 'aa2018-10-09bbaa2018-10-09bb'))  # 除了字母和数字以外的字符
list = re.findall('\d', 'aa2018-10-09bbaa2018-10-09bb')
print(list[1:5])
del list[1:5]
print(list)
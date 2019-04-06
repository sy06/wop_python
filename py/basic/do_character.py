# -*- coding: utf-8 -*-
# ord()函数获取字符的整数
# chr()函数把编码转换为对应的字符
print(ord('A'),ord('中'))
print(chr(66),chr(25991))
# 'ABC':str  b'ABC':bytes
# encode():unicode条件下,将str转换为bytes
print('ABC'.encode('ascii'))
print('中文'.encode('ascii'))



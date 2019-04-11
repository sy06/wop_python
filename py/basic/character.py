# -*- coding: utf-8 -*-

# ord()函数获取字符的整数
# chr()函数把编码转换为对应的字符
print(ord('A'),ord('中'))
print(chr(66),chr(25991))
# 'ABC':str  b'ABC':bytes

# encode():unicode条件下,将str转换为bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii')) 无法运行,中文超过了ascii的范围

#decode():将bytes转换为str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# b'\xe4\xb8\xad\xff'.decode('utf-8')会报错 超过了范围
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#len()计算str中有多少字符
print(len('ABC'))
print(len('中文'))
#len()计算bytes中有多少字节
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))


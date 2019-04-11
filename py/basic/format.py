# -*- coding: utf-8 -*-

#%d 整数
#%f 浮点数
#%s 字符串
#%x 十六进制整数
print('hello, %s' % 'world')
print('%s, %s' % ('hello','world'))
print('%2d-%02d' % (3.14159,3.14159))#补0
print('%.2f' % 3.14159)#小数点后位数
# print('rate is: s% %%' % 7) #%%表示%
# unsupported format character '%' (0x25) at index 12

#work
s1 = 72
s2 = 85
r = (85-72)/72
print('%.2f' % r)


# -*- coding: utf-8 -*-

# if 语句的特点是从上往下判断，如果莫格判断是TRUE，就把该判断单元给执行后，忽略剩下的else/elif
# for example
age = 20
if age >= 6:
    print('Teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#work
H = 1.75
W = 80.5
bmi = (80.5/17.5) ** 2 #平方
if bmi > 32:
    print('fei chang pang!')
elif bmi > 28:
    print('yi ban pang')
elif bmi > 25:
    print('guo zhong')
elif bmi > 18.5:
    print('zhen chang')
else:
    print('qing')
print(bmi)

# -*- coding: utf-8 -*-

classmates = ('A' , 'B' , 'C')
#tuple的指向不会变，没有append() insert()之类的方法
#尽可能地使用tuple
t = () #空tuple
print(t)
t = (1,) #注意逗号，没有逗号，详单与赋值1
print(t)
t = (1,2,[3,4])
print(t)
print(t[0])
print(t[1])
print(t[2])
#t[2] = [4,5]  'tuple' object does not support item assignment
t[2][0]=4
t[2][1]=5 #tuple的每一个元素都不可变 但是tuple中有list的话，可以修改list中元素，重点在于指向不变！
print(t)

#work
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

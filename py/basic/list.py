# -*- coding: utf-8 -*-

#list = [ A, B, C]
classmate = ['A','B','C']
print(classmate)
print(len(classmate))
print(classmate[0])#start with 0
print(classmate[1])
print(classmate[2])
#print(classmate[3]) wrong

print(classmate[len(classmate)-1])
#same as 
print(classmate[-1])

print(classmate[-2])
print(classmate[-3])
#print(classmate[-4]) wrong

classmate.append('D')#添加至末尾
print(classmate)
classmate.insert(1,'A0')#插入至指定位置
print(classmate)
classmate.pop()#删除末尾
print(classmate)
classmate.pop(1)#删除指定位置数据
print(classmate)
classmate[0] = 'A1'#赋值
print(classmate)
L = ['A' , 123 , 'C']#LIST中数据类型可以不一样
L = ['A' , 'B' , ['C', 'D'] , 'E']#LIST中可以有别的LIST，即二（三/N）重数组
p = ['C' , 'D',]
L = ['A' , 'B' , p , 'E']
print(L)
print(p[1])
print(L[2][1])


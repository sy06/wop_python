# -*- coding: utf-8 -*-

#for
name = ['A' , 'B' , 'C']
for i in name:
    print(i)

sum = 0
for i in range(101):
    sum = sum+i
print(sum)

#while
sum = 0
n = 99
while n >= 0:
    sum = sum + n
    n = n - 2
print(sum)

#work
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('HELLO, %s' % name)
    
#break
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 1
while n <= 100:
    if n >= 10:
        break
    print(n)
    n = n + 1
print('END')

#continue
n = 0
while n <= 10:
    n = n + 1
    print(n)

n = 0
while n <= 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
    
#将可能避免使用 break 和 continue 会使逻辑分叉过多，造成混乱

#!/usr/bin/env python3
#-*-coding:utf-8 -*-

#1.数据类型及变量
print(10_1000_1000)
print('字符串 转义字符\n \\n \"\"')
print(r'使用r带\n \' \" 表示内部的字符都不转义')
print('''三个单引号表示多行
,second line''')
print(r'''第一行 多行模式也可以带r表示内部不转义\n
第二行''')
a=True
print(a)

print(r'# -*- coding: utf-8 -*-')
n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)
#2.python 字符串
a = ord('A')
print(a)
a = ord('中')
print(a,chr(66),chr(25991),'\u4e2d\u6587')
print('ABC'.encode('ascii'),'中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
print(len('A'),len('中国'),len('汗'),len(b'abc'))
print('%2d-%02d' % (3,1))
r=2.5
s=3.14*r**2
print(f'The area of a circle with radius {r} is {s:2f}')

#3.使用list和tuple
classmates = ['Michael','Bob','Tracy']
print(classmates,classmates[0],classmates[1],classmates[-1])
classmates.append('wangxiang')
print(classmates)
classmates.insert(2,'test')
print(classmates)
classmates.pop()
print(classmates)
classmates[2] = ['A','B','C']
print(classmates[2][2])
classmates = ('Michael','Bob','Tracy')
emptyTuple=()
oneTuple=(1,)
print(emptyTuple,oneTuple)
#4.条件判断
age=20
if age>=18:
    print('Your age is',age)
    print('default')
else:
    print('your age is',age)
    print('teenager')

height = 1.75
weight = 80.5
bmi = weight/(height**2)
if bmi<18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')


#5.循环
names = ['wangxiang','zengbing','wangjingcheng']
for name in names:
    print(f'名字是：{name}')

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#6.dic 和 set

d = {'wangxiang':31,'zengbing':25,'wangjingcheng':2}
print(d['wangxiang'])
for name in d:
    print(d[name])

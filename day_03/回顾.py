# 回顾
# Python
# 变量
"""
1、普通赋值
name = 10
2、链式赋值
a=b=c=10
3、多元赋值
a,b=1,2

"""
# a = 10
# b = 20
# c = a
# a = b
# b = c
# a,b = b,a
#
# print(a,b)

# 输入输出工具
# sex = input('请输入你的性别:')
# print("asdf",2345,1+2,end="\n")

#
""""""
''''''

# 数据类型
# 数字类型（int/float）
# bool 布尔   True False
# 字符型
# '' ""  """"""  ''''''
# 字符编码： ASCII GBK GB2312  UTF-8 unicode
# 前缀  b r f
# 转义字符  \' \" \\ \n \r \t
# 模板字符串  "我的名字是%s"%()   %0.2f
# f"{} {变量}"
# 切片 [start:end:step]

# 列表 list 数组
# arr = [1,2,3,4,5,6]
# 列表的操作
# 增  append() insert()
# 删除 .pop() del **
# arr[index] = ""
# arr[index]

# 二维列表
# 浅拷贝  .copy()

# 元组
# t1 = (1,)
# 不能改变

# 字典 dict
# xm = {'name':'小明','sex':'男'}

# 集合 set
#
# arr = [1,2,3,4,5,6,7,12,2,3,4]
# print( list(set(arr)) )

# 可变
# list set dict
# 不可变
# str int float bool tuple


# 运算符
# 算术运算符
# + - * / %  //  **
#  //  **
# +  *     ( str list tuple )
# print("abc"*3)

# 赋值运算符
# += -+ *= /= %= //= **= =
# num = 10
# num+=20   # num = num+20
# print(num)

# 关系运算符 结果 bool
# > >= < <= != ==

# 逻辑运算符
# and or not
# in not in
# is is not

# num = input("请输入一个数:")
# input函数返回值 是 str
# 单路分支
# if int(num)>5:
#     print("%s大于5"%num)

# 双路分支

# num = 5
# if num>10:
#     print("%s>10"%num)
# else:
#     print("%s<=10"%num)

# 多路分支

# num = 5
#
# if num>10:
#     print(f"{num}>10")
# elif num==10:
#     print(f"{num}==10")
# else:
#     print(f"{num}<10")


# for  while  |   do while

"""
for while 适用场合不一样:
for 适用在明确循环次数
while 适用在次数不明确的情况下

for

for i in 迭代对象:
    print(i)



"""
# for i in range(1,11):
#     if i%2==0:
#         print("偶数:%s"%i)
#     else:
#         print("奇数:%s"%i)

"""
while 条件:
    循环体
"""
#
# num = 1
# while num<=10:
#     print(num)
#     num+=1


# 猜数字  0-99 num

import random

num = random.randint(0,99)
cs = 0

while True:
    if cs<5:
        cs+=1
    else:
        print("你太笨了!!")
        break
    num1 = int(input("请输入一个数(0,99):\n"))
    if num==num1:
        print("恭喜你胜利!!")
        break  # 终止循环   continue 继续
    elif num1<num:
        print("太小了!")
    else:
        print("太大了!")




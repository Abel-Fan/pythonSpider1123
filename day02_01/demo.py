# print("hello",end="。")
# print('world')

# 单行注释
"""
多行注释
"""
'''
多行注释
'''

# str3 = '''abc'''
#  type() 测试数据类型
# print(  type(str3) )
# print(   "\\"  )
# print("我的名字叫%s,我的年龄%s"%("小明",18))
# print("我的成绩%0.2f"%68.87)
# print(f"我的名字叫{'小明'},我的年龄{20}")

# print("山西优逸客科技有限公司"[:])


# list 列表
# arr1 = [1,2,3,4,5,6]
# print(arr1)

# 访问元素
# arr[index]
# print(arr1[0])  # 访问第一个数据
# 修改元素
# arr1[0] = "a"
# print(arr1)
# 增加
# arr1.append('b')  # 末尾增加
# print(arr1)

# arr1.insert(1,"A")
# print(arr1)

# 删除
# arr1.pop(0)
# print(arr1)

# del arr1[0]
# print(arr1)

# num1 = 10
# num2 = num1
# num2 = 20
# print(num1,num2)

# arr1 = [1,2]
# arr2 = arr1
# arr2[0] = 'a'
# print(arr1,arr2)
# [1,2]  ['a',2]

# arr1 = [1,2]
# arr2 = arr1.copy()
# arr2[0] = 'a'
# print(arr1,arr2)

# dict1 = {'name':'小明','age':20}
# print(dict1)
# 基本操作
# 访问
# print(  dict1['name']  )
# 添加
# dict1['sex'] = '男'
# print(dict1)
# 修改
# dict1['name'] = "小明明"
# print(dict1)
# 删除
# dict1.pop("age")
# print(dict1)
# del dict1['age']
# print(dict1)


# t1 = (1,2,3,4,5,6)
# t1[0] = 'a'
# arr = [1,2,1,2,3,4,5]
# print(  list(set(arr))  )

# 算术运算符
# + - *  / %  ** 幂运算  // 地板除
print(2**10)
print(10//3)

# + 拼接   * 重复
# print("abc"+"def")
# print([1,2,3]+[4,5,6])
# print((1,2,3)+(4,5,6))
#
# print("abc"*3)

# arr = [1,2,3,4,5]
# print(1 not in arr)
#
# arr1 = [1,2]
# arr2 = arr1
# print(arr1 is arr2)
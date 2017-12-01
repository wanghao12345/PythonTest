# int内部功能的介绍
#
# type():
# 1.基本数据类型使用type()函数时,得到相应的数据类型
# a = 12
# b = 12.01
# c = "123"
# print(type(a))          >>> int
# print(type(b))          >>> float
# print(type(c))          >>> str
# 2.其它类使用type()函数时,得到这个类所在的位置
# from twisted.internet import reactor
# print(type(reactor))    >>> twisted.internet.selectreactor.SelectReactor
#
# bit_length():
# 返回表示该数字占用的最少位数
# age = 18
# print(bin(18))            >>> 0b10010
# 0001 0010
# print(age.bit_length())   >>> 5
#
# __abs__():
# 返回绝对值
# age = 18
# score = -100
# print(age.__abs__())    或者 print(abs(age))        >>> 18
# print(score.__abs__())  或者 print(abs(score))      >>> 100
#
# __add__(self,y):
# 两个数相加
# a = 1
# b = 2
# print(a.__add__(b))   或者 print(a+b)   >>> 3
#
# __and__(self,y):
# 求两个数的与
# a = 1
# b = 2
# print(a.__and__(b))      >>> 0
#
# __divmod__():
# 计算两个数相除,得到一个元祖,元祖的第一个是商，第二个是余数
# all_item = 95
# pager = 10
# result = all_item.__divmod__(pager)
# print(result)             >>>(9,5)
#
# __rdivmod__():
# 交换两个数字的位置然后相除
#
# __eq__():
# 判断两个数是否相等
# a = 18
# result = a.__eq__(19)
# print(result)              >>> False
# print(18==19)              >>> False
#
# __float__():
# 将int转变成float
# age = 18
# print(type(age))         >>>int
# result = age.__float__()
# print(type(result))      >>>float
#
# __floordiv__():
# 两个数相除，只保留商
# age = 5
# result = age.__floordiv__(6)
# print(result)     >>> 0
# print(5//6)       >>> 0
#
# __init__():
# int类的构造方法
# 执行
#     age = int(19)
# 就会执行构造方法
#
# __pow__():
# 求幂
# a = 2
# b = 2
# print(a.__pow__(b))   >>> 4
# print(a**b)           >>> 4
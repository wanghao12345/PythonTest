#变量名起名:只能是字母、数字或下划线的任意组合

# 合法：
# 1.显式
# 2.nums_of_alex_gf = 19
# 3.NumsOfAlexGf = 2
# 4.name5f=21
# 不合法：
# 1.nams-of-alex-gf =
# 2.5name=
# 3.!name=
# 4.name of alex=
# 5.id =
a = 3
b = a
print(a,b)
print(id(a),id(b))

a = 5
print(a,b)
print(id(a),id(b))

#eval()函数:去python内存中寻找是否含有某个变量,如果含有该变量，就会返回该变量的值，没有就会报错，传经的参数使用字符串格式。
print(eval('a'))






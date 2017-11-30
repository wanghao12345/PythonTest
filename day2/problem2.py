# 字符串格式化
name = input("name:")
age = input("age:")
job = input("job:")

# 一般写法
# 有多少字符串就占有多少内存
# print("Information of []:"+name+"\nName:[]"+name+"\nAge:[]"+age+"\nJob:[]"+job)

# 格式化写法
# 只占有一个内存
# print("Information of %s:\nName:%s\nAge:%s\nJob:%s" %(name,name,age,job))

# 单引号：单引号中可以使用双引号,中间的会当作字符串输出

# 双引号：双引号中可以使用单引号，中间的会当作字符串输出

#python中单引号和双引号没有区别

# 三引号：三单引号和三双引号中间的字符串在输出市保持原来的格式
msg = '''
        Information of %s:
        Name:%s
        Age:%s
        Job:%s
''' %(name,name,age,job)
print(msg)


# %s 字符串
# %d 数字
# %f 浮点型

name = input("name:")
age = int(input("age:"))
job = input("job:")

msg = '''
        Information of %s:
        Name:%s
        Age:%d
        Job:%s
''' %(name,name,age,job)
print(msg)
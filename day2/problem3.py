# 列表的常用操作 list
name_list = ["alex","65brother","tenglan"]
# 查看name_list的拥有方法：dir(name_list) help(name_list)
# 索引
print(name_list[2])
print(name_list.index("65brother"))
# 切片:切列表的一块
print(name_list[0:3])
print(name_list[0:3:2])
print(name_list[-2:]) #取后面两个
# 追加
name_list.append("ERIC")
name_list.append("65brother")
print(name_list)
# 删除
name_list.pop() #删除最后一个
name_list.remove("65brother")#删除指定值但是只能删除一个
#删除所有的65brother值
for i in range(name_list.count('56brother')):
    name_list.remove("56brother")
# 长度
# 循环
# 包含
# 某个值的个数
name_list.count("65brother")
# 插入
name_list.insert(2,"66brother")
print(name_list)
# 反转
name_list.reverse()
# 排序
name_list.sort()
# 扩展
a = [1,2,3]
b = [4,5,6]
c = "Alex"
# print(a=a+b)
a.extend(b)
a.extend(c)
print(a)

# 元祖的常用操作 tuple
t = (1,2,3,4)
l = [1,2,3,4]
# dir(t)
# help(t)

# 将元祖转变为列表
list(t)
# 将列表转变为元祖
tuple(l)








# 字符串常用功能:
# (1) 移除空白
# str.strip()默认移除两边的空白,不能去掉中间的空格,但是可以指定去除某个字符str.strip("A")
# (2) 分割
# (3) 长度
# (4) 索引
# (5) 切片

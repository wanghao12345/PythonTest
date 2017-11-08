# PythonTest
Python学习


1.安装Python环境

2.第一个Python程序
	2-1.输出：print()
		2-1-1.输出时，两个字符串输出时，用作隔离的逗号当做空格使用
	2-2.输入：name = input()

3.Python基础
	3-1.数据类型和变量
		3-1-1.整数
		3-1-2.浮点数
		3-1-3.字符串
		3-1-4.布尔值 
		3-1-5.空值
		3-1-6.变量：变量在程序中就是用一个变量名表示，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
		3-1-7.常量：变量名字母全部用大写
	3-2.字符串和编码
		3-2-1.字符编码
		3-2-2.Python字符串：ord()、chr()、encode()、decode()、len()
		3-2-3.格式化
	3-3.使用list和tuple
		3-3-1.list
			添加：append()
			插入：insert(index,value)
			删除：pop()----删除末尾的值   pop(index)----删除指定位置的值
			长度：len(list)	
		3-3-2.tuple
			tuple初始化就不能修改，即没有append()、insert()这样的方法，可以正常的使用classmates[0],classmates[-1],但不能赋值成另外的元素
			空tuple：t=()
			单一元素tuple：t=(1,)
	3-4.条件判断
		if<条件判断1>:
			<执行1>
		elif<条件判断2>:
			<执行2>
		else:
			<执行3>
	3-5.循环
		for x in ...
		range(101):生成0-100的序列整数
		while<执行条件>:
			<执行>
	3-6.使用dict和set
		dict：其它语言俗称map，使用键值对（key-value）存储，具有极快的查找速度
			1.查询：
				d={'michael':95,'Bob':75,'Tracy':85}
				d['michael']
				>>>95
			2.判断是否存在：
				in: 'a' in arr
				dict的get方法：arr.get('a')或arr.get('a',-1)
			3.删除
				pop(key)
		set:set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
			1.添加：add(key)
			2.删除：remove(key)

4.函数
	4-1.调用函数
	4-2.定义函数
		def my_fun(x):
			if x>=0:
				return x
			else:
				return -x
		1.位置参数
		2.默认参数
		3.可变参数
		4.关键字参数
		5.命名关键字参数
	4-3.递归函数

5.高级特性
	5-1.切片
		list、tuple、字符串都实用
	5-2.迭代
		list、tuple、dict、字符串
		1.判断一个对象是否可以迭代：
			from collections import Iterable
			isinstance(object,Iterable)
		2.在for循环中同时迭代索引和元素本身
			for i,value in enumerate(['A','B','C']);
			print(i,value)
			0 A
			1 B
			2 C
	5-3.列表生成式
	5-4.生成器




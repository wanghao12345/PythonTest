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
	5-5.迭代器
		可迭代对象Iterable:可以直接作用于for循环的对象统称为可迭代对象（list,tuple,dict,set,str）
		isinstance()：判断一个对象是否是Iterable对象
		迭代器Iterator：可以被next()函数调用不断返回下一个值的对象称为迭代器
		isinstance():判断一个对象是否是Iterator对象
		生成器都是Iterator对象，但list、dict、str、虽然是Iterable，但不是Iterator,但是list、dict、str等Iterable可以通过iter()函数变成Iterator

6.函数式编程
	6-1.高阶函数
		6-1-1.变量可以指向函数
		6-1-2.函数名也是变量
		6-1-3.传入函数
		6-1-4.map/reduce
			map:接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果
		6-1-5.filter
		6-1-6.sorted
	6-2.返回函数
		6-2-1.函数作为返回值：高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
		6-2-2.闭包：当一个函数返回了一个函数后，其内部的局部变量还被新函数引用。(返回闭包时注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量。如果一定要引用循环变量，方法就是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变)
	6-3.匿名函数
		关键字lambda表示匿名函数，冒号前面的X表示函数参数。匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
		好处：用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数父子给一个变量，再利用变量来调用该函数(f = lambda x:x+1)
	6-4.装饰器
		def now()
			print('2017-11-15')
		f = now   
		f()
		2017-11-15
		now.__name__
		now
		f.__name__
		now
		(函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用该函数。函数对象有一个__name__属性,可以拿到函数的名字)
		装饰器(Decorator)：需要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望改变now()函数的定义，这种代码运行期间动态增加功能的方式称之为"装饰器"
	6-5.偏函数
		functools.partial:把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

7.模块
	7-1.使用模块
	7-3.安装第三方模块

8.面向对象编程
	class Student(object):
		def __init__(self,name,score):
			self.name = name
			self.score = score
		def print_score(self):
			print('%s:%s' %(self.name,self.score))
	bart = Student('Bart Simpson',59)
	bart.print_score()
	8-1.类和实例
	8-2.访问限制
		在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑
		私有变量：如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在python中，实例的变量名如果以__开头，就变成了一个私有变量(private)，只有内部可以访问，外部不能访问，所以我们把Student类改一改
		<!-- class Student(object):
			def __init__(self,name,score):
				self.__name = name
				self.__score = score
			def print_score(self):
				print('%s:%s' %(self.__name,self.__score)) -->
		get访问私有变量：
			<!-- class Student(object):
				...
				def get_name(self):
					return self.__name -->
		set方法：
	8-3.继承和多态
		继承：在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类(Subclass)，而被继承的class称为基类、父类或超类(Base class、Super class).
		class Animal(object):
			def run(self):
				print('Animal is running...')
		class Dog(Animal):
			pass
		class Cat(Animal):
			pass
		继承的好处：子类获得了父类的全部功能。
		多态：当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()，在代码运行的时候，总会调用子类的run()。
		isinstance():判断一个变量是否是某个类型
			a = list() #a是list类型
			b = Animal() #b是Animal类型
			c = Dog() #c是Dog类型
			isinstance(a,list)    true
			isinstance(b,Animal)  true
			isinstance(c,Dog)     true
			isinstance(c,Animal)  true
			isinstance(b,Dog)     False
		静态语言VS动态语言：
			对于静态语言java来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。否则，将无法调用run方法。对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就行了
			class Timer(object):
				def run(self):
					print('Start...')
			这就是动态语言的鸭子类型，它并不要求严格的继承体系，一个对象只要看起来像鸭子，走起路来像鸭子，那它就可以被看做是鸭子。
	8-4.获取对象信息
		使用type():
			判断基本类型和变量
		使用isinstance():
			对于class的继承关系来说，使用type()就很不方便，要判断class的类型，可以使用isinstance()
		使用dir():
			如果要获得一个对象的所有属性和方法，可以使用dir函数，它返回一个包含字符串的list，比如，获得一个               str对象的所有属性和方法
		使用getattr()、setattr()以及hasattr()直接操作一个对象的状态:
			class MyObject(object):
				def __init__(self):
					self.x = 9
				def power(self):
					return self.x * self.x
				obj = MyObject()
			hasattr(obj,'x')  true  判断某个对象是否有属性x
			setattr(obj,'y',19)  给某个对象设置一个属性y
			getattr(obj,'y') 获取某个对象的属性y也可以获得对象的方法
	8-5.实例属性和类属性
		实例绑定属性的方法：通过实例变量或者通过self变量
			class Student(object):
				def __init__(self,name):
					self.name = name
			s = Student('Bob')
			s.score = 90
		类属性：在class中定义属性
			class Student(object):
				name = 'Student'

9.面向对象高级编程
	9-1.使用__slots__
		如果我们要限制实例的属性，比如只允许对Student实例添加name和age属性，因此利用__slots__可以限制该class实
		例能添加的属性:
		class Student(object):
			__slots__=('name','age') #用tuple定义允许绑定的属性名称
		s=Student()
		s.name = 'Machael' #true
		s.age  = 25 #true
		s.score = 99 #false
		注意：它只对当前的类之类起作用，对继承的子类是不起作用的。
	9-2.使用@property
		在绑定属性时，如果把属性暴露出去，虽然写起来很简单，但是，没有办法检查参数。
		传统检查参数：
			<!-- class Student(object):
				def get_score(self):
					return self.__score
				def set_score(self,value):
					if not isinstance(value,int):
						raise ValueError('score must be an integer!')
					if value<0 or value>100
						reise ValueError('score must between 0~100')
					self._score = value -->
        Python内置的@property装饰器把一个方法变成属性调用：
            class Student(object):
                @property
                def score(self):
                    return self._score
                @score.setter
                def score(self,value):
                    if not isinstance(value,int):
                        raise ValueError('score must be an integer!')
                    if value <0 or value >100:
                        raise ValueError('score must between 0~100!')
                    self._score = value
            @property的实现比较复杂，它把一个getter方法变成属性，只需要加上@property就可以了，此时@property本              身又创建了另一个装饰器@score.setter：负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的             属性操作
                s = Student()
                s.score = 60  s.score => 60
                s.score = 9999 =>ValueError:score must between 0~100!
             注意：我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的，还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
             class Student(object):
                @property
                def birth(self):
                    return self._birth
                @birth.setter
                def birth(self,value):
                    self._birth = value
                @property
                def age(self):
                    return 2015-self._birth
	         上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前的时间计算出来
	9-3.多重继承
	    9-3-1.多重继承
	        #动物类
	        class Animal(object)
	            pass
	        #大类
	        class Mammal(Animal):
	            pass
	        class Bird(Animal):
	            pass
	        #各种动物
	        class Dog(Mammal):
	            pass
	        class Bat(Mammal):
	            pass
	        class Parrot(Bird):
	            pass
	        class Ostrich(Bird):
	            pass
            #定义Runable和Flyable类
            class Runnable(object):
                def run(self):
                    print('Running....')
            class Flyable(object):
                def fly(self):
                    print(Fly.....')
            对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog
            class Dog(Mammal,Runable):
                pass
            对于需要Flyable功能的动物，就多继承一个Flyable，例如Dog
            class Bat(Mammal,Flyable):
                pass
        9-3-2.MixIn
            MixIn:在设计类的继承关系时，通常，主线都是单一继承下来的，但是，如果需要“混入”额外的功能，通过多重继承就可以实现，这种继承称之为MixIn。
            为了更好的看出继承关系，把Runnable和Flyable改为RunnableMixIn和FlyableMixIn.....
            class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
                pass
    9-4.定制类
        9-4-1.__str__
            (1)
            class Student(object):
                def __init__(self.name):
                    self.name = name
            print(Student('Michael'))
            >>><__main__.Student object at 0x109afb190>
            (2)
            class Student(object):
                def __init__(self,name):
                    self.name = name
                def __str__(self):
                    return 'Student object (name:%s)' %self.name
            print(Student('Michael'))
            >>>Student object (name:Michael)
            s = Student('Michael')
            s
            >>><__main__.Student object at 0x109afb310>
            (3)
            __str__()和__repr__()：两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。解决办法是再定义一个__repr__(),通常__str__和__repr__()代码都是一样的，所以，有个偷懒的写法：
            class Student(object):
                def __init__(self, name):
                    self.name = name
                def __str__(self):
                    return 'Student object (name=%s)' % self.name
                __repr__ = __str__
        9-4-2.__iter__
            如果一个类想被用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
            class Fib(object):
            	def __init__(self):
            		self.a,self.b = 0,1 #初始化两个计数器a,b
            	def __iter__(self):
            		return self
            	def __next__(self):
            		self.a,self.b = self.b,self.a+self.b #计算下一个值
            		if self.a>10000
            			raise StopIteration()
            		return self.a 
			>>>for n in Fib()
			print(n)
		9-4-3.__getitem__ 
			(1)
			Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第五个元素：
				>>> Fib()[5]
				Traceback (most recent call last):
				  File "<stdin>", line 1, in <module>
				TypeError: 'Fib' object does not support indexing
			要像list那样按照下标取出元素，需要实现__getitem__()方法：
				class Fib(object):
					def __getitem__(self,n):
						a,b = 1,1 
						for x in range(n):
							a,b = b,a+b
						return a 
				>>>f = Fib()
				>>>f[1]
				1 
				>>>f[10]
				89
			(2)
			list有个神奇的切片方法，对于Fib却报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
				class Fib(object):
					def __getitem__(self,n):
						if isinstance(n,int): #n是索引
							a,b = 1,1 
							for x in range(n):
								a,b = b,a+b 
							return a 
						if isinstance(n,slice):
							start = n.start 
							stop = n.stop 
							if start is None:
								start = 0 
							a,b = 1,1 
							L = []
							for x in range(stop):
								if x>=start:
									L.append(a)
								a,b = b,a+b 
							return L 
				>>>f = Fib()
				>>>f[0:5]
				[1,1,2,3,5]
		9-4-4.__getattr__ 
			(1)
			正常情况下，当我们调用类的方法和属性时，如果不存在，就会报错，要避免这个错误，除了可以加上一个属性score外，Python还有另外一个机制，那就是写一个__getattr__()方法，动态返回一个属性
			class Student(object):
				def __init__(self):
					self.name = 'Michael'
				def __getattr__(self,attr):
					if attr=='score':
						return 99
			>>> s = Student()
			>>> s.name
			'Michael'
			>>> s.score
			99
			(2)
			返回函数也是可以的：
				class Student(object):
					def __getattr__(self,attr):
						if attr == 'age':
							return lambda:25 
						raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
			调用方式为：
				>>>s.age()
				25
			注意：只有在没有找到属性的情况下，才调用__getattr__已有的属性,当调用__getattr__也没有的属性，如s.abc都会返回None，这是因为我们定义的__getattr__默认返回的就是None。要让class只响应特定的几个属性，我们就要按照约定抛出AttributeError的错误
		9-4-5.__call__
			__call__：一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们使用instance.method()来调用。__call__方法可以直接对实例进行调用
			class Student(object):
				def __init__(self,name):
					self.name = name
				def __call__(self):
					print('My name is %s' %self.name)
			>>>s = Student('Michael')
			>>>s()
			My name is Michael
	9-5.使用枚举类
	9-6.使用元类 

10.错误、调试和测试
	10-1.错误处理 
		try...except...finally...
			try:
				print('try...')
				r = 10/0
				print('result:' r)
			except ZeroDivisionError as e:
				print('except:',e)
			finally:
				print('finally...')
			print('END')
		当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块




































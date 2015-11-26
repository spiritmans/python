Python Built-in Functions
	abs(x)							绝对值或复数的值
	all(iterable)					如果iterable的元素不为0、''、False或者iterable为空时，all()返回True，否则返回False
	any(iterable)					集合中的元素有一个为真的时候为真;特别的，若为空串返回为False
	basestring()					str和unicode的超类,不能直接调用，可以用作isinstance判断
	bin(x)							将整数x转换为二进制字符串
	bool(x)							将x转换为Boolean类型。true/false

	bytearray([source [,encoding [,errors]]])	
									返回一个byte数组。
										1、如果source为整数，则返回一个长度为source的初始化数组；
										2、如果source为字符串，则按照指定的encoding将字符串转换为字节序列；
										3、如果source为可迭代类型，则元素必须为[0 ,255]中的整数；
										4、如果source为与buffer接口一致的对象，则此对象也可以被用于初始化bytearray.

	callable(object)				检查对象object是否可调用:
										1、类是可以被调用的;
										2、实例是不可以被调用的，除非类中声明了__call__方法
	chr(x)							返回整数x对应的ASCII字符

	classmethod()					1、注解，用来说明这个方式是个类方法;
									2、类方法即可被类调用，也可以被实例调用;
									3、类方法类似于Java中的static方法;
									4、类方法中不需要有self参数
	cmp(x,y)						如果x < y ,返回负数；x == y, 返回0；x > y,返回正数
	
	compile(source, filename, mode[,flags[,dont_inherit]])
									将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值:
										1、参数source：字符串或者AST（Abstract Syntax Trees）对象;
										2、参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值;
										3、参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’
	
	complex([real[,imag]])			创建一个复数
	delattr(object,name)			删除object对象名为name的属性
	dict([arg])						创建数据字典
	
	dir([object])					1、不带参数时，返回当前范围内的变量、方法和定义的类型列表;
									2、带参数时，返回参数的属性、方法列表;
									3、如果参数包含方法__dir__()，该方法将被调用。当参数为实例时;
									4、如果参数不包含__dir__()，该方法将最大限度地收集参数信息
	
	divmod(a,b)							分别取商和余数。整型和浮点型皆可
	enumerate(sequence [,start=0])		返回一个可枚举的对象,该对象的next()方法将返回一个tuple
	eval(expression [,globals[,locals]])
										计算表达式expression的值
	file(filename [,mode[,bufsize]])	打开文件。mode：'r'（读）、'w'（写）、'a'（追加）

	filter(function, iterable)			构造一个序列，等价于[ item for item in iterable if function(item)];
											1、参数function：返回值为True或False的函数，可以为None;
											2、参数iterable：序列或可迭代对象

	float()							将一个字符串或数转换为浮点数。如果无参数将返回0.0
	format(value[,format_spec])		格式化输出字符串。格式化的参数顺序从0开始，如“I am {0},I like {1}”
	frozenset([iterable])			产生一个不可变的set
	getattr(object,name [,defalut])	获取一个类的属性
	hasattr(object,name)			判断对象object是否包含名为name的特性
	hash(object)					如果对象object为哈希表类型，返回对象object的哈希值
	help()
	hex(x)							将整数x转换为16进制字符串
	id(object)						返回对象的唯一标识
	input()
	int([x[,base]])					将一个字符转换为int类型，base表示进制
	isinstance(object,classinfo)	判断object是否是class的实例
	issubclass(class,classinfo)		判断是否为子类
	iter(o[,sentine])				生成一个对象的迭代器，第二个参数表示分隔符
	len(s)							返回集合长度
	list([iterable])				将一个集合类转换为另外一个集合类
	locals()						返回当前的变量列表
	long([x[,base]])				将一个字符转换为long类型
	map(function, iterable, ...)	遍历每个元素，执行function操作
	max(iterable[,args...][key])	返回集合中的最大值
	memoryview(object)				返回一个内存镜像类型的对象
	min(iterable[,args...][key])	返回集合中的最大值
	next(iterator[, default])		类似于iterator.next()
	object()						基类
	oct(x)							将一个数字转化为8进制
	open(name[,mode[,buffering]])	打开文件
	
	ord()							是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，
									它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，
									如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常

	pow(x,y[,z])					返回x的y次幂			
	print()							打印函数
	
	property([fget[,fset[,fdel[,doc]]]])  	属性访问的包装类，设置后可以通过c.x=value等来访问setter和getter
	
	range([start],stop[,step])				产生一个序列，默认从0开始
	raw_input()								设置输入，输入都是作为字符串处理
	reduce(function, iterable[, initializer])	
											合并操作，从第一个开始是前两个参数，然后是前两个的结果与第三个合并进行处理，以此类推
	reload(module)							重新加载模块
	repr(object)							将一个对象变幻为可打印的格式
	round(x[,n])							四舍五入
	set()									set对象实例化
	setattr(object, name, value)			设置属性值
	slice()						
	sorted(iterable[,cmp[,key[,reverse]]])	对集合排序
	staticmethod()							声明静态方法，是个注解
	str([object])							转换为string类型
	sum()									对集合求和
	super(type[,object-or-type])			引用父类
	tuple([iterable])						生成一个tuple类型
	type()									查看对象类型
	unichr(x)								返回给定int类型的unicode
	unicode(object)							返回object的Unicode版本字符串
	vars([object])							返回对象的变量，若无参数与dict()方法类似
	xrange([start],stop[,step])				与range()类似，但xrnage()并不创建列表，而是返回一个xrange对象，
											它的行为与列表相似，但是只在需要时才计算列表值，当列表很大时，这个特性能为我们节省内存
	zip()
	__import__()

"""def func1():
	print("1")
def func2():
	print("2")
def func3():
	print("3")
def func4():
	print("4")
lis=[func1,func2,func3,func4]
for i in lis:
	i()
print(lis)"""

#传参
"""def func():
	print("1")
def func2(fn):
	print("2")
	fn()
	print("3")
func2(func)#将函数func当做参数传递给func2的参数fn


def func_1():
	print("111")
	def func_2():
		print("222")
	print("333")
	return func_2
fn=func_1()#执行函数1，函数1返回的是函数2.这是fn指向的是上面的函数2
fn()#执行上面的返回函数值          111   333   222"""

#闭包(即内层函数，对非全局的外层函数的变量的引用）
"""def func1():
	name="alex"
	def func2():
		print(name)
	func2()
func1()#alex
##可用__closure__来检测函数是否是闭包，使用函数名.__closure__返回cell就是闭包，返回None则不是
def func1():
	name="alex"
	def func2():
		print(name)#alex
	func2()
	print(func2.__closure__)#alex (<cell at 0x000000000283A4F8: str object at 0x00000000004BC148>)
func1()

##外部调用闭包
def outer():
	name="alex"
	def inner():
		print(name)
	return inner#返回inner的函数地址
fn=outer()#访问外部函数，获取到内部函数的函数地址
fn()#访问内部函数

##外部访问多层嵌套函数，只需要一层一层的往外层返回
def func1():
	name="alex"
	def func2():
		def func3():
			print(name)
		return func3
	return func2
func1()()()"""

#迭代器iterator
#常见的可迭代对象：str\list\tuple\dic\set
#可迭代协议

#通过dir()查看对象的方法和函数
##列表
lst=[1,3]
print(dir(lst))
##元祖
tuple=(1,2)
print(dir(tuple))
##字典
dic={'a':1,'b':2}
print(dir(dic))
##集合
se={1,2,3,4,5}
print(dir(se))
#range
print(dir(range))

#还可通过isinstence()函数来查看一个对象的类型
l=[1,2,3]
l_iter=l.__iter__()
from collections import  Iterable
from collections import  Iterator
print(isinstance(l,Iterable))#True          查看是不是可迭代对象
print(isinstance(l,Iterator))#False         查看是不是迭代器
print(isinstance(l_iter,Iterator))#True
print(isinstance(l_iter,Iterable))#True

#for机制
s="学无止境"
c=s.__iter__()#获取迭代器
print(c.__next__())#学  使迭代器迭代获取元素
print(c.__next__())
print(c.__next__())
print(c.__next__())
#在输入一次print(c.__next__())则会报错StopIteration，即迭代结束

#while循环和迭代器模拟for循环
lst=[5,4,3]
l=lst.__iter__()
while True:
	try:
		i=l.__next__()
		print(i)
	except StopIteration:
		break







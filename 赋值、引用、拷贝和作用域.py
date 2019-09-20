"""import copy
a=[0,[1,2],3]
b=copy.deepcopy(a)
a[0]=8
a[1][1]=9
print(a)
print(b)
#引用VS拷贝
#没有限制条件的分片表达式（L[:])能够复制序列，但只能进行浅复制
#字典copy方法，D.copy()能够复制字典，但此法只能进行浅复制
#有些内置函数，例如list，能够生成拷贝list（L)
#copy标准库模块能够生成完整拷贝：deepcopy本质上是递归copy
#对于不可变对象和可变对象来说，浅复制是复制的引用，只是应为复制不变对象和复制不变对象的引用是等效的（因为对象不可变，当改变时会新建对象重新赋值）。故看起来浅复制只复制不可变对象（整数、实数和字符串等，对于可变对象，浅复制其实是创建了一个对于该对象的引用，也就是说只是给同一个对象贴上了另一个标签而已。
L=[1,2,3]
D={'a':1,'b':2}
A=L[:]
B=D.copy()
print("L,D")
print(L,D)
print("A,B")
print(A,B)
print("------------------")
A[1]='NI'
B['c']='spam'
print("L,D")
print(L,D)
print("A,B")
print(A,B)



#增强赋值以及共享引用
L=[1,2]
M=L
L=L+[3,4]#此处的第一个L是新建重新定义的L，故M没有复制新定义的L，而是保留原来L的值
print(L,M)#[1,2,3,4] [1,2]
print("---------")
L=[1,2]
M=L
L+=[3,4]
print(L,M)#[1,2,3,4]  [1,2,3,4]   L没有重建定义，故M会随L的值进行变化


#python从2k到3k，语句变函数引发的变量作用域问题
def test():
	a=False
	exec("a=True")
	print("a=",a)
test()

b=False
exec("b=True")
print("b=",b)

print("-------------------")

def test():
	a=False
	ldict=locals()
	exec("a=True",globals(),ldict)#exec(字符串，全局变量（存在则要求为字典对象），局部变量（可以是任何映射对象，若被忽略，则会取与globals相同的值））
	a=ldict['a']
	print(a)#True
test()

b=False
exec("b=True",globals())
print(b)#True
print("b=",b)#b=True
"""



#深入python变量作用域及其陷阱
##不可变对象（不可变指的是值不可变，对不不可变类型的变量，若更改变量会创建一个新值，旧值没有被引用的话就等待垃圾回收。但不可变类型可以计算hash值，作为字典的key）
##可变对象（不需要再重新申请内存，只需要在此对象后面连续申请即可，即它的内存地址会保持不变，但区域会变长或者变短）
a='aaaaaaaa'
id(a)#65442608
a='dfsdgas'
id(a)#62005576
#####需在python console中执行才能显示地址。重新赋值后，变量a的内存地址发生了变化，


a_list=[1,2,3]
id(a_list)#65442888
a_list.append(4)
id(a_list)#65442888
#####list重新赋值后，变量a_list的内存地址并未发生改变

##函数值传递
def func_int(a):
	a+=4
	
def func_list(a_list):
	a_list[0]=4
	
t=0
func_int(t)
print(t)#0

t_list=[1,2,3]
func_list(t_list)
print(t_list)#[4,2,3]   需注意可变对象list与不可变对象int之间的调用

#list的=与append或extend的差别
import sys
import importlib
importlib.reload(sys)

list_a=[]
def a():
	list_a=[1]
a()
print(list_a)#[]

list_b=[]
def b():
	list_b.append(1)
b()
print(list_b)#[1]  =创建了局部变量，而.append()或者.extend()则重用了全局变量

##使用可变的默认参数(!!!永远不要使用可变的默认参数）
def foo(a,b,c=[]):
	c.append(a)
	c.append(b)
	print(c)
foo(1,1)#[1,1]
foo(1,1)#[1,1,1,1]
foo(1,1)#[1,1,1,1,1,1]#同一变量c在函数调用的每一次都被反复引用

#应改为如下代码：
def foo(a,b,c=None):
	if c is None:
		c=[]
		c.append(a)
		c.append(b)
		print(c)
foo(1,1)#[1,1]
foo(1,1)#[1,1]
foo(1,1)#[1,1]




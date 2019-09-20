def func():
	print(11)
	return 22
ret=func()
print(ret)

def func():
	print("12")
	return '函数'
func()


def func1():
	print("hanshu")
	yield '函数hhh'
func1()
print(func1())#<generator object func1 at 0x00000000028098E0>

def func():
	print("111")
	yield 222
	print(333)
	yield 444
	
gener=func()
ret=gener.__next__()
print(ret)#111  222
ret2=gener.__next__()
print(ret2)#333  444
#ret3=gener.__next__()报错print(ret3)

#for循环占用很大内存
def eat():
	lst=[]
	for i in range(1,10000):
		lst.append('food'+str(i))
	return lst
e=eat()
print(e)
#yield使用生成器节省内存空间
def eat():
	for i in range(1,10000):
		yield 'food'+str(i)
e=eat()
print(e.__next__())#food1
print(e.__next__())#food2
#......

#send()
def func1():
	print('1')
	f1=yield '2'
	print(f1)
	f2=yield '3'
	print(f2)
f=func1()
f.__next__()#1
f.send('4')#给f1传值4

#yield from可直接把可迭代对象中的每一个数据作为生成器的结果进行返回
##但写入两个yield from不会产生列表数据交替输出的效果
def func():
	lst1=['1','2','3','4']
	lst2=['5','6','7','8']
	yield from lst1
	yield from lst2
g=func()
for i in g:
	print(i)












































# coding:utf-8


class Foo(object):
	def __init__(self):
		pass
	
	def __getattr__(self, item):
		print(item,end=' ')
		return self
	
	def __str__(self):
		return ""
	
	
foo = Foo()
print(foo.think.different.itcast)
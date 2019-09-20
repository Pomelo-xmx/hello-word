import socketserver
class FTPserver(socketserver.BaseRequestHandler):#定义一个类，继承BaseRequestHandler。进行通讯
	def handle(self):
		print(self)
		print(self.request)#拿到一个conn链接循环
		while True:
			data=self.request.recv(1024)
			print(data.decode('utf-8'))
			self.request.send(data.upper())
			
if __name__=='__main__':
	obj=socketserver.ThreadingTCPServer(('127.0.0.1',8000),FTPserver)#自己的类名
	obj.serve_forever()#链接循环
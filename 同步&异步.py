"""import socket
import select

##########http请求，IO阻塞########
sk=socket.socket()
sk.connect(('www.baidu.com',80,))
print("succeed to connect")
sk.send(b"GET/HTTP/1.0\r\nHost:baidu.com\r\n\r\n")
data=sk.recv(8096)
print(data)
sk.close()

import socket
import select
#########http请求，IO非阻塞########
sk=socket.socket()
sk.setblocking(False)
try:
	sk.connect(('www.baidu.com',80,))#非阻塞，但会报错
	print("succeed to connect")
except BlockingIOError as e:
	print(e)
sk.send(b"GET/HTTP/1.0\r\n\Host:baidu.com\r\n\r\n")
data=sk.recv(8096)
print(data)
sk.close()"""

import socket
import select

class HttpRequest:
	def __init__(self,sk,host,callback):
		self.socket=sk
		self.host=host
		self.callback=callback
		
	def fileno(self):
		return self.socket.fileno()
	
class HttpResponse:
	def __init__(self,recv_data):
		self.recv_data=recv_data
		self.header_dict={}
		self.body=None
		
		self.initialize()
		
	def initalize(self):
		header,body=self.recv_data.split(b'\r\n\r\n',1)
		self.body=body
		header_list=header.split(b'\r\n')
		for h in header_list:
			h_str=str(h,encoding='utf-8')
			v=h_str.split(':',1)
			if len(v)==2:
				self.header_dict[v[0]]=v[1]
				
class AsyncRequest:
	def __init__(self):
		self.conn=[]
		self.connection=[]
		
	def add_request(self,host,callback):
		try:
			sk=socket.socket()
			sk.setblocking(0)
			sk.connect((host,80))
		except BlockingIOError as e:
			pass
		request=HttpRequest(sk,host,callback)
		self.conn.append(request)
		self.connection.append(request)
		
	def run(self):
		while True:
			rlist,wlist,elist=select.select(self.conn,self.connection,self.conn,0.05)
			for w in wlist:
				print(w.host,'succeed to connect')
				tp1="GET/HTTP/1.0\r\n\Host:%s\r\n\r\n" %(w.host,)
				w.socket.send(bytes(tp1,encoding='utf-8'))
				self.connection.remove(w)
			for r in rlist:
				recv_data=bytes()
				while True:
					try:
						chunck=r.socket.recv(8096)
						recv_data+=chunck
					except Exception as e:
						break
				response=HttpResponse(recv_data)
				r.callback(response)
				r.socket.close()
				self.conn.remove(r)
			if len(self.conn)==0:
				break
				
def f1(response):
	print('save at document',response.header_dict)
	
def f2(response):
	print('save at database',response.header_dict)
	
url_list=[
	{'host':'www.youku.com','callback':f1},
	{'host':'v.qq.com','callback':f2},
	{'host':'www.cnblogs.com','callback':f2},
]
req=AsyncRequest()
for item in url_list:
	req.add_request(item['host'],item['callback'])
req.run()
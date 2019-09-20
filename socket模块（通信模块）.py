#套接字（socket):基本上就是一个信息通道，通道两端各有一个程序。通过网络位于不同的计算机，通过套接字和对方
              # 通信socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。
			  #在设计模式中，socket就是一个门面模式，它把复杂的TCPP/IP协议族隐藏在socket接口后面。
			  #对用户来说，一组简单的接口就是全部，让socket去组织数据，以符合指定的协议。
##服务器套接字&客户端套接字

#服务端套接字函数
    #s.bind()  绑定（主机，端口号）到套接字
	#s.listen()  开始TCP监听
	#s.accpet()  被动接受TCP客户的连接，（阻塞式）等待连接的到来
	
#客户端套接字函数
    #s.connect()  主动初始化TCP服务器连接
	#s.connect_ex()  connect（）函数的扩展版本，出错时返回出错码，而不是抛出异常
	

#公共用途的套接字函数
    #s.recv()    接受TCP数据
	#s.send()    发送TCP数据（send在待发送数据量大于己端缓存区剩余空间时，数据丢失，不会发完）
	#s.sendall()  发送完整的TCP数据（本质就是循环调用send，sendall在待发送数据量大于己端缓存区剩余空间时，数据不丢失，循环调用send直到发完）
	#s.recvfrom() 接受UDP数据
	#s.sendto()   发送UDP数据
	#s.getpeername()  连接到当前套接字的远端地址
	#s.getsockname()  当前套接字的地址
	#s.getsockopt()   返回指定套接字的参数
	#s.setsockopt()   设置指定套接字的参数
	#s.close()    关闭套接字
	
#面向锁的套接字方法
    #s.setblocking()   设置套接字的阻塞与非阻塞模式
	#s.settimeout()    设置阻塞套接字操作的超时时间
	#s.gettimeout()    得到阻塞套接字操作的超时时间
	
#面向文件的套接字函数
    #s.fileno()   套接字的文件描述符
	#s.makefile()  创建一个与该套接字相关的文件
	


#基于TCP的通信（单链接服务端和客户端）
"""服务端"""
import socket

IP='127.0.0.1'
PORT=8080
ADDR=(IP,PORT)
#1、创建服务器的socket对象
ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(ser)
#2、设置服务器地址
ser.bind(ADDR)
#3、设置服务端半连接池，同一时刻的最大请求数限制
ser.listen(5)
#4、获取双向链接对象和服务端地址
conn,addr=ser.accept()
print(conn)
print(addr)
#5、收发数据
##接受1024字节数据
data=conn.recv(1024)
conn.send('服务端：已接收数据',encode('utf-8'))
print(data.decode('utf-8'))
#6、断开客户端链接
conn.close()
#7、关闭服务器（一般不关闭）
ser.close()


"""客户端"""
import socket

IP='127.0.0.1'
PORT=8080
ADDR=(IP,PORT)
#1、创建客户端的socket对象
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2、连接服务器地址
cli.connect(ADDR)
#3、收发数据
cli.send('客户端：发送消息'.encode('utf-8'))
#接受1024字节数据
data=cli.recv(1024)
print(data.decode('utf-8'))
#4、关闭客户端
cli.close()
























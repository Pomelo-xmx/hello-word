import socket
BUFSIZE=1024
udp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

qq_name_dic={
	'A':('127.1.0.1',8080),
	'B':{'127.0.0.1',8080},
	'C':{'127.0.1.1',8080},
	'D':{'127.1.1.1',8080},
}

while True:
	qq_name=input('请选择聊天对象：').strip()
	while True:
		msg=input('请输入消息，回车发送，输入q结束和他的聊天：').strip()
		if msg=='quit':break
		if not msg or not qq_name or qq_name not in qq_name_dic:continue
		udp_client_socket.sendto(msg.encode('utf-8'),qq_name_dic[qq_name]B)
		#必须带着自己的地址，udp不需要建立连接，但是要带着自己的地址给服务端，否则服务端无法判断是谁给我发的
		#消息，并且不知道该把消息回复到什么地方，因为两者没有建立连接通道
		
		back_msg,addr=udp_client_socket.recvfrom(BUFSIZE)#同样是阻塞状态，等待接收消息
		print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m'%(addr[0],addr[1],back_msg.decode('utf-8')))
		
udp_client_socket.close()
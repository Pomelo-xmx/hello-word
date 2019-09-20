import socket
ip_port=('127.0.0.1',8080)
BUFSIZE=1024
udp_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server.bind(ip_port)
while True:#udp无链接，只需实现通信循环
	data,addr=udp_server.recvfrom(BUFSIZE)
	print(data.decode('utf-8'),addr)
	msg=input(">>:")
	udp_server.sendto(msg.encode('utf-8'),addr)
	udp_server.sendto(data.upper(),addr)#此处的addr是指服务端传来的数据的ip_port
udp_server.close()

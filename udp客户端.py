import socket
ip_port=('127.0.0.1',8080)
BUFSIZE=1024
udp_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	msg=input('>>:').strip()
	udp_client.sendto(msg.encode('utf-8'),ip_port)#每次发包都要指定端口
	
	data,addr=udp_client.recvfrom(BUFSIZE)
	print(data.decode('utf-8'),addr)
udp_client.close()
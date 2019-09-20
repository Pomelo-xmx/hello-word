import socket
ip_port=('127.0.0.1',8081)
BUFSIZE=1024
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind((ip_port))
phone.listen(5)
print("start...")

while True:
	conn,addr=phone.accept()
	print('接到来自%s的电话'%addr[0])
	while True:
		client_msg=conn.recv(BUFSIZE)
		if len(client_msg)==0:break
		print('client_msg:%s'%client_msg)
		conn.send(client_msg.upper())
	conn.close()
phone.close()


import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_port=('127.0.0.1',8081)
BUFSIZE=1024
phone.connect_ex(ip_port)

while True:
	client_msg=input('>>:').strip()
	if len(client_msg)==0:continue
	phone.send('hello'.encode('utf-8'))
	
	backmsg=phone.recv(BUFSIZE)
	print(backmsg.decode('utf-8'))

phone.close()
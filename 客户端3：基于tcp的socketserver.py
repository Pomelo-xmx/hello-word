import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))

while True:
	msg=input(">>:").strip()
	if not msg:continue
	s.send(msg.encode('utf-8'))
	data=s.recv(1024)
s.close()

import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.1.1',8080))

phone.send('xxxxxhello'.encode('utf-8'))
back_msg=phone.recv(1024)
print(back_msg.decode('utf-8'))

phone.close()
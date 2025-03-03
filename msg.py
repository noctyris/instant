import socket

PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",PORT))
s.listen(5)

print('Connection created on port %s'%PORT)

while 1:
	c, addr = s.accept()
	print('Connection received:', addr[0])
	c.close()
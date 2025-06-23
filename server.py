import socket

s = socket.socket()
print('Server Created')

s.bind(('localhost',9999))
s.listen(3)
print('waaiting for connections')

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with',addr,name)
    c.send(bytes('Welcome to Malos Technologies','utf-8'))
    c.close()
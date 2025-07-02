import socket

s = socket.socket()

print('socket Created')

# accepting the connection
s.bind(('localhost', 9999))

s.listen(3)
print('waiting for connections')

while True:
    # client and address
    c, addr = s.accept()
    name = c.recv(1024).decode()

    print('connected with ', addr, name)

    c.send(bytes('welcome to malos', 'utf-8'))

    c.close()

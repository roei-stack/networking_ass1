import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 12345))
while True:
    data, address = s.recvfrom(1024)
    print(str(data))
    s.sendto(data, address)

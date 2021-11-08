import os.path
import socket
import sys

# todo add system arguments
serverIp = "127.0.0.1"
serverPort = 12345
filename = "vvvv"

if not os.path.isfile(filename):
    raise ValueError('Error: Invalid file path')
# opening the file
file = open(filename, "r")

# opening udp socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:



socket.close()

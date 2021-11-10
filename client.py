import os.path
import socket
import sys

MAX_FILE_SIZE = 50000
MSS = 100

SERVER_IP = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
ADDRESS = (SERVER_IP, SERVER_PORT)
FILE_NAME = sys.argv[3]

# making sure the file name given exists
if not os.path.isfile(FILE_NAME):
    raise ValueError('Error: Invalid file name/path')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file = open(FILE_NAME, "r")

chunk = ''
while True:
    # encoding a string adds 2 bytes to it's length
    chunk = bytes(file.read(MSS), encoding='ascii')
    if not chunk:
        break
    received = b''
    while received != chunk:
        socket.sendto(chunk, ADDRESS)
        received, address = socket.recvfrom(MSS + 1)

file.close()
socket.close()

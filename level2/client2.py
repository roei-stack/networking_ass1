import os.path
import socket
import sys

MAX_FILE_SIZE = 50000
MSS = 100

SERVER_IP = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
ADDRESS = (SERVER_IP, SERVER_PORT)
FILE_NAME = sys.argv[3]

def send(toSend, sock):
    accepted = False
    sock.settimeout(1)

    while not accepted:
        sock.sendto(toSend, ADDRESS)
        try:
            data, _ = sock.recvfrom(MSS)
            # ignoring confirmations for privius packages
            while int(data[0:4]) < int(toSend[0:4]):
                data, _ = sock.recvfrom(MSS)
            accepted = True
        except socket.timeout:
            pass



def main():
    # keeping track of how much we sent
    sent = 0

    # making sure the file name given exists
    if not os.path.isfile(FILE_NAME):
        raise ValueError('Error: Invalid file name/path')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    file = open(FILE_NAME, "r")

    while chunk := bytes(file.read(MSS - 4), encoding='ascii'):
        toSend = bytes(sent) + chunk
        send(toSend, sock)

    file.close()
    socket.close()
### end of main

if __name__ == "__main__":
    main()
import os.path
import socket
import sys

MAX_FILE_SIZE = 50000
MSS = 100

SERVER_IP = sys.argv[1]
SERVER_PORT = 0
try:
    SERVER_PORT = int(sys.argv[2])
except:
    print("invalid port number")
    exit(0)
ADDRESS = (SERVER_IP, SERVER_PORT)
FILE_NAME = sys.argv[3]
# making sure the file name given exists
if not os.path.isfile(FILE_NAME):
    print("invalid file path")
    exit(0)

def send(toSend: bytes, sock: socket):
    accepted = False
    sock.settimeout(1)

    while not accepted:
        try:
            sock.sendto(toSend, ADDRESS)
        except:
            print("error sending, try again")
            exit(0)
        try:
            data, _ = sock.recvfrom(MSS)
            # ignoring confirmations for privius packages
            while int.from_bytes(data[0:4], byteorder='little') < int.from_bytes(toSend[0:4], byteorder='little'):
                data, _ = sock.recvfrom(MSS)
            accepted = True
        except socket.timeout:
            pass



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    file = open(FILE_NAME, "r")

    # keeping track of how much we sent
    sent = 0
    while chunk := bytes(file.read(MSS - 4), encoding='ascii'):
        # adding the serial number to the start of the packege. (4 bytes for sent is enough because the max file size is only 50kb)
        toSend = sent.to_bytes(4, byteorder='little') + chunk
        send(toSend, sock)
        sent += 1

    file.close()
    sock.close()
### end of main

if __name__ == "__main__":
    main()
import socket
import sys

BUFFER_LEN = 127

def main():
    printed = 0

    try:
        PORT = int(sys.argv[1]) # argv[1] is our port
    except:
        print("invalid port")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind(('', PORT))
    except:
        print("error binding to port")
        return

    # we work in stop&wait. the server only need to know how much packeges he printed (to avoid printing the same twice).
    while True:
        data, address = s.recvfrom(BUFFER_LEN)
        # the first 4 bytes are int which represent the serial number of this packege.
        num = int.from_bytes(data[0:4], byteorder='little')
        if num > printed:
            print(data[4::].decode('ascii'), end=None)
            printed = num
        # sending back to the client
        try:
            s.sendto(data, address)
        except:
            print("error sending")
            return
### end of main

if __name__ == "__main__":
    main()
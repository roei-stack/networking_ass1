import socket
import sys

BUFFER_LEN = 127

def main():
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
    
    while True:
        data, address = s.recvfrom(BUFFER_LEN)
        print(str(data))
        try:
            s.sendto(data, address)
        except:
            print("error sending")
            return
# end of main

if __name__ == "__main__":
    main()

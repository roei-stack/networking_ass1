import socket
import sys

BUFFER_LEN = 127


def init_socket(port_str: str, ip: str):
    port = 0
    try:
        port = int(port_str)  # argv[1] is our port
        # The network port number is an unsigned 16-bit integer, which can be no more than 65535
        assert 0 <= port <= 65535
    except Exception as e:
        print('invalid port')
        print('Error info: ', e)
        exit(0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((ip, port))
    except Exception as e:
        print('error binding to port')
        print('Error info: ', e)
        exit(0)
    return sock


def send(sock: socket.socket, data: bytes, address):
    # sending back to the client
    try:
        sock.sendto(data, address)
    except Exception as e:
        print('error sending')
        print('Error info: ', e)
        exit(0)


def main():
    s = init_socket(sys.argv[1], '')
    printed = 0
    # we work in stop&wait. the server only need to know how much packages he printed
    # to avoid printing the same twice.
    while True:
        data, address = s.recvfrom(BUFFER_LEN)
        # the first 4 bytes are int which represent the serial number of this package.
        num = int.from_bytes(data[0:4], byteorder=sys.byteorder)
        if num > printed:
            print(data[4::].decode('ascii'), end='')
            printed = num
        send(s, data, address)


# end of main
if __name__ == '__main__':
    main()

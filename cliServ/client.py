__author__ = 'MichaelWomack'

from socket import socket
from server import server_port, encoding
from utility import formatData

if __name__ == "__main__":
    sock = socket()
    sock.connect(('127.0.0.1', server_port()))
    print("Connection made")

    a = 0
    b = 1
    poly = [-6, 14, -7, 1]
    tolerance = .01

    data = "S" + formatData([a, b, poly, tolerance])
    sock.sendall(str(data).encode(encoding))
    sock.shutdown(1)   # shutdown the sending side of the socket

    response_str = ""
    bytes = sock.recv(2048)
    while len(bytes) > 0:
        response_str += bytes.decode(encoding)
        bytes = sock.recv(2048)

    print("Response: ", response_str)
    sock.close()


    #reconnect socket
    sock = socket()
    sock.connect(('127.0.0.1', server_port()))
    print("Connection made")

     # second request
    x = response_str[2:]
    data = "E" + formatData([x, poly])

    sock.sendall(data.encode(encoding))
    sock.shutdown(1)

    response_str = ""
    bytes = sock.recv(2048)
    while len(bytes) > 0:
        response_str += bytes.decode(encoding)
        bytes = sock.recv(2048)

    print("Response:" , response_str)
    sock.close()
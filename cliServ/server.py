__author__ = 'MichaelWomack'

from socket import socket
from polynomial import eval, bisection

def server_port():
    return 12321

encoding = 'UTF-8'


if __name__ == "__main__":

    # setting up a listener socket
    sock = socket()   # this is how you create a new object,
    sock.bind(('', server_port()))
        #  ('', server_port())  is the socket 'address'
        # ''  is the host, which is all possible addresses
        # server_port() is the port number, 12345
    sock.listen(0)  # 0 backlog of connections


    while True:
        (conn, address) = sock.accept()
        # we now have a connection
        # conn is a socket we can use to communicate
        # address is the address of the client


        print("connection made ", conn)
        print(address)

        # conn is a socket that will be used to communicate with the client

        # get data from client (request)
        data_string = ""
        bytes = conn.recv(2048)
        while len(bytes) > 0:
            # we actually got data from the client
            bytes_str = bytes.decode(encoding)
            print("data received: |{}|".format(bytes_str))
            data_string += bytes_str
            bytes = conn.recv(2048)

        print("all data received: " + data_string)

        values = data_string.split(' ')
        print("values: ", values)

        response = ""
        data = []

        try:
            # remove letter E or S from first Argument and parse it to float
            data.append(float("".join(values[0][1:])))

            # parse remaining polynomial arguments to floats
            for arg in values[1:]:
                data.append(float("".join(arg)))

        except TypeError as msg:
            response = "X:TypeError - " + str(msg)

        except ValueError as msg:
            response = "X:ValueError - " + str(msg)

        # if an error has not already occurred
        if response is "":
            # Error check: must have params length of at least 2
            if values[0][:1] is "E":
                if len(data) < 2:
                    response = "X:Invalid argument length - must have (x, poly)"
                else:
                    x = data[0]
                    poly = data[1:]
                    response = "E" + str(eval(x,poly))

            # Error check: must have params length of at least
            elif values[0][:1] is "S":
                if len(data) < 4:
                    response = "X:Invalid argument length - must have (a, b, poly, tolerance)"
                else:
                    a = data[0]
                    b = data[1]
                    poly = data[2: len(data)-1]
                    tolerance = data[len(data) -1]
                    response = "S" + str(bisection(a, b, poly, tolerance))

            else:
                response = "X:Invalid Operation Code |" + values[0][:1] + "|"

        conn.sendall(str(response).encode(encoding))
        conn.shutdown(1)  ## shutdown the sending side
        conn.close()
        print("connection closed")

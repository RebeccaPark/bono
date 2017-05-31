import socket


# TODO: def parse_request(data: string) -> Request:


def get_request(sock):
    connection, _ = sock.accept()
    data = ""
    while True:
        chunk = connection.recv(1024)
        data += chunk.decode()
        if len(chunk) < 1024:
            break

    return connection, parse_request(data)


# TODO: def handle_request(request: Request) -> string:


def serve(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((address, port))
    sock.listen(0)
    
    while True:
        connection, request = get_request(sock)
        response = handle_request(request)
        connection.sendall(response)
        connection.close()

def render_template(name):
    return open(name).read()


def main():
    serve("127.0.0.1", 8080)


if __name__ == "__main__":
    main()

import socket

address = ("0.0.0.0", 5000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(address)

server_socket.listen(5)
print(f"Server listening on {address[0]}:{address[1]}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established!")

    message = "Welcome to the server!"
    client_socket.send(message.encode())

    client_socket.close()
import socket

server_address = ("0.0.0.0", 5000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Receive the welcome message from the server
received_message = client_socket.recv(1024).decode()
print(f"Received: {received_message}")

client_socket.close()

import socket
import threading

bind_ip="127.0.0.1"
bind_port=9090

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print("I'm  listening on %s in the port %d" % (bind_ip,bind_port))

def handle_client(client_socket):
	request = client_socket.recv(4096)
	client_socket.send("ACK!".encode())
	client_socket.close()

while True:
	client, addr = server.accept()
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
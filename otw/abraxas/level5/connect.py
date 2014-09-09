import socket
import sys 
import ssl

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
received = ""
response = ""
cli.bind(('localhost', 21122))
cli.listen(5)
conn, addr = cli.accept()
received = conn.recv(2048)
print "Received: " + received.encode("hex") + "\n"
server.connect(('localhost', 2112))
server.sendall(received)
response = server.recv(2048)
print "Server response: " + response.encode("hex") + "\n"
conn.sendall(response)
received = conn.recv(2048)
print "Received: " + received.encode("hex") + "\n"
server.sendall(received)
response = server.recv(2048)
print "Server response: " + response.encode("hex") + "\n"
conn.sendall(response)
received = conn.recv(2048)
print "Received: " + received.encode("hex") + "\n"
server.sendall(received)
response = server.recv(2048)
print "Server response: " + response.encode("hex") + "\n"
conn.sendall(response)
received = conn.recv(2048)
print "Received: " + received.encode("hex") + "\n"
server.sendall(received)
response = server.recv(2048)
print "Server response: " + response.encode("hex") + "\n"

server.close()
cli.close()

import socket
import sys 
import ssl

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_client():
	cli.bind(('localhost', 21122))
	cli.listen(5)
	global conn
	conn, addr = cli.accept()
	print "Client connected..."

def connect_server():
	server.connect(('localhost', 2112))
	print  "Server connected..."
	server.settimeout(3.0)

def close():
	server.close()
	cli.close()

def craft_client_hello(craft):
	try:
		received = conn.recv(2048)
		try:
			replaced = list(received)
			old_tot = ord(received[1]) 
			old_cip = ord(received[6])
			delta = old_tot - old_cip
			del replaced[21:24]
			new_tot = len(replaced)-2
			new_cip = new_tot - delta
			replaced[1] = chr(new_tot)
			replaced[6] = chr(new_cip)
			replaced= "".join(replaced)
			print "Original client hello: %s\n\nCrafted client hello: %s\n" % (received.encode("hex"), replaced.encode("hex"))
		except:
			print "something went wrong...\n"
		if craft is not True:
			print "\n\nString will be untouched!!!!\n\n"
			server.sendall(received)
		else:
			server.sendall(replaced)
		server_passthrough()
	except:
		print" Client closed, quitting..."
		close()
	
def server_passthrough():
	try:
		response = server.recv(2048)
		print "Server response: %s\n" % (response.encode("hex"))
		conn.sendall(response)
		client_passthrough()
	except:
		print "Server closed, quitting..."
		close()

def client_passthrough():
	try:
		received = conn.recv(2048)
		print "Client response: %s\n" % (received.encode("hex"))
		server.sendall(received)
		server_passthrough()
	except:
		print "Client closed, quitting..."
		close()

connect_client()
connect_server()
craft_client_hello(False)

close()


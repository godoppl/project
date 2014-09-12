import socket, ssl, threading

check = 1 
class Server(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		print "server started!"
		self.deamon=True
		self.start()

	bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	bindsocket.bind(('localhost', 21123))
	
	bindsocket.listen(5)
	
	def deal_with_client(name, connstream):
	    data = connstream.read()
	    # null data means the client is finished with us
	    while data:
		if not data:
			break
	        else: 
			print data
		data = ""
	#	print data
	
	def run(self):
		check = 1
		while check is 1:
			connection, fromaddr = self.bindsocket.accept()
			rec = connection.recv(2048)
			print fromaddr
			print rec
			check = 0
		return 0		
	def sslfunc(self):
		while True:
			try:
				newsocket, fromaddr = self.bindsocket.accept()
				connstream = ssl.wrap_socket(newsocket, server_side=True, certfile="/tmp/lev5/ssl/server.crt", keyfile="/tmp/lev5/ssl/private.key", ssl_version=2)
				try:
				        self.deal_with_client(connstream)
				finally:
			       		connstream.shutdown(socket.SHUT_RDWR)
			        	connstream.close()
			except:
				print "server error..."
				break
		return 0	
		
print "server starting..."
Server()
def terminal():
	global check
	print check
	console = raw_input("> ")
#	if console is "exit":
#		return 0


import socket


key = "dfs!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.66.67", 4373))
data = ""
l = 0
#print longkey
while l<=120:
	received = s.recv(4)
	for i in range(len(received)):
		data += chr(ord(received[i]) ^ ord(key[i]))
	l += 1
print data



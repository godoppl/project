#!/usr/bin/env python
#
#

import socket


s = socket.socket()
s.connect(("semtex.labs.overthewire.org", 24001))

binary = open('binary', 'w')	

#i=0
while True:
	data = s.recv(32678)
#	i += 1
#	if i %2==0:
	binary.write(data)
	if not data: break
s.close

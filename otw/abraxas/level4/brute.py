#!/usr/bin/env python
import string
import itertools
import binascii

#char = string.ascii_letters
#print char.__len__()
char = []
string = ""
for i in range(16,256):
	hexchar = hex(i)
	hexchar = hexchar.lstrip('0x')
	char.append(hexchar)
for i in range(150, char.__len__()):
	hexstring = char[i]
	string = string + binascii.unhexlify(hexstring)
#	print string + " <--> " + string.encode("base64")

print string

def bruteforce(charset):
	return (''.join(candidate) 
		for candidate in itertools.chain(itertools.product(charset, repeat=4)))
current = list(bruteforce(string))
for i in range(1, current.__len__()):
	for j in range(0,3):
		newstring = "A"*j + current[i]
		print binascii.hexlify(newstring) + " : " + newstring.encode("base64")

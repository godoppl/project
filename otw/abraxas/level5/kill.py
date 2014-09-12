#!/usr/bin/python2.7

from socket import socket
import ssl
import sys

s = socket()
c = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/tmp/lev5/cert.pem', ciphers='ALL:eNULL', ssl_version=2)
#c = ssl.wrap_socket(s, ciphers='ALL:eNULL', ssl_version=2)
# maybe this is port 2112 in the future ? see meeting !
c.connect(('0.0.0.0', 21123))

cert = c.getpeercert()
k,v = cert['subject'][5][0]

if k == 'commonName' and v == 'abraxas.dildosfromspace.com':
    print "yay!"
else:
    print "Failed!"
    sys.exit(0)
c.write('Password\n')
print c.recv()
c.close()


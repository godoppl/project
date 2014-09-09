#!/usr/bin/env python
#
#

import socket
import Queue
import threading
import time

socket.timeout(10)

host = "127.0.0.1"
port = 24027
password = "HELICOTRMA"
signature = "AGENTRANDM"

def xor_strings(s1, s2):
    return ''.join([chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(s1, s2)])

class actionThread (threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
	def run(self):
		DoIt(self.name, self.q)

def DoIt(threadName, q):
	while True:
		queueLock.acquire()
		if not workQueue.empty():
			idx = q.get()
			queueLock.release()
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			print "Started socket: %s %s"%(idx,host)
			s.bind((idx, 0))
			s.connect((host, port))
			data = s.recv(10)
			print "Received: " + repr(data)
			xordata = xor_strings(data, password)
			s.send(bytearray(xordata + signature))
			time.sleep(5)
			data = s.recv(256)
			print "Received new password: " + data
			s.close()
		else:
			queueLock.release()

threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", "Thread-6", "Thread-7", "Thread-8", "Thread-9", "Thread-10"]
ip_index = ['127.0.0.10', '127.0.0.11', '127.0.0.12', '127.0.0.13', '127.0.0.14', '127.0.0.15', '127.0.0.16', '127.0.0.17', '127.0.0.18', '127.0.0.19']
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
	thread = actionThread(threadID, tName, workQueue)
	threads.start()
	threads.append(thread)
	threadID += 1

queueLock.acquire()
for idx in ip_index:
	workQueue.put(idx)
queueLock.release()

while not workQueue.empty():
	time.sleep(1)
	pass

for t in threads:
	t.join()


print "All done"


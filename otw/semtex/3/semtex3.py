import random
import numpy


def DoIt():
	result = 0
	i = 0
	combo = "Combination is:"
	while (result == 0):
		keypress = random.randint(1,8)
		i += 1
		combo = combo + str(keypress)
		Numbers[0]+=Numbers[keypress]	
		if numpy.array_equal(Numbers[0], Numbers[9]):
			print combo
			result = 1
		for l in range(0,5):
			if Numbers[[0],[l]] >= 1000 or Numbers[[0],[l]] <= -1000:
				Numbers[0] = [300, 300, 300, 300, 300]
				combo = "Combination is:"
	print Numbers[0]

Numbers = numpy.array([[300, 300, 300, 300, 300],[5, 2, 1, 7, 5], [13, -7, -4, 1, 5], [9, 12, 9, 70, -4], [-11, 9, 0, 5, -13], [4, 17, 12, 9, 24], [11, -17, 21, 5, 14], [15, 31, 22, -12, 3], [19, -12, 4, 3, -7], [400, 400, 400, 400, 400]])

DoIt()



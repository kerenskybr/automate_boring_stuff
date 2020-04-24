import logging

#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(message)s')


#logging.disable(logging.CRITICAL)

logging.debug('Start')


def factorial(n):
	logging.debug('Start factorial')
	total = 1
	for i in range(1, n + 1):
		total *= i
		logging.debug('i is %s, total is %s' % (i, total))

	logging.debug('Return total is %s' % (total))
	return total

print(factorial(5))
logging.debug('end')
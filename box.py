def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception("Symbol needs to be only one")

	if (width < 2) or (height < 2):
		raise Exception("width and height need to be high than 2")

	print(symbol * width)

	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)

	print(symbol * width)

boxPrint(".", 20, 5)

'''
import traceback
try:
	raise Exception('This is the error message.')
except:
	errorFile = open('errorInfo.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written to errorInfo.txt.')

'''



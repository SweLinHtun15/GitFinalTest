#Raising Exception

class ShortInputExceptions(Exception):
	'''A user-defined exception class'''

	def __init__(self, length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something-->')
	if len(text) < 3:
		raise ShortInputExceptions(len(text), 3)
	elif len(text) > 10:
		raise LongInputExceptions(len(text), 10)
		#Other work can continue as usual here

except EOFError:
		print('Why did you do an EOF on me?')

except ShortInputExceptions as ex:
		print(('ShortInputExceptions:The input was' +
			'{0}long, excepted at least {1}')
		.format(ex.length, ex.atleast))

except LongInputExceptions as lex:
		print(('LongInputExceptions: The input was' + 
			'{0} long, excepted at least {1}')
		.format(lex.length, ex.atleast))
else:
		print('No exception was raised')


# import time

# f = none
# try:
# 	f = open('poem.txt')

# 	#Our usual file-reading idiom

# 	while True:
# 		line = f.readline()
# 		if len(line) == 0:
# 			break
# 		print(line, end=' ')
# 		sys.stdout.fludh()
# 		print("Press clrt+c now")

# 		#To make sure it runs for a while

# 		time.sleep2()

# except IQError:

# 		print("Could not find poem.txt")

# except KeyboardInterrupt:
# 	print("!! You cancelled the reading from the file")

# finally:
# 	if f:
# 		f.close()
# 	print("(Cleaning up: Clean the file)")

# #tutorial/errors.html
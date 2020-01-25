#keyboardInterrupt eg, passwords

# while True:
# 	try:
# 		x = int(input('Please enter a number: '))
# 		print(x)
# 		break
# 	except ValueError:
# 		print("Oops! That was no valid number. Try again...")
# ----------------------------------------------------------

#OSError, ValueError

import sys
try:
     f = open('myfile.txt')
     s = f.readline()
     i = int(s.strip())
except OSError as err:
     print("OS Error: {0}". format(err))
except ValueError:
     print("Could not comvert data to integer.")
except:
     print("Unexcepted error:", sys.exc_info()[0])
     raise

#EOFError,keyboardInterrupt

try:
	text = input('Enter Something-->')
except EOFError:
	print('Why did you do an EOF in me?')
except KeyboardInterrupt:
	print('You cancelled the operation.')
else:
	print('You entered.{}'.format(text))

#Raising Exception

class ShortInputExceptions(Exception):
	'''A user-defined exception class'''

	def__init__(self, length,atleast):
		Exception.__init___(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something-->')
	if len(text) < 3:
		raise ShortInputExceptions(len(text), 3)
		#Other work can continue as usual here

	except EOFError:
		print('Why did you do an EOF on me?')

	except ShortInputExceptions as ex:
		print(('ShortInputExceptions:The input was' +
			'{0}long, excepted at least{1}')
		.format(ex.length, ex.atleast))
	else:
		print('No exception was raised')

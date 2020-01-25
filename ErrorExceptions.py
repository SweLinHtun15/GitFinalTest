#keyboardInterrupt eg, passwords

# while True:
# 	try:
# 		x = int(input('Please enter a number: '))
# 		print(x)
# 		break
# 	except ValueError:
# 		print("Oops! That was no valid number. Try again...")
----------------------------------------------------------

#OSError, ValueError

import sys
try:
...     f = open('myfile.txt')
...     s = f.readline()
...     i = int(s.strip())
... except OSError as err:
...     print("OS Error: {0}". format(err))
... except ValueError:
...     print("Could not comvert data to integer.")
... except:
...     print("Unexcepted error:", sys.exc_info()[0])
...     raise

	
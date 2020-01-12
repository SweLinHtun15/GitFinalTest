# Fibonacci

# Fibonacci numbers module

# n = int(input("Please enter a number:"))

def fib(n):  # write Fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

# fib(200)

#Go to Fibonacci powerpoint

def fib2(n):	# return series up to n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

# fib2(200)		



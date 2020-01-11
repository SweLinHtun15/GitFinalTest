#loops

- While loops
- for loops

Condition is true, while loop excute a set of statements

x = 1
while x < 7:
		print(x)
		x += 1

while loops reqiure variable ready.

x = 1
while x < 7:
		print(x)
		if x == 5:
				break
		x += 1

============================================
For loops

# for loops is iterating over a sequence

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
		print(x)

#looping in a string

for x in "pineapple":
	print(x)

# the break statement

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)
	if x == "pineapple":
		break

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pineapple":
		break
	print(x)

	# The continue Statement - stop the current iteration

	fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
	for x in fruits:
		if x == "pineapple":
			continue
		print(x)

# The range() function - a set of code specified number of times

for x in range(10):
	print(x)

for x in range(10, 100):
	print(x)

for x in range(10, 100, 5):
	print(x)

#range() count from 0
#len() count from 1


# Nested loops

numberA = [1, 2, 3, 4, 5]
numberB = [1, 2, 3, 4, 5]

for x in numberA:
		for y in numberB:
			print(x,y)
-----------
#Pass

for x in [1, 2, 3, 4, 5]:
	pass
------------

words = ["cat", "window", "defenstrate"]
for w in words:
		print(w, len(w))
--------------

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equal', x, '*', n//x)
			break
		else:
			#loop fell through without finding a factor
			print(n, 'is a prime number')

---------------

for num in range(2, 10):
	if num % 2 == 0:
		print("found an even number", num)
		continue
	print("Found a number", num)

-----------------

>>> Fibonacci #module folder

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end= ' ')
		a, b = b, a+b
	print()
	
fib(200)

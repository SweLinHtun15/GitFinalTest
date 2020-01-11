#Boolean espression

print(28 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions

Equals					 -> x == y
Not Equals				 -> x != y
Less than				 -> x <  y
Less than or equal to	 -> x <= y
Greater than			 -> x >  y
Greater than or equal to -> x >= y

Boolean or 				 -> x or y, x | y
Boolean and 			 -> x and y, x & y
Boolean not 			 -> not x

#if statament

x = 70
y = 60

if x > y:
	print("x is greater than y")

#elif

x = 70
y = 60
if x > y:
...     print("x is greater than y")
... elif x == y:
...     print("x and y are equal")

 x = 50
 y = 150
 if x > y:
    print("x is greater than y")
 elif x == y:
    print("x and y are equal")
 else:
    print("x is less than y")

#Short Hand If

if x > y: print("x is gerater than y")

# Short Hand If...Else

x = 50
y = 150
print(x) if x > y else print(y)

#and is logical operater

x = 50
y = 40
z = 100
if x > y and z > x:
	print("All Conditions are True")
else:
	print("All Conditions are False")

#or is logical operater

x = 50
y = 40
z = 100
if x > y or z > y:
	print("one of the Conditions is True")
elif x > y and z > y:
	print("All Conditions are True")
else:
	print("nothing else")

#Nested If is if statements in if statement

x = 50
 if x > 10:
 	print("x is ten")
 	if x > 20:
 		print("x is Greater than 20")
 	else:
 		print("No, x is greater than 20")

 # pass statement

 x = 100
 y = 50
 
 if x > y:
 	pass

x = int(input("Please enter an integer"))

if x < 0:
	x = 0
	print('negative change to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

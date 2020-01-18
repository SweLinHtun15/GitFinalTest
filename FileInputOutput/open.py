# "r" - Read

# "a" - Append

# "w" -  Write

# "x" - Create

# "t" - Text

# "b" - Binary

#open & Read file

f = open('test.txt', 'r') # R - Read
print(f.name)
f.close()


with open('test1.txt', 'a') as g:

	g.write('This is line number 6'+"\n")

	print(g,end='')


with open('test.txt', 'r') as f:

	f_text = f.readline()	  #readline = read each line
	print(f_text,end='')

	f_text = f.readline()
	print(f_text,end='')


	for f_text in f:		  #read all by looping
		print(f_text,end='')


	f_text = f.read(60)	 	  #.read = read no. of words
	print(f_text,end='')


	
	f_text = f.read(100)
	

	while 100 > 0:			   # Loop 100 words each time
		print(f_text,end='')

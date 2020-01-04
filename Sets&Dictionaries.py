#Sets

#include a data type for sets
#Curly braces on the set() function can be used create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

#Demonstrates set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazm')
a 				# unique letter in a
a - b 			# letter in a but not in b
a | b 		    # letters in a or b or both
a & b  			# letters in both a and b
a ^ b  			# letters in a or b but not both

a = {x for x on 'abracadabra' if x not in 'abc'}
a

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape", "water melon")
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits


>>>Dictionaries

#Dictionaries

#Another useful data type bulit into python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

dict([('sape', 4098,),('guido', 4139), ('irv', 3123)])
dict(sape=4139, guido=4127, jack=4098)

{x: x**2 for x in (2,4,6)}
{x: x**3 for x in (1,2,3,4,5)}

#when looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
		print(k,v)

for i, v in enumerate(['tic','toc','toe'])
print(i,v)

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy graill', 'blue']
for q, a in zip(questions, answers):
...     print('What is your{0}? It is {1}.'.format(q,a))


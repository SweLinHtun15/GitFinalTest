#Tuple

Tuple = ()
t = 12345,54321, 'hello'
t[0]

t

#tuple may be nested
u = t, (1,2,3,4,5)
u 

# Tuples are immuted
t[0] = 88888

# but they can contain mutable objects
v = ([1,2,3],[3,2,1])
v

fruits = ('apple', 'banana', 'cheery', 'orange', 'kiwi', 'melon', 'mango')
print(fruits[2:5])

# change Tuples Values
x = ("apple", "banana", "cherry", "orange")
y = list(x)
y[1] = "mango"
x = tuple(y)
x

fruits = ('apple', 'banana', 'cheery', 'orange', 'kiwi', 'melon', 'mango')
x[4] = "pineapple"
fruits
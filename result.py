int(input("Examination Result :"))

100 - 90 		- A
89 - 70 		- B
69 - 60 		- C
59 - 40 		- D
39 - 10 		- Fail

if x >= 90 and x <= 100:
	print("A")
elif x >= 70 and x <= 89:
	print("B")
elif x >= 60 and x <= 69:
	print("C")
elif x >= 40 and x <= 59:
	print("D")
elif x >= 10 and x <= 39:
	print("Fail")
else:
	print("Wrong")

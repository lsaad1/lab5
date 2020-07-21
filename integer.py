Input = raw_input("Enter a number: \n ")
print(Input)
print("input type")
print(type(Input))
try:
	a = int(Input)
	print("number conversion: \n")
	print(a)
	print("converted to type:")
	print(type(a))
except:
	print("Sorry, not an INT")
 
             


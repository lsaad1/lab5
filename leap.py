Input = raw_input("Enter a year: \n")
year = int(Input)
if ((year % 100 == 0) and (year % 400 == 0)):
	print("%d is a leap year.\n" % year)
elif(year % 4 == 0):
	print("%d is a leap year.\n" % year)
else:
	print("%d is not a leap year.\n" % year)


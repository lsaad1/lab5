oneTo9 = ['zero','one','two','three','four','five','six','seven','eight','nine']
elevento19 = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen',
'seventeen','eighteen','nineteen']
tens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty',
'ninety','one hundred']

number = input('Enter number: ')
number = int(number)
if number < 10:
	print("Number is: ", oneTo9[number])
elif number < 20 and number > 10:
	print("Number is: ", elevento19[number % 10 - 1])
elif number % 10 == 0:
	print("Number is: ",tens[int(number / 10)-1])
else:
	tens = tens[int(number / 10) -1]
	oneTo9 = oneTo9[number  % 10]
	print tens, "-" ,oneTo9

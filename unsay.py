OneTo9 = ['zero','one','two','three','four','five','six','seven','eight','nine']
elevenTo19 = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen',
'seventeen','eighteen','nineteen']
tens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty',
'ninety']

def find(str):
  try:
    temp = OneTo9.index(str)
  except:
    try:
      temp = elevenTo10.index(str)+11
    except:
      temp = tens.index(str)+1
      temp = temp * 10
  return temp;

number=raw_input('Enter a string number: ')
number=number.split(' ')
n = len(number)
if( n == 1):
  num1 = find(number[0])
  print(num1)
else:
  num1 = find(number[0])
  num2 = find(number[1])
  print( num1 + num2) 


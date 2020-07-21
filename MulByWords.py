OneTo9 = ['zero','one','two','three','four','five','six','seven','eight','nine']
elevenTo19 = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen',
'seventeen','eighteen','nineteen']
tens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty',
'ninety','one hundred']

def find(str):
  try:
    temp = OneTo9.index(str)
  except:
    try:
      temp = elevenTo19.index(str)+11
    except:
      temp=tens.index(str)+1
      temp=temp * 10
  return temp;

firstNumber=raw_input('Enter a number in string below 100: ')
secNumber=raw_input('Enter a number in string below 100: ')
firstNumber = firstNumber.split('-')
n = len(firstNumber)
if(n==1):
  firstNumber = find(firstNumber[0])
else:
  temp1 = find(firstNumber[0])
  temp2 = find(firstNumber[1])
  firstNumber = temp1 + temp2

secNumber=secNumber.split('-')
n2 = len(secNumber)
if(n2==1):
  secNumber = find(secNumber[0])
else:
  temp3 = find(secNumber[0])
  temp4 = find(secNumber[1])
  secNumber = temp3 + temp4

total = firstNumber * secNumber
print firstNumber, '*', secNumber, '=' , total 




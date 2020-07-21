def palindrome():
  rangeI = xrange(100,1000)
  rangeJ = xrange(10,100)
  pal = 0
  for i in rangeI:
    for j in rangeJ:
      product = i * j 
      if str(product) == str(product) [::-1]:
        if product > pal:
          pal = product
  return pal
print(palindrome()) 

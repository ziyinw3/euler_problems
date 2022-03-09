file = open("euler8 text.txt", "r", 1)
string = file.read()

#mytable = string.maketrans("\n", " ")
#working = string.translate(mytable)

s = string.replace("\n", "")

adjacentLength = 13
largestProduct = 0

for i in range(0, len(s) - adjacentLength + 1):

  product = 1

  for j in range(i, i + adjacentLength):
    product *= int(s[j: j + 1])

  if product > largestProduct:
    largestProduct = product

print (largestProduct)
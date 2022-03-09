sum = 0
for i in range(1, 101):
    sum = sum + i ** 2

square = 0
for i in range(1, 101):
    square = square + i

square = square ** 2

print(square - sum)
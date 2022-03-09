i = 600851475143
j = 2

while j < i:
    while i % j == 0:
        i = i / j
    j += 1    

print(i)
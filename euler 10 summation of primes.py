set = {2}
sum = 2

for i in range(3, 100000):
    prime = True
    for item in set:
        if i % item == 0:
            prime = False
    if prime == True:
        set.add(i)
        sum += i

print(sum)
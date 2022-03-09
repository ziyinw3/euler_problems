#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

factors = []
starter = 1

for candidate in range(1, 21):
    working = candidate
    for item in factors:
        if working % item == 0:
            working = working // item
    factors.append(working)
    starter = starter * working

print(factors)
print(starter)
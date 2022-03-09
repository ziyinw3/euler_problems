#What is the 10 001st prime number?
#takes approx 56 seconds...

from cmath import inf


list=[]
prime = True

for i in range(2, 200000):
    prime = True
    for item in list:
        # iterate through items. if a divisor is found, set prime boolean to false
        if i % item == 0:
            prime = False
    # once finished iterating, check prime status
    if prime == True:
        list.append(i)
    if len(list) == 10001:
        break

print(list[10000])
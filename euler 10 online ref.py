def IsPrime(x):
    returnVal = True
    for i in range(2,int(x)):
        if (int(x) % i)==0:
            returnVal=False
            break
    return returnVal
sum=2

for i in range(11, 2000):
    if IsPrime(i):
        sum = sum + i
        
print(sum)
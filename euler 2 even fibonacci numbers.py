# create list of fibonacci numbers up til 4 mil
# iterate through list to find all numbers with zero remainder
# sum up

fibonacci = [1, 1]
counter = 1;
i = 0;

while i < 4000000:
    i = fibonacci[counter] + fibonacci[counter - 1]
    fibonacci.append(i)
    counter += 1

sum = 0
for j in range(len(fibonacci)):
    if fibonacci[j] % 2 == 0 :
        sum += fibonacci[j]

print(sum)
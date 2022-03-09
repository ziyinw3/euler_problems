#pythagorean triplet: a + b + c = 1000 
#a < b < c
#a^2 + b^2 = c^2

triplets = []
list = []

for a in range(0, 1001):
    for b in range(0, 1001):
        if (a ** 2 + b ** 2) ** 0.5 % 1 == 0:
            c = (a ** 2 + b ** 2) ** 0.5
            if c == 1000 - a - b:
                set = {a, b, c}
                if set not in triplets:
                    triplets.append(set)

for i in triplets:
    if len(i) == 3:
        print(i)
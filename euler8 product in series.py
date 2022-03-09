file = open("euler8 text.txt", "r", 1)
string = file.read()

#mytable = string.maketrans("\n", " ")
#working = string.translate(mytable)

working = string.replace("\n", "")

index_start = 0
index_end = 12

list = working.split("0")
listnew = []
candidates = []
number_list = []

for item in list:
    if len(item) >= 13:
        listnew.append(item)

for item in listnew:
    if index_end < len(item):
        if int(item[index_start]) < int(item[index_end]) :
            index_start += 1
            index_end += 1
        
        candidates.append(item[index_start:index_end])

print(candidates)

for item in candidates:
    for i in range(len(item)):
        number_list.append(int(item[i]))
print(number_list)

max = 0

def multiplyList(input_list) :
     
    result = 1
    for x in input_list:
         result = result * x
    return result

for k in range(0, len(number_list), 12):
    if multiplyList(number_list[k:k+13]) > max:
        max = multiplyList(number_list[k:k+13])
        print(max)
    print(number_list[k:k+13])

print(max)
list = []
palindrome = []

for i in range(100, 999):
    for j in range(100, 999):
        value = str(i * j)
        list.append(value)

for item in list:
    check = True
    for k in range(len(item) // 2):
        if item[k] == item[len(item) - 1 - k]:
            continue
        else:
            check = False
            break
    if check == True:
        palindrome.append(int(item))
            
print(max(palindrome))
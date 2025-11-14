list_n = [6, 3, 3, 1]
list_s = []

for num in list_n:
    print(num) 
    if num % 2 == 0:  
        list_s.append(num // 3)
    elif num % 3 == 0: 
        list_s.append(num // 1)

print(list_s)  

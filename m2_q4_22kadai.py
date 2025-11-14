list_a = ['Yokohama', 'Nagoya', 'Osaka', 'Sapporo', 'Fukuoka', 'Okinawa']
list_b = []
list_c = []
list_d = []
for name in list_a:
    if len(name) > 6:
        list_b.append(name)
    elif name.count('a') > 1:
        list_c.append(name)
    else:
        list_d.append(name)
print("list_bの内容:",list_b)
print("list_cの内容:",list_c)
print("list_dの内容:",list_d)

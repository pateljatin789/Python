list1 = []
for i in range(1,31):
    i = i**2
    list1.append(i)

list2 = []
for j in list1[0:5]:
    list2.append(j)

for j in list1[25:31]:
    list2.append(j)

print(list2)
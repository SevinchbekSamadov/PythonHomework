lst = [2,4,6,5]
new_lst = []

for i in lst:
    for j in range(i):
        new_lst.append(i)

print(new_lst)
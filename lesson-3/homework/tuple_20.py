tp = (2,4,6,5)
new_lst = []

for i in tp:
    for j in range(i):
        new_lst.append(i)
new_tp = tuple(new_lst)
print(new_tp)
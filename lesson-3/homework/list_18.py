lst = [21,34,56,78,234,567]
sub_list1 = [34,58]
sub_list2 = [56, 78, 234]
result = False

for i in sub_list1:
    if i in lst:
        result = True
    else:
        result = False

print(result)



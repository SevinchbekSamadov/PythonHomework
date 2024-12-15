lst = [21,34,56,78,234,567]
sub_list1 = [34,56]
sub_list2 = [56, 78, 234]
print(str(lst))
if str(sub_list1) in str(lst):
    print(True)
else:
    print(False)

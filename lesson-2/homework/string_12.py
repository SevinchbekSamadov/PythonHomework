lst = [input() for i in range(4)]
print(lst)
striing = ''
for i in lst:
    striing += i
    if i != lst[3]:
        striing += '-'
print(striing)
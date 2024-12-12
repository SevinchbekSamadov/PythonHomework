txt = input('txt = ')

for i in txt:
    if i.isdigit():
        print('raqam bor')
        break
else:
    print('raqam yoq')
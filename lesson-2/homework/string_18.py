txt = input('txt = ')

starting = ''
ending = ''

for i in txt:
    if i != ' ':
        starting += i 
    else:
        break
txt = txt[::-1]
for i in txt:
    if i != ' ':
        ending += i 
    else:
        break

if starting == ending[::-1]:
    print('ular teng')
else:
    print('ular teng emas')


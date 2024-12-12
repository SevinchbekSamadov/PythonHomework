txt = input('gap kiriting: ')
striing = txt[0]

for i in range(len(txt)):
    if txt[i] == ' ':
        striing += txt[i + 1]

print(striing)
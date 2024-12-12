txt = input('txt = ')
sozlar = 0
for i in txt.strip():
    if i == ' ':
        sozlar += 1

print("sozlar soni",sozlar + 1)
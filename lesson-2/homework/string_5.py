txt = input('soz kiriting: ')
vowel = 0
consonant = 0

for i in txt:
    if i == 'o' or i == 'a' or i == 'e' or i == 'i' or i == 'u':
        vowel += 1
    else:
        consonant += 1

print(f"{txt} sozida {vowel} ta unli {consonant} ta undosh harflari mavjud")
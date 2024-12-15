numbers = [12,23,2,43,45,56,6,8,9]
even_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count += 1

print(even_count)
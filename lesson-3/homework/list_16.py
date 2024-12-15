numbers = [12,23,2,43,45,56,6,8,9]
odd_count = 0

for i in numbers:
    if i % 2 == 1:
        odd_count += 1

print(odd_count)
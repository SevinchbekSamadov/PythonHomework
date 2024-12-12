a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
    
if a >= b:
    if a <= c:
        print(f"kattasi: {c}, kichigi: {b}")
    else:
        if b >= c:
            print(f"kattasi: {a}, kichigi: {c}")
        else:
            print(f"kattasi: {a}, kichigi: {b}")
else:
    if b <= c:
        print(f"kattasi: {c}, kichigi: {a}")
    else:
        if c >= a:
            print(f"kattasi: {b}, kichigi: {a}")
        else:
            print(f"kattasi: {b}, kichigi: {c}")



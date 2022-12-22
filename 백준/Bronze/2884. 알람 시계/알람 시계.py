a, b = map(int, input().split())
if b < 45:
    if a == 0:
        a = 23
        b = b + 60 - 45
        print(a, b)
    elif a != 0:
        a = a - 1
        b = b + 60 - 45
        print(a, b)
elif b >= 45:
    b = b - 45
    print(a, b)
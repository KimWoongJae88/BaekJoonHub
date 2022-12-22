a = input()
b = input()
if a[0] == '-':
    if b[0] == '-':
        print(3)
    if b[0] != '-':
        print(2)
if a[0] != '-':
    if b[0] == '-':
        print(4)
    if b[0] != '-':
        print(1)
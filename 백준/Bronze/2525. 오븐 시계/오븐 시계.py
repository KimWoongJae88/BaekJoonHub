a, b = map(int, input().split()) # 17, 40
c = int(input()) # 80
a += c // 60
b += c % 60
if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -=24
print(a, b)
a, b, c = map(int, input().split())
if a == b == c:
    print(a*1000+10000)
else:
    if a == b or a == c:
        print(a*100+1000)
    if b == c:
        print(b*100+1000)
    if a != b and a != c and b != c:
        print(max(a,b,c)*100)
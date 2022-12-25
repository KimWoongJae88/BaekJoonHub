n = int(input())
c = 0
for _ in range(n):
    c += 1
    a,b = map(int, input().split())
    print(f'Case #{c}:', a + b)
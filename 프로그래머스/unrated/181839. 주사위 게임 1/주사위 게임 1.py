def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return a**2 + b**2
    if (a + b) % 2 != 0:
        return (a + b) * 2
    if a % 2 == 0 and b % 2 == 0:
        if a == b:
            return 0
        if a > b:
            return a - b
        if b > a:
            return b - a
            
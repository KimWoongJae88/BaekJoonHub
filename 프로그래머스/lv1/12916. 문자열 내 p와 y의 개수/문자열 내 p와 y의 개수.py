def solution(n):
    pp = 0
    yy = 0
    for i in n:
        if i == 'p' or i == 'P':
            pp += 1
        if i == 'y' or i == 'Y':
            yy += 1
    if pp == yy:
        return True
    else:
        return False
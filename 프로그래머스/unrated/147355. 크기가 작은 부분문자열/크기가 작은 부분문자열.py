def solution(t, p):
    answer = []
    a = []
    for i in range(len(t)-len(p)+1):
        a.append(t[0+i:len(p)+i])
    for j in a:
        if j <= p:
            answer.append(j)
    return len(answer)    
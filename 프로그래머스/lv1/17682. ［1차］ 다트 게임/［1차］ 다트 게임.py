def solution(dartResult):
    answer = []
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            if dartResult[i-2 : i].isdigit():
                answer.append(int(dartResult[i-2 : i])**1)
            else:
                answer.append(int(dartResult[i-1])**1)
        if dartResult[i] == 'D':
            if dartResult[i-2 : i].isdigit():
                answer.append(int(dartResult[i-2 : i])**2)
            else:
                answer.append(int(dartResult[i-1])**2)
        if dartResult[i] == 'T':
            if dartResult[i-2 : i].isdigit():
                answer.append(int(dartResult[i-2 : i])**3)
            else:
                answer.append(int(dartResult[i-1])**3)
        if dartResult[i] == '#':
            answer[-1] *= -1
        if dartResult[i] == '*':
            if len(answer) == 1:
                answer[-1] = answer[-1]*2
            else:
                answer[-1] = answer[-1]*2
                answer[-2] = answer[-2]*2
    return sum(answer)
def solution(k, m, score):
    answer = 0
    num = []
    score = sorted(score, reverse = True)
    for i in range(len(score)):
        num.append(score[i])
        if len(num) == m:
            answer += min(num)*m
            num = []
    return answer
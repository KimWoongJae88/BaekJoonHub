def solution(k, score):
    answer = []
    a = []
    for i in score:
        a.append(i)
        a = sorted(a, reverse = True)
        if len(a) <= k:
            answer.append(min(a))
        if len(a) > k:
            a = a[:k]
            answer.append(min(a))
    return answer
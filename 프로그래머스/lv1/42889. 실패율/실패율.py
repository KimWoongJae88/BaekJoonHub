def solution(N, stages):
    answer = []
    dic = {}
    dic_2 = {}
    stages = sorted(stages)
    for i in range(1, N+2):
        dic[i] = 0
    for j in stages:
        dic[j] += 1
    for k in range(1, len(dic)):
        a = 0
        for h in range(1, k):
            a += dic[h]
        if (len(stages)-a) != 0:
            dic_2[k] = dic[k]/(len(stages)-a)
        else:
            dic_2[k] = dic[k]
    dic_2 = sorted(dic_2.items(), key = lambda x : x[1], reverse = True)
    for p in range(len(dic_2)):
        answer.append(dic_2[p][0])
    return answer
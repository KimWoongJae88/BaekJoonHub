def solution(answers):
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == num_1[i%len(num_1)]:
            score[0] += 1
        if answers[i] == num_2[i%len(num_2)]:
            score[1] += 1
        if answers[i] == num_3[i%len(num_3)]:
            score[2] += 1
    for i, v in enumerate(score):
        if v == max(score):
            answer.append(i+1)
    return answer
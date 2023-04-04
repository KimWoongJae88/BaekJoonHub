def solution(lottos, win_nums):
    answer = []
    for i in lottos:
        if i in win_nums:
            win_nums.remove(i)
    if len(win_nums) == 6:
        if lottos.count(0) == 0 and 1:
            answer.append(6)
            answer.append(6)
        else:
            answer.append(7-(6-len(win_nums)+lottos.count(0)))
            answer.append(6)
    if len(win_nums) != 6:
        answer.append(7-(6-len(win_nums)+lottos.count(0)))
    if len(win_nums) != 6:
        answer.append(7-(6-len(win_nums)))
    return answer
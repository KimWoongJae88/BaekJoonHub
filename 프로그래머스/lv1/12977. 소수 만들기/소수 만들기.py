from itertools import combinations
def solution(nums):
    numbers = []
    answer = 0
    for i in list(combinations(nums, 3)):
        numbers.append(sum(i))
    for j in numbers:
        a = 0
        for k in range(2, int((j)**0.5)+1):
            if j % k == 0:
                a += 1
        if a == 0:
            answer += 1
    return answer
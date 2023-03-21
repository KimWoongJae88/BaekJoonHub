def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        a = numbers.pop(i)
        for j in numbers:
            answer.append(a+j)
        numbers.insert(i, a)
    return sorted(list(set(answer)))
def prime_number(n, limit, power):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i ==0:
            if n == i**2:
                count += 1
            else:
                count += 2
        if count > limit:
            return power
    return count

def solution(number, limit, power):
    answer = 1
    for i in range(2, number+1):
        pri_num = prime_number(i, limit, power)
        answer += pri_num
    return answer
def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        if i == '':
            answer += ' '
        else:
            if i[0].isdigit():
                answer += i
                answer += ' '
            else:
                answer += i[0].upper()
                answer += i[1:]
                answer += ' '
    return answer[0:-1]
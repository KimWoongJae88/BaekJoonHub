n = int(input())  # 반복될 문자열의 갯수
for _ in range(n):  # 갯수만큼 반복시켜주고
    a, b = map(str, input().split())  # a는 b가 반복될 숫자, b는 반복될 문자를 입력받아
    c = ''  # 빈문자열을 생성해주고
    for i in b:
        c += i*int(a)  # b에서 반복되는 문자열 하나마다 a만큼 곱해서 빈문자열 c에 더해준다.
    print(c)
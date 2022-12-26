# 리스트의 길이 값a와 리스트 내의 값중 작은 수를 찾을 기준b를 입력받고
a, b = map(int, input().split())
# 리스트를 입력받는다.
list_a = list(map(int, input().split()))
a = '' # 빈문자열a를 생성
for i in list_a:
    if b > i:  # 리스트를 반복하고 기준b 보다 작은 i값을 빈문자열a에 더해준다.
        a += str(i)
        a += ' ' # 출력형식에 맞게 공백도 더해준다.
print(a)
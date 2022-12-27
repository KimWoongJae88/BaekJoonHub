n = int(input())  # 총 과목수를 입력 받는다.
sum_a = 0  # 0의 값을 가진 객체를 생성
list_a = list(map(int, input().split()))  # n의 갯수만큼 숫자(과목점수)를 입력받고
for i in list_a:
    sum_a += i/max(list_a)*100  # 문제 조건에 맞게 계산해준 값을 sum_a에 더해준 후,
print(sum_a/n)  # 조건에 맞게 계산된 총 합에 총 과목수를 나눠준 후 출력해준다.
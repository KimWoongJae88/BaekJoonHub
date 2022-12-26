N = int(input())
list_a = list(map(int, input().split())) # N갯수만큼의 리스트?형식으로 숫자를 받는다.
num = int(input())  # 찾는 숫자를 입력받고
count = list_a.count(num)  # count()를 이용하여 갯수를 센다.
print(count)
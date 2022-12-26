# 주어지는 정수 갯수를 a로 입력받는다.
a = map(int, input().split())
# a만큼 정수를 입력받고
list_a = list(map(int, input().split()))
# 주어진 정수중에 작은수, 큰수를 찾아서 출력
print(min(list_a), max(list_a))
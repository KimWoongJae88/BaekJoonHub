a, b = map(str, input().split())  # 뒤집기 위해 str로 숫자를 입력받는다
print(max(int(a[::-1]), int(b[::-1])))  # 뒤집고 다시 int로 바꿔준후 큰숫자를 출력
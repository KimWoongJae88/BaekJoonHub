n = input()

# 입력받은 수의 자리가 한자리이면 앞에 '0'을 더해서 계산하기 편하게 만들어준다.
if len(n) == 1:
    n = '0'+n

a = int(n[-1]) * 10 + int(str(int(n[0]) + int(n[-1]))[-1]) # 입력받은 숫자를 다음 루프 숫자로 바꾸고 a로 객체화
count = 1 # 객체화 시킨 다음부터 비교 할 것이기 때문에 카운트는 1

while True:
    if a != int(n): # 다음 루프 숫자가 입력받은 n과 다르면
        # 다음 루프 숫자가 한자리이면 앞에 '0'을 더해준다.
        if len(str(a)) == 1:
            a = '0'+str(a)
        # 두자리인 a 다음 루프 숫자로 바꿔주고 다시 a로 객체화
        a = int(str(a)[-1]) * 10 + int(str(int(str(a)[0]) + int(str(a)[-1]))[-1])
        count += 1 # 카운트에 += 1
    if a == int(n):
        print(count)
        break
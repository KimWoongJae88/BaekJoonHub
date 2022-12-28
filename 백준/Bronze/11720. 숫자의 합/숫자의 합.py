a = input()  # 숫자의 갯수를 입력받고
n = input()  # 갯수만큼 자리숫의 수가 입력된다.
sum_n = 0  # 각자리 수의 총합을 구하기위해 0을
for i in n:
    sum_n += int(i)  # 문자열로 들어온 n을 int로 변환하여 반복해서 더해준다.
print(sum_n)
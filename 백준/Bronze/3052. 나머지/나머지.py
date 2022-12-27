a = [] # 입력받은 수를 리스트화
b = [] # 정답을 구하기 위해 빈리스트 생성
for _ in range(10): # 10개의 수를 입력 받는다.
    a.append(int(input()))
for i in a: # 10개의 수를 입력받은 a리스트를 i로 반복
    if i%42 not in b: # i%42가 정답용 빈리스트b에 없으면 추가해준다.
        b.append(i%42)
    else:
        pass # 있으면 패스
print(len(b)) # 각각의 갯수를 구해준다.
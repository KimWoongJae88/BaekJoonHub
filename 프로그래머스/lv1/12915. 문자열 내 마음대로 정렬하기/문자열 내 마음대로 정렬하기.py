def solution(strings, n):
    answer = []
    st = []
    pm = []
    for i in strings:
        if i[n] not in st:
            st.append(i[n])
    st.sort()
    for j in st:
        for k in strings:
            if j == k[n]:
                pm.append(k)
        pm.sort()
        answer += pm
        pm = []
    return answer
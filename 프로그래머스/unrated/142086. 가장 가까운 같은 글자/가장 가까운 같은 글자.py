def solution(s):
    answer = []
    st = ''
    for i in s:
        if i in st:
            index_num = st.rindex(i)
            st += i
            answer.append(st.rindex(i)-index_num)
        else:
            st += i
            answer.append(-1)
    return answer
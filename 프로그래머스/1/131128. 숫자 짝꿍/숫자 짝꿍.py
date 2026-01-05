def solution(X, Y):
    answer = ''
    list1 = [0] * 10
    list2 = [0] * 10
    for i in X:
        list1[int(i)] +=1
    for j in Y:
        list2[int(j)] +=1
    for i in range(9, -1, -1):
        if list1[i] and list2[i]:
            answer += str(i) * min(list1[i], list2[i])
    if len(answer) == 0:
        return "-1"
    elif answer[0] == "0":
        return "0"
    return answer
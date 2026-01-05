def solution(clothes):
    answer = 1
    dict1 = dict()
    for i,v in clothes:
        if v not in dict1:
            dict1[v] =1
        else:
            dict1[v] +=1
    for v in dict1.values():
        answer *= (v+1)
    answer-=1
    return answer
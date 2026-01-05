def solution(participant, completion):
    answer = ''
    dict1 = dict()
    for p in participant:
        if p not in dict1:
            dict1[p] = 1
        else:
            dict1[p] +=1
    for c in completion:
        if c in dict1:
            dict1[c]-=1
    for i,v in dict1.items():
        if v:
            answer = i
    return answer
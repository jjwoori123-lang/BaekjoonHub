def solution(genres, plays):
    answer = []
    tot = {}
    cnt =  {}
    for i in range(len(genres)):
        if genres[i] not in cnt:cnt[genres[i]] = [(plays[i], i )]
        else:cnt[genres[i]].append((plays[i], i))
    
    for i in range(len(genres)):
        if genres[i] not in tot:tot[genres[i]] = plays[i]
        else:tot[genres[i]] += plays[i]
    tot = dict(sorted(tot.items(), key = lambda x: x[1], reverse = True))
    for c in cnt: cnt[c].sort(key = lambda x : (-x[0], x[1]))

    for t in tot:
        tmp = 2
        for i,v in enumerate(cnt[t]):
            if tmp == 0:
                break
            answer.append(v[1])
            tmp-=1
    return answer
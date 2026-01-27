import heapq

def solution(operations):
    deletion = [0] * len(operations)
    max_heap = []
    min_heap = []
    for i, op in enumerate(operations):
        cm, d = op.split()
        num = int(d)
        if cm == 'I':
            heapq.heappush(max_heap, (-num, -i))
            heapq.heappush(min_heap, (num, i))
        else:
            if num == 1:
                while max_heap:
                    del_num, del_ind = heapq.heappop(max_heap)
                    if not deletion[-del_ind]:
                        deletion[-del_ind] = 1
                        break
            else:
                while min_heap:
                    del_num, del_ind = heapq.heappop(min_heap)
                    if not deletion[del_ind]:
                        deletion[del_ind] = 1
                        break
                        
    max_v = None
    while max_heap:
        val,ind = heapq.heappop(max_heap)
        if not deletion[-ind]:
            max_v = -val
            break
    min_v = None
    while min_heap:
        val,ind = heapq.heappop(min_heap)
        if not deletion[ind]:
            min_v = val
            break
    if max_v is None or min_v is None: 
        return [0,0]
    else: 
        return [max_v, min_v]
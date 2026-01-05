from collections import Counter

def solution(nums):
    answer = 0
    pick = int(len(nums)//2)
    mon = list(Counter(nums))
    if len(mon) >= pick:
        return pick
    else:
        return len(mon)
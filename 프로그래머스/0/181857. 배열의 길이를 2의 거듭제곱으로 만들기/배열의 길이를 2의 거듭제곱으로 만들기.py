def solution(arr):
    answer = []
    while bin(len(arr)).count('1') != 1:
        arr.append(0)
    answer = arr
    return answer
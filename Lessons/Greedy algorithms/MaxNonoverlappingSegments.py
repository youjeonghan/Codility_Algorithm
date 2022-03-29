def solution(A, B):
    arr = sorted(zip(A, B), key=lambda x: x[1])
    cnt = 0
    now = -1
    for s, e in arr:
        if now < s:
            cnt += 1
            now = e
    return cnt


print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))

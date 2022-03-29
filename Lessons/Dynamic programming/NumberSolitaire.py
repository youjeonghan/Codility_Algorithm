def solution(A):
    arr = [0] * len(A)
    arr[0] = A[0]
    arr[1] = A[0] + A[1]
    for i in range(2, len(A)):
        if i <= 6:
            arr[i] = A[i] + max(*arr[1:i], A[0])
            continue
        arr[i] = A[i] + max(arr[i - 6 : i])

    return arr[-1]


print(solution([1, -2, 0, 9, -1, -2, 2]))

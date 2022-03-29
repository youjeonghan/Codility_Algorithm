def solution(A):
    A.sort()
    if len(A) == 1:
        return A[0]
    for i in range(0, len(A), 2):
        if i == len(A) - 1:
            return A[i]
        if A[i] != A[i + 1]:
            return A[i]


print(solution([1, 3, 1]))

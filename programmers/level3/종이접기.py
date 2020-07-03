def solution(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 0, 1]

    arr = [0, 0, 1]

    for i in range(n-2):
        rev = [0 if i == 1 else 1 for i in arr[::-1]]
        arr = arr + [0] + rev
    return arr

print(solution(4))
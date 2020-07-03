import sys
sys.setrecursionlimit(10**9)

def recursion(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if cache[n] != 0:
        return cache[n]

    cache[n] = (recursion(n-1) + recursion(n-2)) % 1234567

    return cache[n]

def solution(n):
    global cache
    cache = [0] * (n+1)
    answer = recursion(n)
    return answer


print(solution(3))
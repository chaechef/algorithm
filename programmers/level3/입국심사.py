def solution(n, times):
    answer = 0
    mintime = min(times)
    lo = 0
    hi = mintime * n + 1

    while lo < hi:
        mid = (lo + hi) // 2
        temp = sum([mid // a for a in times])
        if temp < n:
            lo = mid + 1
        else:
            hi = mid

    return lo



solution(6, [7,10])
def bisearch(lo, hi, budgets, M):
    while lo < hi:
        mid = int((lo + hi) / 2)
        tsum = 0
        for val in budgets:
            if mid >= val:
                tsum += val
            else:
                tsum += mid
        print(lo,mid,hi, tsum, M)
        if tsum >= M:
            hi = mid
        else:
            lo = mid + 1

    return lo

def solution(budgets, M):
    budgets.sort()
    answer = bisearch(0, M, budgets, M)
    tsum = 0
    for val in budgets:
        if answer > val:
            tsum += val
        else:
            tsum += answer

    if answer == M:
        return max(budgets)
    return answer if tsum <= M else answer -1

print(solution([50, 50, 200], 400))
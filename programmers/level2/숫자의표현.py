def solution(n):
    arr = [i for i in range(1, n+1)]
    start = 0
    end = 1
    answer = 0
    while start < end:
        tsum = sum(arr[start:end])
        if tsum < n:
            end += 1
        elif tsum > n:
            start += 1
        else:
            start += 1
            answer += 1

    return answer


print(solution(15))
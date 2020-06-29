from collections import deque

def solution(people, limit):
    arr = deque(sorted(people, reverse=True))
    answer = 0
    while arr:
        curr = arr.popleft()
        while arr:
            if curr + arr[0] <= limit:
                curr += arr.popleft()
            else:
                break

        while arr:
            if curr + arr[-1] <= limit:
                curr += arr.pop()
            else:
                break

        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
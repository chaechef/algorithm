import heapq
from collections import deque


def solution(stock, dates, supplies, k):
    answer = 0
    curr = stock
    idx = 0
    hq = []
    while curr <= k:
        for i in range(idx, len(dates)):
            if dates[i] <= curr:
                heapq.heappush(hq, -supplies[i])
            else:
                idx = i
                break
        else:
            idx = len(dates)
        curr += -heapq.heappop(hq)
        answer += 1

    return answer

print(solution(4,[1,2,3,4],[10,40,20,30],100))
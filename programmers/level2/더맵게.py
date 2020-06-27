import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            if scoville[0] >= K:
                break
            else:
                return -1

        if scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            answer += 1
        else:
            break

    print(answer)
    return answer

solution([1, 2, 3, 9, 10, 12], 7)
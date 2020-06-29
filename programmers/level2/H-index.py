def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(max(citations), -1, -1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
            else:
                break
        if count >= i and len(citations) - count <= i:
            return i


print(solution([10,9,4,1,1]))
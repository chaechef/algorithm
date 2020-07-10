def solution(weights):
    answer = 0
    weights.sort()
    prev = 0
    for i in range(1, len(weights)):
        prev = prev + weights[i-1]
        if prev + 1 < weights[i]:
            answer = prev
            break
    else:
        answer = sum(weights)
    return answer + 1

print(solution([1, 2, 3]))
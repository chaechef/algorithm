def solution(d, budget):
    answer = 0
    d = sorted(d)
    for v in d:
        if v > budget:
            break
        answer += 1
        budget -= v
    return answer


if __name__ == '__main__':
    solution([1,3,2,5,4], 9)
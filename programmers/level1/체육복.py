def solution(n, lost, reserve):
    remains = [1] * (n)
    for val in reserve:
        remains[val-1] += 1
    for val in lost:
        remains[val-1] -= 1

    for idx, val in enumerate(remains):
        if val == 0 and idx - 1 >= 0 and remains[idx-1] == 2:
            remains[idx] += 1
            remains[idx-1] -= 1
            continue
        if val == 0 and idx + 1 < n and remains[idx+1] == 2:
            remains[idx] += 1
            remains[idx+1] -= 1

    return remains.count(1) + remains.count(2)


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))

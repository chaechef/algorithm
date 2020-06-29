def solution(arr1, arr2):
    answer = []
    arr2 = [list(a) for a in zip(*arr2)]
    for i in arr1:
        tempa = []
        for j in arr2:
            temp = sum([a * b for a, b in zip(i, j)])
            tempa.append(temp)
        answer.append(tempa)
    return answer


solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    aidx = 0
    bidx = 0
    while bidx != len(B):
        if A[aidx] < B[bidx]:
            answer += 1
            bidx += 1
            aidx += 1
        else:
            bidx += 1

    return answer
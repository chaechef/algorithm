
def pick(arr):
    ret = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            ret = arr[i]
            arr[i] = 0
            break
    return ret

def solution(board, moves):
    answer = 0
    stack = []
    trans = [list(a) for a in zip(*board)]
    for val in moves:
        picked = pick(trans[val-1])
        if picked != 0:
            if len(stack) > 0 and stack[-1] == picked:
                answer += 2
                stack.pop()
            else:
                stack.append(picked)

    return answer


if __name__ == "__main__":
    a = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])

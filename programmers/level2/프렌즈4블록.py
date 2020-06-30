def isboom(y,x,board):
    checkidx = [(0, 1), (1, 0), (1, 1)]
    tile = board[y][x]
    if len(board[y+1])-1 <= x:
        return False
    for i in range(3):
        if tile != board[y+checkidx[i][0]][x+checkidx[i][1]]:
            return False

    return True


def solution(m, n, board):
    board = [list(row)[::-1] for row in zip(*board)]
    answer = 0
    while True:
        stk = set([])

        for i in range(len(board)-1):
            for j in range(len(board[i])-1):
                if isboom(i, j, board):
                    stk.add((i, j))
                    stk.add((i + 1, j))
                    stk.add((i, j + 1))
                    stk.add((i + 1, j + 1))

        if len(stk) == 0:
            break
        stk = sorted(list(stk), key=lambda x: -x[1])
        answer += len(stk)
        for val in stk:
            i, j = val
            board[i].pop(j)

    return answer

print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
# print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
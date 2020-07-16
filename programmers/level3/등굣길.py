from collections import deque

def bfs(n, m, board):
    visit = [[False for j in range(m)] for i in range(n)]
    count = [[100000000 for j in range(m)] for i in range(n)]

    dq = deque([[0,0]])
    count[0][0] = 1
    xy = [[0,1],[1,0],[0,-1],[-1,0]]
    step = 0
    while dq:
        size = len(dq)
        for i in range(size):
            cy, cx = dq.popleft()
            if visit[cy][cx]:
                continue
            visit[cy][cx] = True
            for d in xy:
                ny, nx = cy + d[0], cx + d[1]
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                if board[ny][nx] == -1:
                    continue

                if not visit[ny][nx]:
                    dq.append([ny,nx])
                    if count[ny][nx] != 100000000:
                        count[ny][nx] = (count[ny][nx] + count[cy][cx]) % 1000000007
                    else:
                        count[ny][nx] = count[cy][cx]

        step += 1

    if count[n-1][m-1] ==100000000:
        return 0

    return count[n-1][m-1]


def solution(m, n, puddles):
    answer = 0
    board = [[0 for j in range(m)] for i in range(n)]

    for puddle in puddles:
        x, y = puddle
        board[y-1][x-1] = -1

    answer = bfs(n, m, board)
    return answer


print(solution(4, 3, [[2,2]]))
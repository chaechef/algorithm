r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
md = 0
mu = 0

for i in range(r):
    if board[i][0] == -1:
        mu = i
        md = i + 1
        break

while t > 0:
    # 미세먼지 확산
    queue = []
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                queue.append((i, j, board[i][j]))

    for ele in queue:
        total = ele[2]
        spreadAmout = int(total / 5)
        spreadArea = 0
        if spreadAmout == 0:
            continue

        for i in range(4):
            ny, nx = ele[0] + dy[i], ele[1] + dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if board[ny][nx] == -1:
                continue
            board[ny][nx] += spreadAmout
            spreadArea += 1
        board[ele[0]][ele[1]] -= spreadArea * spreadAmout

    for i in reversed(range(0, mu)):
        if board[i+1][0] == -1:
            continue
        board[i+1][0] = board[i][0]

    for i in range(c-1):
        board[0][i] = board[0][i+1]

    for i in range(mu):
        board[i][c-1] = board[i+1][c-1]

    for i in reversed(range(1, c)):
        if board[mu][i-1] == -1:
            board[mu][i] = 0
            continue
        board[mu][i] = board[mu][i-1]

    for i in range(md, r-1):
        if board[i][0] == -1:
            continue
        board[i][0] = board[i+1][0]
    for i in range(c-1):
        board[r-1][i] = board[r-1][i+1]

    for i in reversed(range(md+1, r)):
        board[i][c-1] = board[i-1][c-1]

    for i in reversed(range(1,c)):
        if board[md][i-1] == -1:
            board[md][i] = 0
            continue
        board[md][i] = board[md][i-1]

    t -= 1


ret = 0

for i in range(r):
    for j in range(c):
        if board[i][j] == -1 or board[i][j] == 0:
            continue
        ret += board[i][j]

print(ret)
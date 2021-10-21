# 21608
n = int(input())
size = n**2
board = [[0] * n for _ in range(n)]
sarr = []
fdict = {}
dy = [0,0,1,-1]
dx = [1,-1,0,0]
for i in range(size):
    line = list(map(int, input().split()))
    id = line[0]
    favorite = line[1:]
    sarr.append(id)
    fdict[id] = favorite


for id in range(size):
    currId = sarr[id]
    currFavor = fdict[currId]
    candidates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                continue
            emptyCount = 0
            favorCount = 0
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                if board[ny][nx] in currFavor:
                    favorCount += 1
                    continue
                if board[ny][nx] == 0:
                    emptyCount += 1
                    continue

            candidates.append((favorCount, emptyCount, i, j))

    bestPosition = sorted(candidates, key=lambda x: (-x[0], -x[1], i, j))[0]
    by, bx = bestPosition[2], bestPosition[3]
    board[by][bx] = currId


ret = 0
for i in range(n):
    for j in range(n):
        fcount = 0
        for d in range(4):
            ny, nx = i + dy[d], j + dx[d]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] in fdict[board[i][j]]:
                fcount += 1
        if fcount == 0:
            ret += 0
        elif fcount == 1:
            ret += 1
        elif fcount == 2:
            ret += 10
        elif fcount == 3:
            ret += 100
        else:
            ret += 1000

print(ret)
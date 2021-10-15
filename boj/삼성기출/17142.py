# 연구소 3
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
candidates = []
dy = [0,0,1,-1]
dx = [1,-1,0,0]
retMin = 10000000
walls = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            candidates.append((i, j))
            board[i][j] = "*"
        if board[i][j] == 1:
            board[i][j] = "-"
            walls.append((i, j))

for candi in combinations(candidates, m):
    cboard = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    for wall in walls:
        cboard[wall[0]][wall[1]] = "-"
    for cc in candidates:
        cboard[cc[0]][cc[1]] = "*"

    queue = deque()
    e = {}
    for c in candi:
        cboard[c[0]][c[1]] = 1
        visited[c[0]][c[1]] = 1
        queue.append((c[0], c[1]))

    while queue:
        cy, cx = queue.popleft()
        currCount = cboard[cy][cx] if cboard[cy][cx] != "*" else e[(cy, cx)]
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if cboard[ny][nx] == "-" or visited[ny][nx] == 1:
                continue
            if cboard[ny][nx] == "*":
                e[(ny, nx)] = currCount + 1
                visited[ny][nx] = 1
                queue.append((ny, nx))
                continue
            if cboard[ny][nx] != 0 and cboard[ny][nx] < currCount + 1:
                continue
            cboard[ny][nx] = currCount + 1
            queue.append((ny, nx))
            visited[ny][nx] = 1

    maxval = 0
    isContainZero = False
    for i in range(n):
        for j in range(n):
            if cboard[i][j] == "-" or cboard[i][j] == "*":
                continue
            if cboard[i][j] == 0:
                isContainZero = True
            maxval = max(maxval, cboard[i][j])

    if not isContainZero:
        retMin = min(retMin, maxval)

if retMin == 10000000:
    print(-1)
else:
    print(retMin - 1)
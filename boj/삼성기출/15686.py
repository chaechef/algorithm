from collections import deque
from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chickens = []
house = []
queue = deque()
dy = [1,-1,0,0]
dx = [0,0,-1,1]
mmin = 1000000000
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i,j))
            board[i][j] = 0
        if board[i][j] == 2:
            chickens.append((i,j))
            board[i][j] = 0


for chickenHouses in list(combinations(chickens, m)):
    cboard = [[0] * n for _ in range(n) ]
    for y,x in chickenHouses:
        cboard[y][x] = 1
        queue.append((y,x))

    while queue:
        cy, cx = queue.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if cboard[ny][nx] == 0:
                cboard[ny][nx] = cboard[cy][cx] + 1
                queue.append((ny,nx))
            elif cboard[ny][nx] > cboard[cy][cx] + 1:
                cboard[ny][nx] = cboard[cy][cx] + 1
                queue.append((ny,nx))
    mmin = min(mmin, sum(list(map(lambda x : cboard[x[0]][x[1]] - 1, house))))

print(mmin)
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
babySharkSize = 2
needsEat = 2
dy = [0,0,1,-1]
dx = [1,-1,0,0]
sharkY = -1
sharkX = -1
loop = 0

def canEatFishes(sy, sx):
    countBoard = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > babySharkSize:
                countBoard[i][j] = -1
    countBoard[sy][sx] = 1
    queue = deque()
    queue.append((sy,sx))

    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if countBoard[ny][nx] == -1:
                continue
            if countBoard[ny][nx] != 0:
                continue
            countBoard[ny][nx] = countBoard[cy][cx] + 1
            queue.append((ny,nx))

    minCount = 100000
    miny, minx = -1, -1

    for i in range(n):
        for j in range(n):
            if countBoard[i][j] != 0 and countBoard[i][j] != -1 and board[i][j] != 0 and board[i][j] < babySharkSize:
                if minCount > countBoard[i][j]:
                    minCount = countBoard[i][j]
                    miny, minx = i, j

    return miny, minx, minCount - 1


for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            sharkY, sharkX = i, j

while True:
    nsy, nsx, count = canEatFishes(sharkY, sharkX)
    if nsy == -1 or nsx == -1:
        break

    sharkY, sharkX = nsy, nsx
    board[nsy][nsx] = 0
    needsEat -= 1
    if needsEat == 0:
        babySharkSize += 1
        needsEat = babySharkSize

    loop += count


print(loop)
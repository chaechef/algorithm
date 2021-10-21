# 21609
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
score = 0

# def rotate
def rotate():
    global board
    newBoard = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newBoard[n - j - 1][i] = board[i][j]

    board = newBoard


# def fallDown
def fallDown():
    for i in range(n):
        target = list(map(lambda x: x[i], board))
        for j in reversed(range(n)):
            if target[j] == -1 or target[j] == " ":
                continue
            idx = -1
            for k in range(j+1, n):
                if target[k] == " ":
                    idx = k
                else:
                    break
            if idx != -1:
                target[idx] = target[j]
                target[j] = " "

        for j in range(n):
            board[j][i] = target[j]

# bfs find widthest block
def findWidthestBlock():
    blockList = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                continue
            if board[i][j] == -1:
                visited[i][j] = 1
                continue
            if board[i][j] == 0:
                continue
            if board[i][j] == " ":
                continue

            visited[i][j] = 1
            blockSize = 1
            blockColor = board[i][j]
            rainbowBlock = []
            queue = deque()
            queue.append((i, j))
            while queue:
                cy, cx = queue.popleft()
                for d in range(4):
                    ny, nx = cy + dy[d], cx + dx[d]
                    if ny < 0 or nx < 0 or ny >= n or nx >= n:
                        continue
                    if visited[ny][nx] == 1:
                        continue
                    if board[ny][nx] == -1:
                        continue
                    if board[ny][nx] == 0:
                        if (ny, nx) in rainbowBlock:
                            continue
                        else:
                            rainbowBlock.append((ny, nx))
                            blockSize += 1
                            queue.append((ny, nx))
                    if board[ny][nx] == blockColor:
                        visited[ny][nx] = 1
                        blockSize += 1
                        queue.append((ny, nx))

            if blockSize > 1:
                blockList.append((i, j, blockSize, len(rainbowBlock)))

    if len(blockList) == 0:
        return 0

    return sorted(blockList, key=lambda x: (-x[2], -x[3], -x[0], -x[1]))[0]


while True:
    ret = findWidthestBlock()
    if ret == 0:
        break
    score += ret[2]**2
    queue = deque()
    queue.append((ret[0], ret[1]))
    currColor = board[ret[0]][ret[1]]
    board[ret[0]][ret[1]] = " "
    while queue:
        cy, cx = queue.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] == " ":
                continue
            if board[ny][nx] == 0 or board[ny][nx] == currColor:
                queue.append((ny, nx))
                board[ny][nx] = " "

    fallDown()
    rotate()
    fallDown()


print(score)
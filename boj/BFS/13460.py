
from collections import deque
from enum import Enum
import copy

n, m = map(int, input().split(" "))
board = [list(input()) for _ in range(n)]
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
ry, rx, by, bx = 0, 0, 0, 0
queue = deque()
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def init():
    global ry, rx, by, bx
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                ry, rx = i, j
                board[i][j] = "."
            if board[i][j] == "B":
                by, bx = i, j
                board[i][j] = "."

    visited[ry][rx][by][bx] = 1
    queue.append((ry, rx, by, bx, 0))


init()

def move(y, x, dy, dx):
    count = 0
    while board[y+dy][x+dx] != "#" and board[y][x] != "O":
        y += dy
        x += dx
        count += 1
    return y,x, count

def bfs():
    while queue:
        ry, rx, by, bx, count = queue.popleft()
        if count >= 10:
            return -1
        for i in range(4):
            nry, nrx, rcount = move(ry, rx, dy[i], dx[i])
            nby, nbx, bcount = move(by, bx, dy[i], dx[i])

            if board[nby][nbx] == "O":
                continue

            if board[nry][nrx] == "O":
                return count + 1

            if nry == nby and nrx == nbx:
                if rcount > bcount:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]

            if visited[nry][nrx][nby][nbx] == 1:
                continue

            visited[nry][nrx][nby][nbx] = 1
            queue.append((nry, nrx, nby, nbx, count + 1))
    return -1



print(bfs())
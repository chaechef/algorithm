from itertools import combinations
import copy
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
n, m = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(n)]

candidate = []
queue = deque()

ret = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            candidate.append((i,j))
        if board[i][j] == 2:
            queue.append((i,j))

for can in list(combinations(candidate, 3)):
    nboard = copy.deepcopy(board)
    nqueue = copy.deepcopy(queue)
    for ele in can:
        nboard[ele[0]][ele[1]] = 1

    while nqueue:
        y, x = nqueue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if nboard[ny][nx] == 0:
                nboard[ny][nx] = 2
                nqueue.append((ny,nx))

    count = 0
    for i in range(n):
        for j in range(m):
            if nboard[i][j] == 0:
                count += 1

    ret = max(ret, count)


print(ret)
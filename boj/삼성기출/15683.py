# 1: 4, 2: 2, 3: 4, 4: 4, 5: 1
from collections import deque
import copy
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
mmin = 1000000000
for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            queue.append((i, j, board[i][j]))



def fillboard(board, y, x, direct):
    # direct 1,2,3,4 up right down left
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    cy, cx = y, x
    while 0 <= cy < n and 0 <= cx < m:
        if board[cy][cx] == 6:
            break
        if board[cy][cx] == 0:
            board[cy][cx] = 7
        cy, cx = cy + dy[direct], cx + dx[direct]



def recursion(queue: deque, rboard):
    global mmin
    if not queue:
        sum = 0
        for b in rboard:
            for e in b:
                if e == 0:
                    sum += 1

        mmin = min(mmin, sum)
        return
    cqueue = copy.deepcopy(queue)
    curr = cqueue.popleft()

    if curr[2] == 1:
        for i in range(4):
            cboard = copy.deepcopy(rboard)
            fillboard(cboard, curr[0], curr[1], i)
            recursion(cqueue, cboard)

    elif curr[2] == 2:
        for i in range(2):
            cboard = copy.deepcopy(rboard)
            fillboard(cboard, curr[0], curr[1], i)
            fillboard(cboard, curr[0], curr[1], i+2)
            recursion(cqueue, cboard)

    elif curr[2] == 3:
        for i in range(4):
            cboard = copy.deepcopy(rboard)
            fillboard(cboard, curr[0], curr[1], i)
            fillboard(cboard, curr[0], curr[1], (i+1) % 4 )
            recursion(cqueue, cboard)
        #4
    elif curr[2] == 4:
        for i in range(4):
            cboard = copy.deepcopy(rboard)
            fillboard(cboard, curr[0], curr[1], i)
            fillboard(cboard, curr[0], curr[1], (i+1) % 4 )
            fillboard(cboard, curr[0], curr[1], (i+2) % 4 )
            recursion(cqueue, cboard)
        #4
    else:
        cboard = copy.deepcopy(rboard)
        for i in range(4):
            fillboard(cboard, curr[0], curr[1], i)
        recursion(cqueue, cboard)


recursion(queue, board)
print(mmin)
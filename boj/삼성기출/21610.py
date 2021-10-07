n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
opers = [list(map(int, input().split())) for _ in range(m)]
clouds = [[0] * n for _ in range(n)]
diay = [-1,-1,1,1]
diax = [1,-1,1,-1]

clouds[n-1][0] = 1
clouds[n-1][1] = 1
clouds[n-2][0] = 1
clouds[n-2][1] = 1

def move_cloud(cy, cx, direct, count):
    dy = 0
    dx = 0
    if direct == 1:
        dy = 0
        dx = -1
    elif direct == 2:
        dy = -1
        dx = -1
    elif direct == 3:
        dy = -1
        dx = 0
    elif direct == 4:
        dy = -1
        dx = 1
    elif direct == 5:
        dy = 0
        dx = 1
    elif direct == 6:
        dy = 1
        dx = 1
    elif direct == 7:
        dy = 1
        dx = 0
    else:
        dy = 1
        dx = -1
    ny = (cy + dy * count) % n
    nx = (cx + dx * count) % n
    return ny, nx



for oper in opers:

    next_clouds = []
    for i in range(n):
        for j in range(n):
            if clouds[i][j] == 1:
                ny, nx = move_cloud(i, j, oper[0], oper[1])
                clouds[i][j] = 0
                next_clouds.append((ny,nx))
    for nc in next_clouds:
        clouds[nc[0]][nc[1]] = 1

    for i in range(n):
        for j in range(n):
            if clouds[i][j] == 1:
                board[i][j] += 1

    for i in range(n):
        for j in range(n):
            if clouds[i][j] == 1:
                count = 0
                for direct in range(4):
                    dny, dnx = i + diay[direct], j + diax[direct]
                    if dny < 0 or dnx < 0 or dny >= n or dnx >= n:
                        continue
                    if board[dny][dnx] > 0:
                        count += 1
                board[i][j] += count

    for i in range(n):
        for j in range(n):
            if clouds[i][j] == 0 and board[i][j] >= 2:
                clouds[i][j] = 2
                board[i][j] -= 2

    for i in range(n):
        for j in range(n):
            if clouds[i][j] == 1:
                clouds[i][j] = 0

    for i in range(n):
        for j in range(n):
            if clouds[i][j] == 2:
                clouds[i][j] = 1

print(sum([sum(b) for b in board]))

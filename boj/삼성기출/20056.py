n, m, k = map(int, input().split())
balls = [list(map(int, input().split())) for _ in range(m)]
board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(len(balls)):
    balls[i][0] -= 1
    balls[i][1] -= 1

def move(r, c, s, d):
    dy = 0
    dx = 0
    if d == 0:
        dy += -1
    elif d == 1:
        dy += -1
        dx += 1
    elif d == 2:
        dx += 1
    elif d == 3:
        dy += 1
        dx += 1
    elif d == 4:
        dy += 1
    elif d == 5:
        dy += 1
        dx += -1
    elif d == 6:
        dx += -1
    else:
        dy += -1
        dx += -1
    nr, nc = (r + dy * s) % n, (c + dx * s) % n
    return nr, nc

for _ in range(k):

    newballs = []
    board = [[[] for _ in range(n)] for _ in range(n)]

    for ball in balls:
        nr, nc = move(ball[0], ball[1], ball[3], ball[4])
        board[nr][nc].append((ball[2], ball[3], ball[4]))

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) == 1:
                newballs.append((i,j, board[i][j][0][0],board[i][j][0][1],board[i][j][0][2]))
            elif len(board[i][j]) > 1:
                measureSum = 0
                measureSpeed = 0
                changed = False
                flag = True if board[i][j][0][2] % 2 == 0 else False # 짝수면 0 홀수면 1
                for ba in board[i][j]:
                    measureSum += ba[0]
                    measureSpeed += ba[1]
                    if not changed:
                        ft = True if ba[2] % 2 == 0 else False
                        if flag != ft:
                            changed = True
                measureSum = int(measureSum / 5)
                measureSpeed = int(measureSpeed / len(board[i][j]))
                if measureSum == 0:
                    continue
                if changed:
                    newballs.append((i,j,measureSum, measureSpeed, 1))
                    newballs.append((i,j,measureSum, measureSpeed, 3))
                    newballs.append((i,j,measureSum, measureSpeed, 5))
                    newballs.append((i,j,measureSum, measureSpeed, 7))
                else:
                    newballs.append((i,j,measureSum, measureSpeed, 0))
                    newballs.append((i,j,measureSum, measureSpeed, 2))
                    newballs.append((i,j,measureSum, measureSpeed, 4))
                    newballs.append((i,j,measureSum, measureSpeed, 6))

    balls = newballs

ret = 0
for baa in balls:
    ret += baa[2]

print(ret)
n, m = map(int, input().split())
y, x, d = map(int, input().split())
board = [list(map(int, input().split(" "))) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

time = 2
while True:
    # 청소하기
    if board[y][x] == 0:
        board[y][x] = time
        time += 1
    isToClean = False

    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        ny, nx = y + dy[d], x + dx[d]
        if board[ny][nx] == 0:
            y, x = ny, nx
            isToClean = True
            break

    if not isToClean:
        ny, nx = y - dy[d], x - dx[d]
        if board[ny][nx] == 1:
            break
        else:
            y, x = ny, nx

print(time - 2)
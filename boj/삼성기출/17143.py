r, c, m = map(int, input().split())
board = [[0] * c for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
position = 0
ret = 0
for _ in range(m):
    rs, cs, s, d, z = map(int, input().split())
    rs, cs, d = rs - 1, cs - 1, d - 1
    board[rs][cs] = (s, d, z)

while position < c:
    for i in range(r):
        if board[i][position] != 0:
            ret += board[i][position][2]
            board[i][position] = 0
            break

    sharks = []

    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                temp = board[i][j]
                sharks.append((i, j, temp[0], temp[1], temp[2]))
                board[i][j] = 0

    for shark in sharks:
        r1, c1, s, d, z = shark
        move = 0
        nextr = r1
        nextc = c1
        if d == 0 or d == 1:
            move = s % ((r - 1) * 2)
        else:
            move = s % ((c - 1) * 2)

        while move > 0:
            if d == 0 and nextr == 0:
                d = 1
            if d == 1 and nextr == r-1:
                d = 0
            if d == 2 and nextc == c-1:
                d = 3
            if d == 3 and nextc == 0:
                d = 2
            nextr = nextr + dy[d]
            nextc = nextc + dx[d]
            move -= 1

        if board[nextr][nextc] == 0:
            board[nextr][nextc] = [(s,d,z)]
        else:
            board[nextr][nextc].append((s,d,z))

    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                big = sorted(board[i][j], key=lambda x: x[2], reverse=True)[0]
                board[i][j] = big
    position += 1




print(ret)
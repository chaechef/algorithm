line1 = list(map(int, input().split(" ")))
board = [[0] * line1[1] for _ in range(line1[0])]
curr = (line1[2], line1[3])
dice = [[" ", 0, " "],
        [ 0, 0, 0 ],
        [" ", 0, " "],
        [" ", 0, " "]]
dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]

for i in range(line1[0]):
    arr = list(map(int, input().split(" ")))
    for j in range(line1[1]):
        board[i][j] = arr[j]

command = list(map(int, input().split(" ")))


def rolling(direct):
    if direct == 1:
        temp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = temp
    if direct == 2:
        temp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = temp
    if direct == 3:
        temp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = temp
    if direct == 4:
        temp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = temp


board

for c in command:
    ny, nx = curr[0] + dy[c], curr[1] + dx[c]
    if ny < 0 or nx < 0 or ny >= line1[0] or nx >= line1[1]:
        continue
    rolling(c)
    if board[ny][nx] == 0:
        board[ny][nx] = dice[3][1]
    else:
        dice[3][1] = board[ny][nx]
        board[ny][nx] = 0
    curr = (ny, nx)
    print(dice[1][1])



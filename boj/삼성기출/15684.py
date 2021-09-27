from itertools import combinations

n, m ,h = map(int, input().split())
board = [[0] * n for _ in range(h)]

for _ in range(m):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1

arr = []
for i in range(h):
    for j in range(n):
        if board[i][j] == 0:
            arr.append((i,j))


def simulate(sboard, idx: int):
    cy, cx = 0, idx
    while cy < h:
        if cx + 1 < n and sboard[cy][cx] == 1:
            cx += 1
            cy += 1
        elif cx - 1 >= 0 and sboard[cy][cx - 1] == 1:
            cx -= 1
            cy += 1
        else:
            cy += 1
    return cx

flag = True
for line in list(map(lambda x: list(combinations(arr, x)), range(4))):
    if not flag:
        break
    for eles in line:
        if not flag:
            break

        for ele in eles:
            board[ele[0]][ele[1]] = 1

        for i in range(n):
            if i != simulate(board, i):
                for ele in eles:
                    board[ele[0]][ele[1]] = 0
                break
        else:
            for ele in eles:
                board[ele[0]][ele[1]] = 0
            if flag:
                print(len(eles))
                flag = False
            break

if flag:
    print(-1)
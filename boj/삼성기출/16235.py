#16235

n, m, k = map(int, input().split())
board = [[5] * n for _ in range(n)]
growth = [list(map(int, input().split())) for _ in range(n)]
treeBoard = [[[] for _ in range(n)] for _ in range(n)]
dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]

for _ in range(m):
    y, x, age = map(int, input().split())
    treeBoard[y-1][x-1].append(age,)


for _ in range(k):

    for i in range(n):
        for j in range(n):
            if len(treeBoard[i][j]) == 0:
                continue

            target = treeBoard[i][j]
            newTarget = []
            deadTrees = []
            for a in reversed(range(len(target))):
                if board[i][j] >= target[a]:
                    board[i][j] -= target[a]
                    newTarget.append(target[a]+1)
                else:
                    deadTrees.append(target[a])
            treeBoard[i][j] = list(reversed(newTarget))
            for dead in deadTrees:
                plus = int(dead / 2)
                board[i][j] += plus

    # 번식
    for i in range(n):
        for j in range(n):
            if len(treeBoard[i][j]) == 0:
                continue
            target = treeBoard[i][j]
            cc = 0
            for ta in target:
                if ta % 5 == 0:
                    cc += 1

            for d in range(8):
                ny, nx = i + dy[d], j + dx[d]
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                treeBoard[ny][nx].extend([1] * cc)

    for i in range(n):
        for j in range(n):
            board[i][j] += growth[i][j]

ret = 0

for i in range(n):
    for j in range(n):
        ret += len(treeBoard[i][j])

print(ret)
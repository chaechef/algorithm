n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [1,1,-1,-1]
dx = [-1,1,1,-1]
gmin = 4000000000

for i in range(n):
    for j in range(n):
        for d1 in range(1, j+1):
            maxd2 = min(n-j, n-i-d1)
            for d2 in range(1, maxd2):
                cboard = [[0] * n for _ in range(n)]
                cy, cx = i, j
                cboard[cy][cx] = 5
                for c in range(4):
                    count = d1 if c % 2 == 0 else d2
                    for _ in range(count):
                        ny, nx = cy + dy[c], cx + dx[c]
                        cboard[ny][nx] = 5
                        cy, cx = ny, nx

                for line in cboard:
                    if line.count(5) == 2:
                        for five in range(line.index(5)+1, line.index(5, line.index(5)+1)):
                            line[five] = 5
                for ii in range(n):
                    for jj in range(n):
                        if cboard[ii][jj] == 5:
                            continue
                        if ii < i + d1 and jj <= j:
                            cboard[ii][jj] = 1
                        elif ii <= i + d2 and j < jj < n:
                            cboard[ii][jj] = 2
                        elif i + d1 <= ii < n and jj < j - d1 + d2:
                            cboard[ii][jj] = 3
                        elif i + d2 < ii < n and j - d1 + d2 <= jj < n:
                            cboard[ii][jj] = 4
                arr = [0] * 5
                for ai in range(n):
                    for aj in range(n):
                        arr[cboard[ai][aj] - 1] += board[ai][aj]

                gmin = min(gmin, max(arr) - min(arr))

print(gmin)




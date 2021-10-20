from collections import deque

n, k = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(2**n)]
opers = list(map(int, input().split()))
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def recursion(y1, x1, y2, x2, nn: int):
    if nn == 0:
        # rotate
        prev = [[0] * (x2 - x1) for _ in range(y2 - y1)]
        for i in range(y1, y2):
            for j in range(x1, x2):
                # 원래는 행 i - y1 열 j - x1
                prev[j-x1][y2 - i - 1] = board[i][j]

        for i in range(len(prev)):
            for j in range(len(prev[0])):
                board[i+y1][j+x1] = prev[i][j]
        return

    midy = int((y1 + y2) / 2)
    midx = int((x1 + x2) / 2)
    recursion(y1, x1, midy, midx, nn - 1)
    recursion(midy, midx, y2, x2, nn - 1)
    recursion(midy, x1, y2, midx, nn - 1)
    recursion(y1, midx, midy, x2, nn - 1)


for oper in opers:
    nth = n - oper
    recursion(0, 0, 2**n, 2**n, nth)
    visited = [[0] * 2**n for _ in range(2**n)]
    queue = deque()
    removelist = []
    for i in range(2**n):
        for j in range(2**n):
            if board[i][j] == 0:
                continue

            count = 0

            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if ny < 0 or nx < 0 or ny >= 2**n or nx >= 2**n:
                    continue
                if board[ny][nx] > 0:
                    count += 1
            if count < 3:
                removelist.append((i, j))

    for ice in removelist:
        cy, cx = ice
        board[cy][cx] -= 1

ret1 = 0
ret2 = 0
for i in range(2**n):
    for j in range(2**n):
        ret1 += board[i][j]

visited = [[0] * 2**n for _ in range(2**n)]

for i in range(2**n):
    for j in range(2**n):
        if board[i][j] == 0:
            visited[i][j] = 1
            continue
        if visited[i][j] == 1:
            continue
        queue = deque()
        visited[i][j] = 1
        queue.append((i,j))
        count = 1
        while queue:
            cy, cx = queue.popleft()
            for d in range(4):
                ny, nx = cy + dy[d], cx + dx[d]
                if ny < 0 or nx < 0 or ny >= 2**n or nx >= 2**n:
                    continue
                if visited[ny][nx] == 1:
                    continue
                if board[ny][nx] == 0:
                    continue
                queue.append((ny,nx))
                visited[ny][nx] = 1
                count += 1
        ret2 = max(ret2, count)


print(ret1)
print(ret2)
from collections import deque
n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
loop = 0
dy = [1,0,-1,0]
dx = [0,1,0,-1]
while True:
    visited = [[0] * n for _ in range(n)]
    group = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                countries = [(i,j)]
                queue = deque()
                queue.append((i, j))
                while queue:
                    cy, cx = queue.popleft()
                    for ii in range(4):
                        ny, nx = cy + dy[ii], cx + dx[ii]
                        if ny < 0 or ny >= n or nx < 0 or nx >= n:
                            continue
                        if visited[ny][nx] == 1:
                            continue
                        if l <= abs(board[cy][cx] - board[ny][nx]) <= r:
                            countries.append((ny,nx))
                            queue.append((ny,nx))
                            visited[ny][nx] = 1

                if len(countries) > 1:
                    group.append(countries)

    if len(group) == 0:
        break
    loop += 1
    for candi in group:
        sum = 0
        for c in candi:
            sum += board[c[0]][c[1]]

        avg = int(sum / len(candi))
        for c in candi:
            board[c[0]][c[1]] = avg

print(loop)
n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
cy, cx = int(n/2), int(n/2)
visited = [[0] * n for _ in range(n)]
visited[int(n / 2)][int(n / 2)] = 1
cdirect = 0
dy = [-1,0,1,0]
dx = [0,-1,0,1]
result = 0

while True:
    if cy == 0 and cx == 0:
        break
    ny, nx = 0, 0
    lefty, leftx = cy + dy[(cdirect + 1) % 4], cx + dx[(cdirect + 1) % 4]
    if lefty >= 0 and lefty < n and leftx >= 0 and leftx < n and visited[lefty][leftx] == 0:
        # 왼쪽으로 감
        visited[lefty][leftx] = visited[cy][cx] + 1
        cdirect = (cdirect + 1) % 4
        ny, nx = lefty, leftx
    else:
        # 방향 그대로 감
        straighty, straightx = cy + dy[cdirect], cx + dx[cdirect]
        visited[straighty][straightx] = visited[cy][cx] + 1
        ny, nx = straighty, straightx

    totalsend = board[ny][nx]
    dileft = (cdirect + 1) % 4
    diright = (cdirect - 1) % 4
    diffSum = 0

    #### 5%
    nnny, nnnx = ny + 2 * dy[cdirect], nx + 2 * dx[cdirect]
    if 0 <= nnny < n and 0 <= nnnx < n:
        diff = int(totalsend * 0.05)
        diffSum += diff
        board[nnny][nnnx] += diff
    else:
        diff = int(totalsend * 0.05)
        diffSum += diff
        result += diff


    ### 10%
    nny, nnx = ny + dy[cdirect], nx + dx[cdirect]

    if 0 <= nny + dy[dileft] < n and 0 <= nnx + dx[dileft] < n:
        diff = int(totalsend * 0.1)
        diffSum += diff
        board[nny + dy[dileft]][nnx + dx[dileft]] += diff
    else:
        diff = int(totalsend * 0.1)
        diffSum += diff
        result += diff

    if 0 <= nny + dy[diright] < n and 0 <= nnx + dx[diright] < n:
        diff = int(totalsend * 0.1)
        diffSum += diff
        board[nny + dy[diright]][nnx + dx[diright]] += diff
    else:
        diff = int(totalsend * 0.1)
        diffSum += diff
        result += diff

    #### 1%
    if 0 <= cy + dy[dileft] < n and 0 <= cx + dx[dileft] < n:
        diff = int(totalsend * 0.01)
        diffSum += diff
        board[cy + dy[dileft]][cx + dx[dileft]] += diff
    else:
        diff = int(totalsend * 0.01)
        diffSum += diff
        result += diff

    if 0 <= cy + dy[diright] < n and 0 <= cx + dx[diright] < n:
        diff = int(totalsend * 0.01)
        diffSum += diff
        board[cy + dy[diright]][cx + dx[diright]] += diff
    else:
        diff = int(totalsend * 0.01)
        diffSum += diff
        result += diff

    #### 7%
    if 0 <= ny + dy[dileft] < n and 0 <= nx + dx[dileft] < n:
        diff = int(totalsend * 0.07)
        diffSum += diff
        board[ny + dy[dileft]][nx + dx[dileft]] += diff
    else:
        diff = int(totalsend * 0.07)
        diffSum += diff
        result += diff

    if 0 <= ny + dy[diright] < n and 0 <= nx + dx[diright] < n:
        diff = int(totalsend * 0.07)
        diffSum += diff
        board[ny + dy[diright]][nx + dx[diright]] += diff
    else:
        diff = int(totalsend * 0.07)
        diffSum += diff
        result += diff


    #### 2%
    if 0 <= ny + dy[dileft] * 2 < n and 0 <= nx + dx[dileft] * 2 < n:
        diff = int(totalsend * 0.02)
        diffSum += diff
        board[ny + dy[dileft] * 2][nx + dx[dileft] * 2] += diff
    else:
        diff = int(totalsend * 0.02)
        diffSum += diff
        result += diff

    if 0 <= ny + dy[diright] * 2 < n and 0 <= nx + dx[diright] * 2 < n:
        diff = int(totalsend * 0.02)
        diffSum += diff
        board[ny + dy[diright] * 2][nx + dx[diright]* 2] += diff
    else:
        diff = int(totalsend * 0.02)
        diffSum += diff
        result += diff

    if 0 <= nny < n and 0 <= nnx < n:
        board[nny][nnx] += totalsend - diffSum
    else:
        result += totalsend - diffSum
    board[ny][nx] = 0
    cy, cx = ny, nx


print(result)
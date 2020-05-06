from collections import deque

n, m, k = map(int, input().split())

arr = [[0 for j in range(m)] for i in range(n)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            arr[j][k] = 1

count = 0


def inRnage(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    else:
        return False


def dfs(y, x, graph):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[y, x]])
    count = 0
    while queue:
        curr = queue.popleft()
        if graph[curr[0]][curr[1]] == 0:
            count += 1
            graph[curr[0]][curr[1]] = 1
            for i in range(4):
                ny, nx = curr[0] + dy[i], curr[1] + dx[i]
                if inRnage(ny, nx) and graph[ny][nx] == 0:
                    queue.append([ny,nx])
    return count


area = []
for y in range(n):
    for x in range(m):
        if arr[y][x] == 0:
            count += 1
            res = dfs(y, x, arr)
            area.append(res)

print(count)
area = sorted(area)
print(" ".join([str(i) for i in area]))
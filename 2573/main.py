import sys
from collections import deque


def check(y, x):
    count = 0
    for i in range(4):
        if graph[y+dy[i]][x+dx[i]] == 0:
            count += 1
    return count


def one_year():
    count = [0 for _ in range(len(ices))]
    newices = []
    for idx, val in enumerate(ices):
        count[idx] = check(val[0], val[1])

    for i in range(len(count)):
        cy, cx = ices[i][0], ices[i][1]
        graph[cy][cx] -= count[i]
        if graph[cy][cx] <= 0:
            graph[cy][cx] = 0
        else:
            newices.append([cy, cx])

    return newices


def bfs(start):
    queue = deque([start])
    count = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while queue:
        curr = queue.popleft()
        if visited[curr[0]][curr[1]] == 0:
            count += 1
            visited[curr[0]][curr[1]] = 1
            for i in range(4):
                ny, nx = curr[0] + dy[i], curr[1] + dx[i]
                if graph[ny][nx] != 0 and visited[ny][nx] == 0:
                    queue.append([ny, nx])
    return count


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [[int(i) for i in sys.stdin.readline().split()] for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ices = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                ices.append([i, j])

    year_count = 0

    while True:
        if len(ices) == 0:
            year_count = 0
            break
        countices = bfs(ices[0])
        if len(ices) != countices:
            break
        ices = one_year()
        year_count += 1

    print(year_count)
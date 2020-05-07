import sys
from collections import deque

def inRange(y, x):
    if 0 <= y < n and 0 <= x < n:
        return True
    else:
        return False


def bfs(y, x):
    visited = []
    queue = deque([[y,x]])

    while queue:
        curr = queue.popleft()
        if graph[curr[0]][curr[1]] == 1:
            visited.append(curr)
            graph[curr[0]][curr[1]] = 0
            for i in range(4):
                ny, nx = curr[0] + dy[i], curr[1] + dx[i]
                if inRange(ny,nx) and graph[ny][nx] != 0:
                    queue.append([ny, nx])

    return visited

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    graph = [[int(i) for i in sys.stdin.readline().split()] for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    countris = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                countris.append(bfs(i, j))

    globalmin = 100000
    for i in range(len(countris)):
        for j in range(len(countris)):
            if i != j:
                minlen = 10000
                for k in range(len(countris[i])):
                    for l in range(len(countris[j])):
                        y1, x1 = countris[i][k][0], countris[i][k][1]
                        y2, x2 = countris[j][l][0], countris[j][l][1]
                        temp = abs(y1-y2) + abs(x1-x2) - 1
                        if minlen > temp:
                            minlen = temp
                if globalmin > minlen:
                    globalmin = minlen
    print(globalmin)
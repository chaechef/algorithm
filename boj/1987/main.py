import sys


def inRange(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    else:
        return False


def dfs(y, x, count):
    if cache[y][x] < count:
        cache[y][x] = count

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if inRange(ny, nx) and alpabets[ord(item[ny][nx]) - 65] == 0:
            alpabets[ord(item[ny][nx]) - 65] = 1
            dfs(ny, nx, count+1)
            alpabets[ord(item[ny][nx]) - 65] = 0


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    item = [sys.stdin.readline() for i in range(n)]
    cache = [[0 for j in range(m)] for i in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    alpabets = [0] * 26
    alpabets[ord(item[0][0])-65] = 1
    dfs(0, 0, 1)
    print(max([max(i) for i in cache]))


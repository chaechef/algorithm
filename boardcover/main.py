import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check(y, x, tile):
    for t in tile:
        ny, nx = y + t[0], x + t[1]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            return False

        if board[ny][nx] != 0:
            return False
    else:
        return True


def set(y, x, tile, delta):
    for t in tile:
        ny, nx = y + t[0], x + t[1]
        board[ny][nx] = delta


def bf():
    tiles = [[(0, 0), (0, 1), (1, 0)],
             [(0, 0), (0, 1), (1, 1)],
             [(0, 0), (1, 0), (1, 1)],
             [(0, 0), (1, 0), (1, -1)]]

    cy, cx = 0, 0
    flag = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cy, cx = i, j
                flag = True
                break
        if flag:
            break

    if not flag:
        return 1

    ret = 0
    for tile in tiles:
        if check(cy, cx, tile):
            set(cy, cx, tile, 1)
            ret += bf()
            set(cy, cx, tile, 0)

    return ret



if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        board = [input().strip() for _ in range(n)]
        board = list(map(lambda a: [1 if val == '#' else 0 for val in list(a)], board))
        if sum(map(lambda a: a.count(0), board)) % 3 != 0:
            print(0)
            continue
        print(bf())



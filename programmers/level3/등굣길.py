from collections import deque
import sys
sys.setrecursionlimit(10**9)
def recursion(n,m, y,x):
    if y == 0 and x == 0:
        return 1

    xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    ret = 0
    for i in range(4):
        cy, cx = y + xy[i][0], x + xy[i][1]
        if 0 <= cy < n and 0 <= cx < m:
            if cache[y][x] - 1 == cache[cy][cx]:
                ret = (ret + recursion(n,m,cy,cx)) % 1000000007

    return ret



def solution(m, n, puddles):
    global cache
    global board
    board = [[0 for j in range(m)] for i in range(n)]
    cache = [[-1 for j in range(m)] for i in range(n)]

    for puddle in puddles:
        ta, tb = puddle
        board[tb-1][ta-1] = -1

    dq = deque([(0,0)])
    step = 0
    xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cache[0][0] = 0
    while dq:
        length = len(dq)
        for _ in range(length):
            curr = dq.popleft()
            for i in range(4):
                ny, nx = curr[0] + xy[i][0], curr[1] + xy[i][1]
                if 0 <= ny < n and 0 <= nx < m and cache[ny][nx] == -1 and board[ny][nx] != -1:
                    cache[ny][nx] = step + 1
                    dq.append((ny, nx))
        step += 1

    if cache[n-1][m-1] == -1:
        return 0
    answer = recursion(n, m, n-1, m-1)

    return answer


print(solution(4, 3, [[3,3],[2,3],[2,4]]))
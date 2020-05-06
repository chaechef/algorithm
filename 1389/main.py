import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    countnumber = [-1] * (n + 1)
    countnumber[start] = 0
    while queue:
        curr = queue.popleft()
        for i in range(1, n+1):
            if graph[curr][i] == 1 and countnumber[i] == -1:
                queue.append(i)
                countnumber[i] = countnumber[curr] + 1

    # print(f'start : {start} , {countnumber}')
    return sum(countnumber) + 1



if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [[0 for j in range(n+1)] for i in range(n+1)]
    kebins = [0] * (n + 1)
    for _ in range(m):
        t1, t2 = map(int, sys.stdin.readline().split())
        graph[t1][t2] = 1
        graph[t2][t1] = 1


    min = 10000
    minidx = 0
    for i in range(1,n+1):
        kebins[i] = bfs(i)
        if kebins[i] < min:
            min = kebins[i]
            minidx = i

    print(minidx)
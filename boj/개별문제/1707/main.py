import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    vertaxes[start] = 1
    while queue:
        curr = queue.popleft()
        curr_color = vertaxes[curr]
        next_color = (vertaxes[curr] + 1) % 2
        for i in range(len(graph_list[curr])):
            ni = graph_list[curr][i]
            if vertaxes[ni] == curr_color:
                return False
            elif vertaxes[ni] == -1:
                queue.append(ni)
                vertaxes[ni] = next_color

    return True


if __name__ == "__main__":
    testcase = int(sys.stdin.readline())
    for _ in range(testcase):
        v, e = map(int,sys.stdin.readline().split())
        graph_list = [[] for i in range(v+1)]
        vertaxes = [-1] * (v+1)
        res = True
        for _ in range(e):
            t1, t2 = map(int, sys.stdin.readline().split())
            graph_list[t1].append(t2)
            graph_list[t2].append(t1)

        for i in range(1, v+1):
            if vertaxes[i] == -1:
                res = bfs(i)
                if not res:
                    break

        if res:
            print("YES")
        else:
            print("NO")
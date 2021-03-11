import sys
from collections import deque


def bfs(graph_list, start):
    visit_path = []
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        if curr not in visit_path:
            visit_path.append(curr)
            queue += sorted(graph_list[curr] - set(visit_path))

    return visit_path


def dfs(graph_list, start):
    visit_path = []
    stack = [start]
    while stack:
        curr = stack.pop()
        if curr not in visit_path:
            visit_path.append(curr)
            stack += sorted(graph_list[curr] - set(visit_path), reverse=True)
    return visit_path


if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().split())
    graph_list = [set([]) for _ in range(n+1)]

    for _ in range(m):
        i, j = map(int, input().split())
        graph_list[i].add(j)
        graph_list[j].add(i)

    print(" ".join(map(str,dfs(graph_list, v))))
    print(" ".join(map(str,bfs(graph_list, v))))


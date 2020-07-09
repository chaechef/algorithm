from collections import deque

def solution(n, edge):
    graph = {i: set() for i in range(1, n+1)}
    visited = [-1] * n
    for e in edge:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    visited[0] = 0
    dq = deque([1])
    while dq:
        curr = dq.popleft()
        for e in list(graph[curr]):
            if visited[e-1] == -1:
                visited[e-1] = visited[curr-1] + 1
                dq.append(e)

    return visited.count(max(visited))


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
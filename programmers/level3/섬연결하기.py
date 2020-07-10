def solution(n, costs):
    answer = 0
    graph = [[0 for j in range(n)]for i in range(n)]
    visited = [False] * n
    dist = [float('inf')] * n

    for cost in costs:
        a1, a2, c = cost
        graph[a1][a2] = c
        graph[a2][a1] = c

    dist[0] = 0
    # visited[0] = True

    for i in range(n):
        now = -1
        min_dist = float('inf')
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                now = j
                min_dist = dist[j]
        answer += min_dist
        visited[now] = True

        for j in range(n):
            if graph[now][j] != 0 and not visited[j]:
                dist[j] = min(dist[j], graph[now][j])

    return answer


solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
from collections import deque

def solution(n, computers):
    answer = 0
    graph = {i:set([]) for i in range(n)}
    check = [False] * n
    for line in range(len(computers)):
        for idx in range(len(computers[line])):
            if computers[line][idx] == 1:
                graph[line].add(idx)

    while True:
        que = deque([])
        for i in range(n):
            if not check[i]:
                que.append(i)
                break
        else:
            break

        while que:
            curr = que.popleft()
            check[curr] = True

            for val in list(graph[curr]):
                if not check[val]:
                    que.append(val)
        answer += 1


    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
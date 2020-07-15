import copy
import sys
sys.setrecursionlimit(10**9)


def dfs(graph, topick, path):
    global answer

    if topick == 0:
        if not answer:
            answer = path[:]
        return

    curr = path[-1]
    if curr not in graph:
        return

    for i in range(len(graph[curr])):
        cpy = copy.deepcopy(graph)
        cpy[curr] = graph[curr][:i] + graph[curr][i+1:]
        tpath = path[:] + [graph[curr][i]]
        dfs(cpy, topick-1, tpath)


def solution(tickets):
    global answer
    curr = 'ICN'
    answer = []
    graph = {}

    for ticket in tickets:
        if ticket[0] not in graph:
            graph[ticket[0]] = [ticket[1]]
        else:
            graph[ticket[0]].append(ticket[1])

    for g in graph:
        graph[g].sort()

    dfs(graph, len(tickets), [curr])
    return answer

print(solution([['ICN', '1'], ['1','2'], ['2','1']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN'],['ICN', 'B'], ['B', 'ICN']]))
print(solution( [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]))
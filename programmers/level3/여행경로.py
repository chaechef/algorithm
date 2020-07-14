def recursion(curr, graph, path):


def solution(tickets):
    curr = 'ICN'
    answer = []
    graph = {}
    for ticket in tickets:
        if graph.get(ticket[0], -1) == -1:
            graph[ticket[0]] = [ticket[1]]
        else:
            graph[ticket[0]].append(ticket[1])

    answer = recursion(curr, graph, [])

    return answer


print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))

def solution(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)} # 기억
    for val in zip(genres, plays, range(len(plays))):
        d[val[0]].append([val[1], val[2]])

    arr = sorted(d.values(), reverse=True, key=lambda a: sum([b[0] for b in a])) # 기억 
    arr = [sorted(a, reverse=True, key=lambda b: b[0]) for a in arr]

    for i in arr:
        for j in range(len(i)):
            if j == 2:
                break
            answer.append(i[j][1])

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
from collections import deque


def isdiffer(str1, str2):
    count = 0
    for a, b in zip(str1, str2):
        if a != b:
            count += 1

    return True if count == 1 else False

def solution(begin, target, words):
    if target not in words:
        return 0
    words= set(words)
    wordd = {word: 0 for word in words}
    wordd[begin] = 0
    dq = deque([begin])
    while dq:
        if target in dq:
            return wordd[target]
        curr = dq.popleft()
        for word in words:
            if isdiffer(curr, word):
                dq.append(word)
                wordd[word] = wordd[curr] + 1

    return 0



print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
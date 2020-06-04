import sys
from collections import deque

def bfs(begin , target, words):
    visited = [begin]
    queue = deque([begin])
    level = {}
    level[begin] = 0
    for val in words:
        level[val] = 0

    while queue:
        curr = queue.popleft()
        if curr == target:
            return level[curr]

        for val in words:
            count = 0
            for i in range(len(begin)):
                if val[i] != curr[i]:
                    count += 1
            if count == 1 and val not in visited:
                visited.append(val)
                queue.append(val)
                level[val] = level[curr] + 1
    return 0




def solution(begin, target, words):
    ret = bfs(begin, target, words)
    return ret


if __name__ == "__main__":
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

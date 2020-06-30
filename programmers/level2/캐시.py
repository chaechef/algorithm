from collections import deque


def solution(cacheSize, cities):
    cities = [val.lower() for val in cities]
    answer = 0
    cache = {}

    if cacheSize == 0:
        return 5 * len(cities)

    for idx, city in enumerate(cities):

        if len(cache) == 0:
            cache[city] = idx
            answer += 5
            continue
        if city in cache:
            cache[city] = idx
            answer += 1
        else:
            if len(cache) == cacheSize:
                imin = min(cache.values())
                target = ""
                for cc, ii in cache.items():
                    if ii == imin:
                        target = cc
                        break
                cache.pop(target)
            cache[city] = idx
            answer += 5

    return answer

print(solution(3, ['asdf','asdf','asdf']))
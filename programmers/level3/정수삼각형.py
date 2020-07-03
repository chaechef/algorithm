def solution(triangle):
    cache = [[0 for m in l]for l in triangle]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            cache[i][j] = triangle[i][j]
            ta, tb = -1, -1
            if 0 <= i - 1 and 0 <= j < len(triangle[i-1]):
                ta = cache[i-1][j]
            if 0 <= i - 1 and 0 <= j - 1 < len(triangle[i-1]):
                tb = cache[i-1][j-1]
            if max(ta, tb) != -1:
                cache[i][j] += max(ta, tb)

    return max(cache[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
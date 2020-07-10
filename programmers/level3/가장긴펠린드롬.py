def solution(s):
    answer = 1
    l = len(s)
    cache = [[False for i in range(l)] for j in range(l)]

    for i in range(len(s)):
        cache[i][i] = True

    for i in range(0, l-1):
        if s[i] == s[i+1]:
            cache[i][i+1] = True

    for i in range(2, l):
        for j in range(0, l-i):
            if s[j] == s[j+i] and cache[j+1][j+i-1] == True:
                cache[j][j+i] = True
                if i + 1 > answer:
                    answer = i + 1

    return answer


print(solution('abcdcba'))
from itertools import combinations

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
mmin = 100000000000
for com in list(combinations(range(n), int(n / 2))):
    arr2 = []
    sum = 0
    sum1 = 0
    for i in range(n):
        if i not in com:
            arr2.append(i)

    for i in com:
        for j in com:
            if i == j:
                continue
            sum += board[i][j]
    for i in arr2:
        for j in arr2:
            if i == j:
                continue
            sum1 += board[i][j]

    mmin = min(mmin, abs(sum1 - sum))

print(mmin)
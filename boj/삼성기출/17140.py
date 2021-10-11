r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
count = 100

def countElement(arr: list):
    e = {}
    for num in arr:
        if num == 0:
            continue
        if num in e.keys():
            e[num] += 1
        else:
            e[num] = 1
    temp = list(map(lambda x: (x, e[x]), e.keys()))
    return sorted(temp, key=lambda x: (x[1], x[0]))


for tc in range(count):

    if r - 1 < len(board) and c - 1 < len(board[0]) and board[r-1][c-1] == k:
        print(tc)
        break
    if len(board) >= len(board[0]):
        news = []
        maxwidth = 0
        for line in board:
            temp = countElement(line)
            new = []
            for a in temp:
                new.append(a[0])
                new.append(a[1])
            maxwidth = max(maxwidth, len(new))
            news.append(new)

        for new in news:
            if len(new) < maxwidth:
                for _ in range(maxwidth - len(new)):
                    new.append(0)
        board = news
    else:
        cc = len(board[0])
        news = []
        maxHeight = 0

        for i in range(cc):
            arr = [line[i] for line in board]
            temp = countElement(arr)
            new = []
            for a in temp:
                new.append(a[0])
                new.append(a[1])
            maxHeight = max(maxHeight, len(new))
            news.append(new)

        for new in news:
            if len(new) < maxHeight:
                for _ in range(maxHeight - len(new)):
                    new.append(0)

        board = [[0] * cc for _ in range(maxHeight)]
        for j in range(cc):
            for i in range(maxHeight):
                board[i][j] = news[j][i]

else:
    print(-1)

from collections import deque
n, m, currentFuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
taxiY, taxiX = map(lambda x: x - 1, map(int, input().split()))
startBoard = [[0] * n for _ in range(n)]
finishDict = {}
dy = [0,0,1,-1]
dx = [1,-1,0,0]
needWork = m
distDict = {}

for i in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    startBoard[y1-1][x1-1] = i + 1
    finishDict[i+1] = (y2-1, x2-1)


def makeDistBoard(a: int, b: int):
    dist = [[-1] * n for _ in range(n)]
    dist[a][b] = 0
    queue = deque()
    queue.append((a, b))
    while queue:
        cy, cx = queue.popleft()
        for ii in range(4):
            ny, nx = cy + dy[ii], cx + dx[ii]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] == 1:
                continue
            if dist[ny][nx] != -1 and dist[ny][nx] <= dist[cy][cx] + 1:
                continue
            dist[ny][nx] = dist[cy][cx] + 1
            queue.append((ny, nx))
    return dist


while needWork > 0:
    distBoard = []
    if (taxiY, taxiX) in distDict.keys():
        distBoard = distDict[(taxiY, taxiX)]
    else:
        distBoard = makeDistBoard(taxiY, taxiX)

    minDist = 1000000
    nextPosition = (-1, -1)
    for i in range(n):
        for j in range(n):
            if startBoard[i][j] != 0 and distBoard[i][j] != -1 and distBoard[i][j] < minDist:
                minDist = distBoard[i][j]
                nextPosition = (i, j)

    if nextPosition == (-1, -1):
        # 사람이있는데 못가는경우
        print(-1)
        break

    needFuel = minDist
    if currentFuel < needFuel:
        # 연료부족
        print(-1)
        break
    # print("nextPosition", nextPosition)
    # print("needFuel", needFuel)
    currentFuel -= needFuel
    taxiY, taxiX = nextPosition
    currId = startBoard[taxiY][taxiX]
    startBoard[taxiY][taxiX] = 0

    if (taxiY, taxiX) in distDict.keys():
        distBoard = distDict[(taxiY, taxiX)]
    else:
        distBoard = makeDistBoard(taxiY, taxiX)

    finishPosition = finishDict[currId]

    if distBoard[finishPosition[0]][finishPosition[1]] == -1:
        # 목적지 까지 못가는 경우
        print(-1)
        break

    needFinishFuel = distBoard[finishPosition[0]][finishPosition[1]]
    if currentFuel < needFinishFuel:
        # 연료부족
        print(-1)
        break
    # print("finishPosition", finishPosition)
    # print("needFinishFuel", needFinishFuel)
    #
    # print("currFuel", currentFuel)
    currentFuel += needFinishFuel
    taxiY, taxiX = finishPosition[0], finishPosition[1]
    needWork -= 1
else:
    print(currentFuel)
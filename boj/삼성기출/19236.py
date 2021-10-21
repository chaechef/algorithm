
board = [[(0,0)] * 4 for _ in range(4)]
fishPosition = [(0,0)] * 16
score = 0
sy, sx = 0, 0

for i in range(4):
    toks = list(map(int, input().split()))
    for j in range(4):
        num, di = toks[2*j], toks[2*j + 1]
        board[i][j] = (num, di-1)
        fishPosition[num-1] = (i,j)


ffId, ffdi = board[0][0]
board[0][0] = " "
score += ffId
sd = ffdi
fishPosition[ffId-1] = " "
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
ret = 0
def recursion(sharkY, sharkX, sharkDi, board, fishArr, score):
    global ret
    checkY, checkX = sharkY + dy[sharkDi], sharkX + dx[sharkDi]
    if checkY < 0 or checkX < 0 or checkY >= 4 or checkX >= 4:
        ret = max(ret, score)
        return

    newBoard = [[board[i][j] for j in range(4)]for i in range(4)]
    newFishArr = fishArr[:]
    for fi in range(16):
        if newFishArr[fi] == " ":
            continue
        cfy, cfx = newFishArr[fi]  # current fish y ,x di
        fid, cfd = newBoard[cfy][cfx]
        nextDirect = -1
        # id == fi 랑 같아야함
        for d in range(8):
            nfd = (cfd + d) % 8
            tnfy, tnfx = cfy + dy[nfd], cfx + dx[nfd]
            if tnfy < 0 or tnfx < 0 or tnfy >= 4 or tnfx >= 4:
                continue
            if tnfy == sharkY and tnfx == sharkX:
                continue
            nextDirect = nfd
            break

        nfy, nfx = cfy + dy[nextDirect], cfx + dx[nextDirect]
        if newBoard[nfy][nfx] == " ":
            # 빈칸환
            newBoard[nfy][nfx] = (fid, nextDirect)
            newFishArr[fi] = (nfy, nfx)
            newBoard[cfy][cfx] = " "
        else:
            # 교
            temp = newBoard[nfy][nfx]
            newBoard[nfy][nfx] = (fid, nextDirect)
            newFishArr[fi] = (nfy, nfx)
            newBoard[cfy][cfx] = temp
            newFishArr[temp[0]-1] = (cfy, cfx)

    step = 0
    while True:
        nsy, nsx = sharkY + dy[sharkDi] * step, sharkX + dx[sharkDi] * step
        if nsy < 0 or nsx < 0 or nsy >= 4 or nsx >= 4:
            break
        step += 1

    flag = 0
    for s in range(1, step):
        nsy, nsx = sharkY + dy[sharkDi] * s, sharkX + dx[sharkDi] * s
        if newBoard[nsy][nsx] == " ":
            continue
        tarFishId, tarFishDi = newBoard[nsy][nsx]
        nextSharkY, nextSharkX = nsy, nsx
        tempFishPosition = newFishArr[tarFishId - 1]
        tempBoardFish = newBoard[nsy][nsx]
        newBoard[nsy][nsx] = " "
        newFishArr[tarFishId - 1] = " "
        recursion(nextSharkY, nextSharkX, tarFishDi, newBoard, newFishArr, score + tarFishId)
        newFishArr[tarFishId - 1] = tempFishPosition
        newBoard[nsy][nsx] = tempBoardFish
        flag += 1

    if flag == 0:
        ret = max(ret, score)


recursion(0,0,ffdi, board, fishPosition, score)

print(ret)
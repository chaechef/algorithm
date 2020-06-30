def solution(board):
    transboard = [list(tu) for tu in zip(*board)]
    maxlen = min(len(board), len(transboard))
    answer = 0
    for widthlen in range(1, maxlen+1):
        # width : 1...2...3...4...5...6...7
        for i in range(0, len(board) - widthlen + 1):
            for j in range(0, len(board[0]) - widthlen + 1):
                tempsum = 0
                for k in range(i, i+widthlen):
                    tempsum += sum(board[k][j:j+widthlen])
                if tempsum == widthlen ** 2 and answer < tempsum:
                    answer = tempsum

    return answer


solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])